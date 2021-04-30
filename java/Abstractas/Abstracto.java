abstract class ElementoGrafico {
    private double x;
    private double y;

    double getX() {
        return x;
    }

    void setX(double x) {
        this.x = x;
    }

    double getY() {
        return y;
    }

    void setY(double y) {
        this.y = y;
    }

    abstract void mover(double x, double y);
    abstract void dibujar();
}

class Ventana extends ElementoGrafico {
    private String titulo;

    Ventana(String titulo, double x, double y) {
        setTitulo(titulo);
        setX(x);
        setY(y);
    }

    String getTitulo()
    {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    @Override
    void mover(double x, double y) {
        setX(x);
        setY(y);
    }

    @Override
    void dibujar() {
        System.out.println("Me dibujo");
    }
}

class CajaDialogo extends Ventana {
    CajaDialogo(String titulo, double x, double y) {
        super(titulo, x, y);
    }

    @Override
    public void setTitulo(String s) {
        super.setTitulo("Pepito");
    }
}

public class Abstracto {
    public static void main(String[] args) {
        Ventana e = new CajaDialogo("Mi título", 4.3, 8.5);
        System.out.println(e.getTitulo());
    }
}
