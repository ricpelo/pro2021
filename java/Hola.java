import java.util.Scanner;

/*
 * Mostrar por la salida todos los números que encuentre por la entrada,
 * desechando lo que no sean números.
 */
public class Hola {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero;

        System.out.print("Números: ");

        while (sc.hasNextInt()) {
            numero = sc.nextInt();
            String numeroCadena = String.valueOf(numero) + " x "; // 3
            StringBuilder sb = new StringBuilder();     // 1

            for (int i = 0; i <= 10; i++) {
                sb.append(numeroCadena);
                sb.append(String.valueOf(i));           // 1
                sb.append(" = ");                       // 1 (0)
                sb.append(String.valueOf(numero * i));  // 1
                System.out.println(sb);                 // 1
                sb.delete(0, sb.length());
            }
        }
    }
}
