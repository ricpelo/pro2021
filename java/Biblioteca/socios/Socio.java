package socios;
import fondos.Prestable;

public class Socio {
    private long numero;
    private String nombre;
    public Prestable[] fondos;

    Socio(long numero, String nombre) {
        setNumero(numero);
        setNombre(nombre);
    }

    public long getNumero() {
        return numero;
    }

    public final void setNumero(long numero) {
        this.numero = numero;
    }

    public String getNombre() {
        return nombre;
    }

    public final void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
