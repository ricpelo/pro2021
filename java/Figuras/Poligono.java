public abstract class Poligono {
    private double[] lados;

    Poligono(double[] lados) {
        setLados(lados);
    }

    public double[] getLados() {
        return lados.clone();
    }

    private void setLados(double[] lados) {
        this.lados = lados;
    }

    public final double perimetro() {
        double suma = 0;

        for (int i = 0; i < lados.length; i++) {
            suma += lados[i];
        }

        return suma;
    }

    public abstract double area();
}
