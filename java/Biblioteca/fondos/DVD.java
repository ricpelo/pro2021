package fondos;

public class DVD extends Fondo implements Prestable {
    private int duracion;

    public DVD(TipoID ID, String denominacion, int duracion) {
        super(ID, denominacion);
        setDuracion(duracion);
    }

    public int getDuracion() {
        return duracion;
    }

    public final void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    @Override
    public int getPlazoPrestamo() {
        return 5;
    }
}
