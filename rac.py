"""
Implementación del TAD rac (números racionales).
"""

from math import gcd
from pareja import *

def racional(n, d):
    """Generadora del TAD rac."""
    if d == 0:
        raise ValueError('El denominador no puede ser cero.')
    r = pareja(n, d)
    _simplificar(r)
    return r

def numer(r):
    """Selectora del numerador del TAD rac."""
    return select(r, 0)

def denom(r):
    """Selectora del denominador del TAD rac."""
    return select(r, 1)

def set_numer(r, n):
    """Mutadora que cambia el numerador del racional r."""
    set_pareja(r, 0, n)
    _simplificar(r)

def set_denom(r, d):
    """Mutadora que cambia el denominador del racional r."""
    set_pareja(r, 1, d)
    _simplificar(r)

def _simplificar(r):
    """Mutadora que simplifica el racional r."""
    g = gcd(select(r, 0), select(r, 1))
    set_pareja(r, 0, select(r, 0) // g)
    set_pareja(r, 1, select(r, 1) // g)

# A partir de aquí, las funciones no tienen por qué saber cómo están
# representados los datos abstractos (los racionales):

def mult_rac(r1, r2):
    return racional(numer(r1) * numer(r2), denom(r1) * denom(r2))

def suma_rac(r1, r2):
    return racional(numer(r1) * denom(r2) + numer(r2) * denom(r1),
                    denom(r1) * denom(r2))

def imprimir(r):
    print(numer(r), '/', denom(r))

def iguales(r1, r2):
    return numer(r1) * denom(r2) == numer(r2) * denom(r1)
