class Animal {
    int numeroPatas;

    public int getNumeroPatas() {
        System.out.println(nombre());
        return numeroPatas;
    }

    public String nombre() {
        return "Animal";
    }

    protected void mover(String w) {
        System.out.println("Me estoy moviendo hacia el " + w);
    }
}

class Gato extends Animal {
    String numeroPatas;

    @Override
    public String nombre() {
        return "Gato";
    }

    @Override
    protected void mover(String s) {
        System.out.println("Me muevo como un gato hacia el " + s);
    }

    public void maullar() {
        System.out.println("Miauuuuuuuu");
    }
}

class Perro extends Animal {
    public void ladrar() {
        System.out.println("Guauuuuuuu");
    }

    @Override
    protected void mover(String s) {
        System.out.println("Me voy saltando y brincando hacia el " + s);
    }
}

public class BaseDerivada {
    public static void main(String[] args) {
        Animal m = new Gato();
        Gato a = new Gato();
        m.nombre();
        System.out.println(a.getNumeroPatas());
    }
}
