package fondos;

public abstract class Fondo {
    private final TipoID ID;
    private String denominacion;

    public Fondo(TipoID ID, String denominacion) {
        this.ID = ID;
        setDenominacion(denominacion);
    }

    public TipoID getID() {
        return ID;
    }

    public String getDenominacion() {
        return denominacion;
    }

    public final void setDenominacion(String denominacion) {
        this.denominacion = denominacion;
    }
}
