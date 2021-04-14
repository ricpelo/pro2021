public class Prueba {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Error: debe indicar el número.");
            return;
        } else if (args.length > 1) {
            System.err.println("Error: se han indicado demasiados argumentos.");
            return;
        }

        try {
            int num = Integer.parseInt(args[0]);

            if (num < 0 || num > 10) {
                System.err.println("El número debe estar comprendido entre 0 y 10.");
                return;
            }

            for (int i = 0; i <= 10; i++) {
                System.out.println(String.format("%d x %d = %d", num, i, num * i));
            }
        } catch (NumberFormatException e) {
            System.err.println("El número pasado no es correcto.");
        }
    }
}
