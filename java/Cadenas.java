public class Cadenas {
    public static void main(String[] args) {
        Object[] ob = new Object[] {
            5,
            "hola",
            true,
            null,
            new StringBuilder("pepe")
        };

        muestraLongitud(ob);
    }

    public static int longitud(CharSequence cadena) {
        return cadena.length();
    }

    public static void muestraLongitud(Object[] obj) {
        for (Object o : obj) {
            if (o instanceof CharSequence) {
                System.out.println(((CharSequence) o).length());
            }
        }
    }
}
