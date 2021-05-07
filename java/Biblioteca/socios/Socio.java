package socios;
import fondos.Prestable;

public class Socio {
    private final int MAX_PRESTABLES = 100;

    private long numero;
    private String nombre;
    private Prestable[] fondos;
    private int numPrestables = 0;

    public Socio(long numero, String nombre) {
        setNumero(numero);
        setNombre(nombre);
        fondos = new Prestable[MAX_PRESTABLES];
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
        if (numPrestables < MAX_PRESTABLES) {
            fondos[numPrestables++] = p;
        }
    }
}
