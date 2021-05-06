package fondos;

import socios.Socio;

public interface Prestable {
    void prestar(Socio socio);
    int getPlazoPrestamo();
}
