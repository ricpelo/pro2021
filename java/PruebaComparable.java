interface Comparable {
    int compararCon(Comparable otro);
}

interface Sumable {
    Sumable sumar(Sumable otro);
}

interface ComparableYSumable extends Comparable, Sumable {

}

class Cadena implements Comparable {
    private String cadena;

    Cadena(String cadena) {
        setCadena(cadena);
    }

    public String getCadena() {
        return cadena;
    }

    public final void setCadena(String cadena) {
        this.cadena = cadena;
    }

    @Override
    public int compararCon(Comparable otro) {
        Cadena otraCadena = (Cadena) otro;

        if (getCadena().compareTo(otraCadena.getCadena()) < 0) {
            return -1;
        } else if (getCadena().compareTo(otraCadena.getCadena()) == 0) {
            return 0;
        } else {
            return 1;
        }
    }
}

class Entero implements ComparableYSumable {
    private int numero;

    Entero(int numero) {
        setNumero(numero);
    }

    public int getNumero() {
        return numero;
    }

    public final void setNumero(int numero) {
        this.numero = numero;
    }

    @Override
    public int compararCon(Comparable otro) {
        Entero otroEntero = (Entero) otro;

        if (getNumero() < otroEntero.getNumero()) {
            return -1;
        } else if (getNumero() == otroEntero.getNumero()) {
            return 0;
        } else {
            return 1;
        }
    }

    @Override
    public Sumable sumar(Sumable otro) {
        Entero otroEntero = (Entero) otro;
        return new Entero(this.getNumero() + otroEntero.getNumero());
    }
}

class Largo extends Entero {
    Largo(int i) {
        super(i);
    }
}

public class PruebaComparable {
    static int posicion = -1;
    static Comparable[] objetos = new Comparable[10];

    public static void main(String[] args) {
        Comparable c1 = new Entero(4);
        Comparable c2 = new Entero(9);

        Comparable c3 = new Cadena("hola");
        Comparable c4 = new Cadena("pepito");

        Sumable s1 = new Entero(5);
        Sumable s2 = new Entero(7);

        meter(c1);
        meter(c3);
    }

    public static void meter(Comparable c) {
        objetos[++posicion] = c;
    }
}
