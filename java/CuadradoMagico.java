/**
 * Un cuadrado mágico es una matriz de 3x3 números enteros que cumple:
 *
 * 1. Contiene todos los números entre 1 y 9 sin repetir ninguno.
 * 2. La suma de todas las filas, columnas y diagonales (principal y
 *    contraprincipal) es la misma.
 */
public class CuadradoMagico {
    public static void main(String[] args) {
        int[][] c = new int[][] { { 4, 7, 5 },
                                  { 8, 2, 1 },
                                  { 6, 3, 9 } };
        boolean esMagico = true;

        // Comprobar la condición 1:

        // Compruebo si cada número está exactamente una vez:
        for (int i = 1; i <= 9; i++) {
            int cont = 0;
            // Busco el número en cada fila:
            for (int numFila = 0; numFila < c.length; numFila++) {
                int[] fila = c[numFila];
                // Busco el número dentro de la fila:
                for (int numCol = 0; numCol < fila.length; numCol++) {
                    int numero = fila[numCol];
                    if (numero == i) {
                        cont++;
                    }
                }
            }
            if (cont != 1) {
                esMagico = false;
                break;
            }
        }

        // Comprobar la condición 2:

        int suma = 0;

        if (esMagico) {
            System.out.println("El cuadrado ES mágico.");
        } else {
            System.out.println("El cuadrado NO ES mágico.");
        }
    }
}
