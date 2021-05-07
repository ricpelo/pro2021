package fondos;

public class Codigo implements TipoID {
    private String codigo;

    public Codigo(String codigo) {
        this.codigo = codigo;
    }

    public String getCodigo() {
        return codigo;
    }

    @Override
    public Codigo getValor() {
        return this;
    }
}
