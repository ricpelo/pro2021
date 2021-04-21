class Coche {
    private class Motor {
        int cilindros;
    }

    private class Rueda {
        int diametro;
    }

    private Motor motor;
    private Rueda[] ruedas;

    Coche() {
        motor = new Motor();
        ruedas = new Rueda[4];

        for (int i = 0; i < ruedas.length; i++) {
            ruedas[i] = new Rueda();
        }
    }
}

public class PrincipalCoche {
    public static void main(String[] args) {
        // Externa.Interna in = new Externa().new Interna();
        // in.imprimir();
        Coche c = new Coche();
        System.out.println(c.motor.cilindros);
    }
}
