public class Racional {
    private int numer;
    private int denom;
    public static int cantidad;

    private void setNumer(int numer) {
        this.numer = numer;
    }

    private void setDenom(int denom) {
        this.denom = denom;
    }

    private void simplificar() {
        int mcd = Matematicas.mcd(getNumer(), getDenom());
        setNumer(getNumer() / mcd);
        setDenom(getDenom() / mcd);
    }

    public Racional(int numer, int denom) {
        setNumer(numer);
        setDenom(denom);
        simplificar();
        cantidad++;
    }

    public Racional(int numer) {
        setNumer(numer);
        setDenom(1);
        cantidad++;
    }

    public int getNumer() {
        return numer;
    }

    public int getDenom() {
        return denom;
    }

    public void imprimir() {
        System.out.println(String.format("%d / %d", numer, denom));
    }

    public void imprimir(String prefijo) {
        System.out.print(prefijo);
        imprimir();
    }
}
