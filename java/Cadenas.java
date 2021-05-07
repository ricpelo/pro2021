public class Cadenas {
    public static void main(String[] args) {
        String s = "Hola";
        StringBuffer sbf = new StringBuffer("hola");
        StringBuilder sbl = new StringBuilder("hola");
        System.out.println(longitud(s));
        System.out.println(longitud(sbf));
        System.out.println(longitud(sbl));
    }

    public static int longitud(CharSequence cadena) {
        return cadena.length();
    }
}
