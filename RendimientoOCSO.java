import java.util.Scanner;
import java.util.InputMismatchException;
import java.text.DecimalFormat;

public class RendimientoOCSO {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    DecimalFormat df = new DecimalFormat("#0.00");

    int n = 0;
    while (true) {
      System.out.print("Ingrese el número de empleados (1-3): ");
      try {
        n = Integer.parseInt(sc.nextLine().trim());
        if (n >= 1 && n <= 3) break;
        System.out.println("Error: el número debe ser entre 1 y 3.");
      } catch (NumberFormatException e) {
        System.out.println("Entrada inválida. Introduce un entero (1-3).");
      }
    }

    double[] ventas = new double[n];
    for (int i = 0; i < n; i++) {
      while (true) {
        System.out.print("Venta del empleado " + (i+1) + " (>= 0): ");
        String linea = sc.nextLine().trim();
        try {
          double v = Double.parseDouble(linea);
          if (v < 0) {
            System.out.println("La venta no puede ser negativa. Intenta de nuevo.");
            continue;
          }
          ventas[i] = v;
          break;
        } catch (NumberFormatException ex) {
          System.out.println("Entrada inválida. Ingresa un número real (ej. 123.45).");
        }
      }
    }

    // Cálculos
    double total = 0.0;
    for (double v : ventas) total += v;
    double promedio = total / n;

    int idxMax = 0, idxMin = 0;
    for (int i = 1; i < n; i++) {
      if (ventas[i] > ventas[idxMax]) idxMax = i;
      if (ventas[i] < ventas[idxMin]) idxMin = i;
    }

    int countSobrePromedio = 0;
    for (double v : ventas) if (v > promedio) countSobrePromedio++;

    // Mostrar resultados
    System.out.println("\n--- RESULTADOS ---");
    for (int i = 0; i < n; i++) {
      System.out.println("Venta empleado " + (i+1) + ": $" + df.format(ventas[i]));
    }
    System.out.println("Total de ventas: $" + df.format(total));
    System.out.println("Promedio por empleado: $" + df.format(promedio));
    System.out.println("Empleado con venta más alta: Empleado " + (idxMax+1) + " ($" + df.format(ventas[idxMax]) + ")");
    System.out.println("Empleado con venta más baja: Empleado " + (idxMin+1) + " ($" + df.format(ventas[idxMin]) + ")");
    System.out.println("Número de empleados que superaron el promedio: " + countSobrePromedio);
    sc.close();
  }
}
