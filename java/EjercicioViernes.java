import java.util.LinkedList;
import java.util.Scanner;

/**
 * Escribir un programa en Java que almacene una lista de cadenas que
 * solicitará al usuario y que éste deberá introducir de una en una.
 * El usuario indicará mediante una cadena vacía que no quiere introducir
 * más cadenas. Finalmente, el programa deberá recorrer dicha lista mientras
 * va creando una nueva cadena que contiene la concatenación de las cadenas
 * de la lista. Explica en un comentario qué implementación concreta del
 * tipo List has usado y por qué.
 */

public class EjercicioViernes {
    public static void main(String[] args) {
        LinkedList<String> lst = new LinkedList<String>();
        Scanner sc = new Scanner(System.in);
        String cadena;

        while (!(cadena = otraCadena(sc)).equals("")) {
            lst.add(cadena);
        }

        StringBuilder sb = new StringBuilder();

        for (String e : lst) {
            sb.append(e);
        }
    }

    public static String otraCadena(Scanner s) {
        System.out.print("Escribe una cadena: ");
        String cadena = s.nextLine();
        return cadena;
    }
}
