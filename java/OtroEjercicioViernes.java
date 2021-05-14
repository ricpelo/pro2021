import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Escribir un programa en Java que solicite al usuario la introducción de
 * una serie de cadenas y las almacene en una colección apropiada. El
 * usuario indicará mediante una cadena vacía que no quiere introducir más
 * cadenas. A continuación, el programa deberá preguntar al usuario si
 * desea que muestre las cadenas en el orden en el que se han introducido,
 * o bien en el orden contrario, y finalmente imprimirá las cadenas en el
 * orden elegido. Procurar escribir el código más breve y elegante posible.
 */

public class OtroEjercicioViernes {
    public static void main(String[] args) {
        LinkedList<String> lst = new LinkedList<String>();
        Scanner sc = new Scanner(System.in);
        String cadena;
        int orden;

        while (!(cadena = otraCadena(sc)).equals("")) {
            lst.add(cadena);
        }

        for (;;) {
            System.out.println("¿En qué orden quieres recorrer la lista?");
            System.out.print("(1 = Normal ; 2 = Contrario): ");

            if (sc.hasNextInt()) {
                orden = sc.nextInt();

                if (orden == 1 || orden == 2) {
                    break;
                }
            } else {
                sc.nextLine();
            }

            System.out.println("Opción incorrecta");
        }

        switch (orden) {
            case 1:
                for (String e : lst) {
                    System.out.println(e);
                }
                break;

            case 2:
                Iterator<String> it = lst.descendingIterator();

                while (it.hasNext()) {
                    String e = it.next();
                    System.out.println(e);
                }

                break;
        }
    }

    public static String otraCadena(Scanner s) {
        System.out.print("Escribe una cadena: ");
        String cadena = s.nextLine();
        return cadena;
    }
}
