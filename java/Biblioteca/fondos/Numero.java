package fondos;

public class Numero implements TipoID {
    private int numero;

    public Numero(int numero) {
        this.numero = numero;
    }

    public int getNumero() {
        return numero;
    }

    @Override
    public Numero getValor() {
        return this;
    }
}
