package fondos;

import socios.Socio;

public abstract class LibroGenerico extends Fondo implements Consultable {
    private String ISBN;
    private int numPaginas;

    LibroGenerico(TipoID ID, String ISBN, String denominacion, int numPaginas) {
        super(ID, denominacion);
        setISBN(ISBN);
        setDenominacion(denominacion);
    }

    public String getISBN() {
        return ISBN;
    }

    public final void setISBN(String ISBN) {
        this.ISBN = ISBN;
    }

    public int getNumPaginas() {
        return numPaginas;
    }

    public final void setNumPaginas(int numPaginas) {
        this.numPaginas = numPaginas;
    }

    @Override
    public void consultar(Socio socio) {
        String cadena = String.format(
            "El socio %d consulta el libro %s",
            socio.getNumero(),
            getISBN()
        );
        System.out.println(cadena);
    }
}
