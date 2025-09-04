import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def calcular_ruta_critica(grafo):
    if not nx.is_directed_acyclic_graph(grafo):
        raise ValueError("El grafo debe ser un DAG (sin ciclos) para aplicar CPM.")

    orden_topologico = list(nx.topological_sort(grafo))

    ES = {n: 0.0 for n in grafo.nodes()}
    EF = {n: 0.0 for n in grafo.nodes()}
    dur = {n: float(grafo.nodes[n].get('duracion', 0.0)) for n in grafo.nodes()}

    for nodo in orden_topologico:
        predecesores = list(grafo.predecessors(nodo))
        if predecesores:
            ES[nodo] = max(EF[p] for p in predecesores)
        else:
            ES[nodo] = 0.0
        EF[nodo] = ES[nodo] + dur[nodo]

    duracion_proyecto = max(EF.values()) if EF else 0.0

    LF = {n: duracion_proyecto for n in grafo.nodes()}
    LS = {n: 0.0 for n in grafo.nodes()}
    for nodo in reversed(orden_topologico):
        sucesores = list(grafo.successors(nodo))
        if sucesores:
            LF[nodo] = min(LS[s] for s in sucesores)
        else:
            LF[nodo] = duracion_proyecto
        LS[nodo] = LF[nodo] - dur[nodo]

    Holgura = {n: LS[n] - ES[n] for n in grafo.nodes()}

    df_resultado = pd.DataFrame({
        'Actividad': orden_topologico,
        'Duracion': [dur[n] for n in orden_topologico],
        'ES': [ES[n] for n in orden_topologico],
        'EF': [EF[n] for n in orden_topologico],
        'LS': [LS[n] for n in orden_topologico],
        'LF': [LF[n] for n in orden_topologico],
        'Holgura': [Holgura[n] for n in orden_topologico],
    })

    nodos_criticos = [n for n,s in Holgura.items() if abs(s) < 1e-9]

    fuentes = [n for n in grafo.nodes() if grafo.in_degree(n) == 0]
    sumideros = [n for n in grafo.nodes() if grafo.out_degree(n) == 0]
    rutas_criticas = []
    for f in fuentes:
        for s in sumideros:
            for camino in nx.all_simple_paths(grafo, f, s):
                if all(n in nodos_criticos for n in camino):
                    longitud_camino = sum(dur[n] for n in camino)
                    if abs(longitud_camino - duracion_proyecto) < 1e-9:
                        if camino not in rutas_criticas:
                            rutas_criticas.append(camino)

    return df_resultado, duracion_proyecto, nodos_criticos, rutas_criticas


def graficar_con_ruta_critica(grafo, nodos_criticos, rutas_criticas, nombre_archivo):
    pos = nx.spring_layout(grafo, seed=42) 
    aristas_criticas = set()
    for ruta in rutas_criticas:
        aristas_criticas.update(zip(ruta, ruta[1:]))

    colores_nodos = ['red' if n in nodos_criticos else 'lightgray' for n in grafo.nodes()]
    colores_aristas = ['red' if (u,v) in aristas_criticas else 'black' for u,v in grafo.edges()]
    grosores = [3 if (u,v) in aristas_criticas else 1 for u,v in grafo.edges()]

    etiquetas = {n: f"{n}\n({grafo.nodes[n].get('duracion',0)})" for n in grafo.nodes()}

    plt.figure(figsize=(9,6))
    nx.draw_networkx_nodes(grafo, pos, node_color=colores_nodos, node_size=1200)
    nx.draw_networkx_edges(grafo, pos, edge_color=colores_aristas, width=grosores, arrowsize=18)
    nx.draw_networkx_labels(grafo, pos, labels=etiquetas, font_size=9)
    plt.title(nombre_archivo)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=200)
    plt.close()


def proyecto_construccion():
    g = nx.DiGraph()
    g.add_node('A', nombre='Cimientos', duracion=5)
    g.add_node('B', nombre='Paredes', duracion=10)
    g.add_node('C', nombre='Plomeria', duracion=4)
    g.add_node('D', nombre='InstalElectrica', duracion=3)
    g.add_node('E', nombre='Techo', duracion=6)
    g.add_node('F', nombre='PinturaInterior', duracion=2)
    g.add_node('G', nombre='PinturaExterior', duracion=2)
    g.add_node('H', nombre='Finalizacion', duracion=0)
    g.add_edges_from([
        ('A','B'), ('A','C'), ('A','D'),
        ('B','E'), ('C','F'), ('D','F'),
        ('E','G'), ('F','H'), ('G','H'),
    ])
    return g

def proyecto_software():
    g = nx.DiGraph()
    g.add_node('A', nombre='Requisitos', duracion=4)
    g.add_node('B', nombre='Diseno', duracion=6)
    g.add_node('C', nombre='ImplementacionM1', duracion=8)
    g.add_node('D', nombre='ImplementacionM2', duracion=7)
    g.add_node('E', nombre='Integracion', duracion=3)
    g.add_node('F', nombre='Pruebas', duracion=5)
    g.add_node('G', nombre='Despliegue', duracion=1)
    g.add_node('H', nombre='Entrega', duracion=0)
    g.add_edges_from([
        ('A','B'), ('B','C'), ('B','D'),
        ('C','E'), ('D','E'), ('E','F'),
        ('F','G'), ('G','H'),
    ])
    return g

if __name__ == "__main__":
    grafo1 = proyecto_construccion()
    df1, dur1, nodos_criticos1, rutas_criticas1 = calcular_ruta_critica(grafo1)
    print("Ejemplo 1 - Duración total:", dur1)
    print(df1.to_string(index=False))
    df1.to_csv("CPM_ejemplo1_construccion.csv", index=False)
    graficar_con_ruta_critica(grafo1, nodos_criticos1, rutas_criticas1, "CPM_ejemplo1_construccion.png")

    grafo2 = proyecto_software()
    df2, dur2, nodos_criticos2, rutas_criticas2 = calcular_ruta_critica(grafo2)
    print("\nEjemplo 2 - Duración total:", dur2)
    print(df2.to_string(index=False))
    df2.to_csv("CPM_ejemplo2_software.csv", index=False)
    graficar_con_ruta_critica(grafo2, nodos_criticos2, rutas_criticas2, "CPM_ejemplo2_software.png")

    print("\nRutas críticas Ej1:", rutas_criticas1)
    print("Rutas críticas Ej2:", rutas_criticas2)

    print("\nSe generaron archivos CSV y PNG en la carpeta actual:")
    print(" - CPM_ejemplo1_construccion.csv")
    print(" - CPM_ejemplo1_construccion.png")
    print(" - CPM_ejemplo2_software.csv")
    print(" - CPM_ejemplo2_software.png")
