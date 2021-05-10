package paquete;

public class Jacinto implements Cloneable {
    public int x;

    public Jacinto(int x) {
        this.x = x;
    }

    protected void hola() {
        System.out.println("Hola");
    }

    @Override
    public Jacinto clone() throws CloneNotSupportedException {
        Jacinto j = (Jacinto) super.clone();
        j.x = x;
        return j;
    }
}
