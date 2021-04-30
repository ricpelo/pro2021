public class Rectangulo extends Poligono {

    Rectangulo(double ancho, double alto) {
        super(new double[] { ancho, alto, ancho, alto });
    }

    public double ancho() {
        return getLados()[0];
    }

    public double alto() {
        return getLados()[1];
    }

    @Override
    public double area() {
        return ancho() * alto();
    }
}
