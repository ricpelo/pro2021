public class Circunferencia extends Poligono {

    Circunferencia(double perimetro) {
        super(new double[] { perimetro });
    }

    @Override
    public double area() {
        return Math.PI * Math.pow(radio(), 2.0);
    }

    public double diametro() {
        return 2.0 * radio();
    }

    public double circunferencia() {
        return perimetro();
    }

    private double radio() {
        return getLados()[0] / (2.0 * Math.PI);
    }
}
