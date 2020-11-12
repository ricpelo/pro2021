<expresión>
=> <operación>
=> ( <expr> <op_bin> <expr> )
=> ( <literal> <op_bin> <expr> )
=> ( entero <op_bin> <expr> )
=> ( 3 <op_bin> <expr> )
=> ( 3 + <expr> )
=> ( 3 + <literal> )
=> ( 3 + <entero> )
=> ( 3 + 5 )







(3 * (4 + 5))          # evalúo 3 y devuelve 3
= (3 * (4 + 5))        # evalúo 4 y devuelve 4
= (3 * (4 + 5))        # evalúo 5 y devuelve 5
= (3 * (4 + 5))        # evalúo (4 + 5) y devuelve 9
= (3 * 9)              # evalúo (3 * 9) y devuelve 27
= 27

((3 * (4 + 5)) - 10)   # evalúo 3 y devuelve 3
= ((3 * (4 + 5)) - 10) # evalúo 4 y devuelve 4
= ((3 * (4 + 5)) - 10) # evalúo 5 y devuelve 5
= ((3 * (4 + 5)) - 10) # evalúo 10 y devuelve 10
= ((3 * (4 + 5)) - 10) # evalúo (4 + 5) y devuelve 9
= ((3 * 9) - 10)       # evalúo (3 * 9) y devuelve 27
= (27 - 10)            # evalúo (27 - 10) y devuelve 17
= 17
