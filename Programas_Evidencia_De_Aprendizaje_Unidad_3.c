//Que onda, aqui le dejo los 3 codigos de la actividad (Los puse juntos para no enviarle tanto link


//Fibonacci_hasta_N.c
#include <stdio.h>
int main(void) {
    long long N;
    unsigned long long f0 = 0ULL, f1 = 1ULL, f2;

    printf("Ingrese N (entero no negativo): ");
    if (scanf("%lld", &N) != 1) {
        printf("Entrada inválida.\n");
        return 1;
    }

    if (N < 0) {                   
        printf("N inválido (debe ser no negativo).\n");
        return 1;
    }

    printf("Fibonacci (valores <= %lld):\n", N);
    printf("%llu", f0);            
    if (N >= 1) {
        printf(" %llu", f1);        
    }

    while (1) {
        f2 = f0 + f1;               
        if (f2 > (unsigned long long)N) break; 
        printf(" %llu", f2);
        f0 = f1;                     
        f1 = f2;
    }

    printf("\n");
    return 0;
}

//es_primo.c
#include <stdio.h>
#include <math.h>

int main(void) {
    long long n;
    printf("Ingrese un entero (n): ");
    if (scanf("%lld", &n) != 1) {
        printf("Entrada inválida.\n");
        return 1;
    }

    if (n < 2) {                    
        printf("%lld no es primo (menor que 2).\n", n);
        return 0;
    }
    if (n == 2) {                  
        printf("%lld es primo.\n", n);
        return 0;
    }
    if (n % 2 == 0) {              
        printf("%lld no es primo (divisible por 2).\n", n);
        return 0;
    }

    long long limite = (long long) sqrt((double)n); 
    for (long long i = 3; i <= limite; i += 2) {    
        if (n % i == 0) {
            printf("%lld no es primo (divisible por %lld).\n", n, i);
            return 0;
        }
    }

    printf("%lld es primo.\n", n); 
    return 0;
}

//Determinante_3x3.c
#include <stdio.h>

int main(void) {
    double a11, a12, a13, a21, a22, a23, a31, a32, a33;
    printf("Ingrese los 9 elementos de la matriz 3x3 (fila por fila):\n");
    if (scanf("%lf %lf %lf %lf %lf %lf %lf %lf %lf",
              &a11,&a12,&a13,&a21,&a22,&a23,&a31,&a32,&a33) != 9) {
        printf("Entrada inválida. Debe introducir 9 números.\n");
        return 1;
    }

    double det = a11*(a22*a33 - a23*a32)
               - a12*(a21*a33 - a23*a31)
               + a13*(a21*a32 - a22*a31);

    printf("Determinante = %lf\n", det);
    return 0;
}
