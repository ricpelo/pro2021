public class Racional {
    private double numer;
    private double denom;

    public Racional(double numer, double denom) {
        setNumer(numer);
        setDenom(denom);
    }

    public Racional(double numer) {
        setNumer(numer);
        setDenom(1.0);
    }

    public Racional() {

    }

    public double getNumer() {
        return numer;
    }

    public double getDenom() {
        return denom;
    }

    public void setNumer(double numer) {
        this.numer = numer;
    }

    public void setDenom(double denom) {
        this.denom = denom;
    }

    public void imprimir() {
        System.out.println(String.format("%.2f / %.2f", numer, denom));
    }

    public void imprimir(String prefijo) {
        System.out.print(prefijo);
        imprimir();
    }

    public void imprimir(boolean logico) {
        System.out.println(logico);
    }
}
