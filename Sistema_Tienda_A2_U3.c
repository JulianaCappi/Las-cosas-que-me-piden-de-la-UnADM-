#include <stdio.h>

int main(void) {
    float precio = 0.0f;
    float subtotal = 0.0f;
    float descuento = 0.0f;
    float total = 0.0f;
    int leidos;

    printf("Ingrese el precio de cada artículo (Ingrese 0 para terminar):\n");

    while (1) {
        printf("Precio: $");
        leidos = scanf("%f", &precio);

        if (leidos != 1) {
            int c;
            printf("Entrada inválida. Por favor ingrese un número.\n");
            while ((c = getchar()) != '\n' && c != EOF) { /* descartar */ }
            continue;
        }

        if (precio < 0.0f) {
            printf("Precio no puede ser negativo. Intente de nuevo.\n");
            continue;
        }

        if (precio == 0.0f) {
            break;
        }

        subtotal += precio;
    }

    if (subtotal > 500.0f) {
        descuento = subtotal * 0.10f;
    } else {
        descuento = 0.0f;
    }

    total = subtotal - descuento;

    printf("\nSubtotal: $%.2f\n", subtotal);
    printf("Descuento: $%.2f\n", descuento);
    printf("Total a pagar: $%.2f\n", total);

    return 0;
}
