package fondos;

public class Fondo {
    private final TipoID ID;
    private String denominacion;

    Fondo(String denominacion) {
        this.ID = new TipoID();
        this.denominacion = denominacion;
    }

    public TipoID getID() {
        return ID;
    }
}
