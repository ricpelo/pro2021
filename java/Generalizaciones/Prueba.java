class Base {
    public int x;                       // Esta es una variable...

    public Object noHaceNada(String o) {
        return o;
    }

}

class Derivada extends Base {
    protected String x;                 // ... y esta es otra distinta

    public String getX() {
        return x;                       // Accede a la «x» de Derivada
    }

    @Override
    public String noHaceNada(Object o) {
        return "hola";
    }
}

public class Prueba {
    public static void main(String[] args) {
        Base b = new Base();
        Derivada d = new Derivada();
        Base bd = new Derivada();
        b.x = 4;                        // Accede a la «x» de Base
        d.x = "Hola";                   // Accede a la «x» de Derivada
        bd.x = 5;                       // Accede a la «x» de Base
        System.out.println(d.getX());   // Imprime «Hola»
    }
}
