class Componente extends Object {
    int x;
}

class Compuesto extends Object {
    private Componente co;

    public Compuesto() {
        co = new Componente();
    }

    public Componente getComponente() {
        Componente ret = new Componente();
        ret.x = co.x;
        return ret;
    }
}

public class PrincipalAgregador extends Object {
    public static void main(String[] args) {
        Compuesto ar = new Compuesto();
        Compuesto ar2 = new Compuesto();
    }
}
