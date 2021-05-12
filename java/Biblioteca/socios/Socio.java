package socios;

import java.util.ArrayList;
import java.util.List;
import fondos.Prestable;

public class Socio {
    private long numero;
    private String nombre;
    private List<Prestable> fondos;

    public Socio(long numero, String nombre) {
        setNumero(numero);
        setNombre(nombre);
        fondos = new ArrayList<Prestable>();
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

    public void anyadirPrestable(Prestable p) {
        fondos.add(p);
    }
}
