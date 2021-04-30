public class Principal {
    public static void main(String[] args) {
        Circunferencia p = new Circunferencia(4.0);
        p.getLados()[0] = 9.0;
        System.out.println(p.perimetro());
    }

    public static double dobleArea(Circunferencia p) {
        return 2.0 * p.area();
    }
}
