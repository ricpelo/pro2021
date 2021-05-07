package fondos;

import socios.Socio;

public interface Prestable {
    default void prestar(Socio socio) {
        socio.anyadirPrestable(this);
    }
    int getPlazoPrestamo();
}
