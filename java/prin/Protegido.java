package prin;

import paquete.Jacinto;
import paquete.Manolo;

public class Protegido {
    public static void main(String[] args) {
        Jacinto p = new Jacinto(4);
        Jacinto j = p.clone();
    }
}
