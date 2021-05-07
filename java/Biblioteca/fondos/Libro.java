package fondos;

public class Libro extends LibroGenerico implements Prestable {
    public Libro(TipoID ID, String ISBN, String denominacion, int numPaginas) {
        super(ID, ISBN, denominacion, numPaginas);
    }

    @Override
    public int getPlazoPrestamo() {
        return 20;
    }
}
