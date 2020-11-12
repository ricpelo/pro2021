not (True and (not False or 4 < 2))     # evalúa True y devuelve True
= not (True and (not False or 4 < 2))   # evalúa False y devuelve False
= not (True and (not False or 4 < 2))   # evalúa not False y devuelve True
= not (True and (True or 4 < 2))        # evalúa 4 y devuelve 4
= not (True and (True or 4 < 2))        # evalúa 2 y devuelve 2
= not (True and (True or 4 < 2))        # evalúa 4 < 2 y devuelve False
= not (True and (True or False))        # evalúa (True or False) y devuelve True
= not (True and True)                   # evalúa (True and True) y devuelve True
= not True                              # evalúa not True y devuelve False
= False


25 if 3 > 2 else 17                     # evalúa 3 y devuelve 3
= 25 if 3 > 2 else 17                   # evalúa 2 y devuelve 2
= 25 if 3 > 2 else 17                   # evalúa 3 > 2 y devuelve True
= 25 if 3 > 2 else 17                   # evalúa 25 y devuelve 25
= 25

(x if c1 else y) if c2 else z



maximo(3, 4)               # evalúa maximo y devuelve la función que calcula el máximo de 2
= maximo(3, 4)      
