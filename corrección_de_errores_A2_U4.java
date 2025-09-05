//Error 1
public class SintaxisError {
    public static void main(String[] args) {
        int numero = 10;
        System.out.println("El número es: " + numero);
    }
}

//Error 2
public class SemanticoError {
    public static void main(String[] args) {
        int edad = 20;
        if (edad > 18) {
            System.out.println("Eres mayor de edad");
        }
    }
}

//Error 3
public class LogicoError {
    public static void main(String[] args) {
        int suma = 0;
        for (int i = 1; i <= 5; i++) {
            suma = suma + i;
        }
        System.out.println("La suma de los primeros 5 números es: " + suma);
    }
}

//Error 4
public class EjecucionError {
    public static void main(String[] args) {
        int numerador = 10;
        int denominador = 0;
        if (denominador != 0) {
            int resultado = numerador / denominador;
            System.out.println("Resultado: " + resultado);
        } else {
            System.out.println("Error: no se puede dividir entre cero");
        }
    }
}

//Solo como nota final pues puse todos juntos, pero se deberán guardar con sus respectivos nombres xd
