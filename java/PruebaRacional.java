public class PruebaRacional {
    public static void main(String[] args) {
        Racional r = new Racional(6, 4);

        for (int i = 0; i < 10; i++) {
            new Racional(2, 1);
        }

        System.out.println(Racional.cantidad);
        r.imprimir();
    }
}

/*
 * Constructor sin parámetros (además de otros posibles con parámetros):
 * - Tiene que haber setters para numerador y denominador
 * - El objeto es mutable
 *
 * Constructores con parámetros (no hay constructor sin parámetros):
 * - No habría necesidad de setters
 * - El objeto es inmutable
 */
