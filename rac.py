"""
Implementación del TAD rac (números racionales).
"""

from math import gcd

def racional(n, d):
    """Generadora del TAD rac."""
    if d == 0:
        raise ValueError('El denominador no puede ser cero.')
    r = {'n': n, 'd': d}
    _simplificar(r)
    return r

def numer(r):
    """Selectora del numerador del TAD rac."""
    return r['n']

def denom(r):
    """Selectora del denominador del TAD rac."""
    return r['d']

def set_numer(r, n):
    """Mutadora que cambia el numerador del racional r."""
    r['n'] = n
    _simplificar(r)

def set_denom(r, d):
    """Mutadora que cambia el denominador del racional r."""
    r['d'] = d
    _simplificar(r)

def _simplificar(r):
    """Mutadora que simplifica el racional r."""
    g = gcd(r['n'], r['d'])
    r['n'], r['d'] = r['n'] // g, r['d'] // g

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
