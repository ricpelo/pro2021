class Externa {
    private static void metodoExterno() {
        System.out.println("Dentro de metodoExterno");
    }

    static class Interna {
        int x = 5;

        public void metodoInternoDeInstancia() {
            System.out.println("Dentro de metodoInternoDeInstancia");
        }

        public static void metodoInterno() {
            System.out.println("Dentro de metodoInterno");
            metodoExterno();
        }
    }
}

public class PrincipalAnidadaEstatica {
    public static void main(String[] args) {
        Externa.Interna in = new Externa.Interna();
        System.out.println(in.x);
        Externa.Interna.metodoInterno();
        in.metodoInternoDeInstancia();
    }
}
