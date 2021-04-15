class Animal {
    private int numeroPatas = 5;

    public int getNumeroPatas() {
        return this.numeroPatas;
    }

    public void setNumeroPatas(int numeroPatas) {
        this.numeroPatas = numeroPatas;
    }
}

public class Animales {
    public static void main(String[] args) {
        Animal a = new Animal();

        a.setNumeroPatas(9);
        System.out.println(a.getNumeroPatas());
    }
}
