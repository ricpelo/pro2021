import java.util.Objects;

abstract class Animal {
    public String nombre = "Animal";
    public String raza;
    public int edad;

    protected void mover(String w) {
        System.out.println("Me estoy moviendo hacia el " + w);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if (obj == null) {
            return false;
        }

        if (getClass() != obj.getClass()) {
            return false;
        }

        Animal animal = (Animal) obj;
        return edad == animal.edad && Objects.equals(raza, animal.raza);
    }

    @Override
    public int hashCode() {
        return Objects.hash(raza, edad);
    }
}

class Gato extends Animal {
    public String nombre = "Gato";

    @Override
    protected void mover(String s) {
        System.out.println("Me muevo como un gato hacia el " + s);
    }

    public void maullar() {
        System.out.println("Miauuuuuuuu");
    }
}

class Perro extends Animal {
    public String nombre = "Perro";

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
        Gato a = new Gato();
        Gato b = new Gato();
        a.edad = 5;
        a.raza = "Persa";
        b.edad = 5;
        b.raza = "Persa";
        System.out.println(a.equals(b));
        System.out.println(a.hashCode());
        System.out.println(b.hashCode());
    }
}
