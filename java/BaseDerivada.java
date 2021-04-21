class Base {
    protected void imprimir() {
        System.out.println("Hola");
    }

}

class Derivada extends Base {   // Derivada <1 Base
    public void imprimirDesdeDerivada() {
        System.out.println("Hola desde Derivada");
    }
}

public class BaseDerivada {
    public static void main(String[] args) {
        Base b = new Derivada();
        ((Derivada) b).imprimirDesdeDerivada();
    }
}
