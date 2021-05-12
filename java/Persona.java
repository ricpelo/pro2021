import java.util.Objects;

public class Persona implements Cloneable {
    private static int ultimoNumero = 0;

    public int numero;
    public String nombre;

    public Persona(String nombre) {
        this.numero = ++ultimoNumero;
        this.nombre = nombre;
    }

    @Override
    public boolean equals(Object otro) {
        if (this == otro) {
            return true;
        }

        if (!(otro instanceof Persona)) {
            return false;
        }

        Persona otraPersona = (Persona) otro;

        return nombre.equals(otraPersona.nombre);
    }

    @Override
    public int hashCode() {
        return Objects.hash(nombre);
    }

    @Override
    public Persona clone() throws CloneNotSupportedException {
        Persona o = (Persona) super.clone();
        o.numero = ++ultimoNumero;
        return o;
    }
}
