class Base {
    public void hola() {
        System.out.println(this.nombre());
    }

    public String nombre() {
        return "Base";
    }

    public long numero() {
        return 24L;
    }
}

class Derivada extends Base {
    @Override
    public String nombre() {
        return "Derivada";
    }

    @Override
    public int numero() {
        return 24;
    }
}

public class Principal {
    public static void main(String[] args) {
        Base b = new Derivada();
        b.hola();
    }
}


/**
 *
 * Integer[] != Number[]
 *
 * si Integer <: Number, entonces Integer[] <: Number[]
 *
 * si A <: B, entonces A[] <: B[]
 *
 *
 */
