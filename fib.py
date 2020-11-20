n = int(input('Escribe el número: '))

"""
fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
...
"""

if n == 0:
    a = 0
elif n == 1:
    a = 1
else:
    a = 0 # fib(0)
    b = 1 # fib(1)
    while a < n - 1:          # a = fib(n), b = fib(n + 1)
        a, b = b, a + b

print(a)

"""
       a b
     a b

   0 1 2 3 4 5 6 7  8
   0 1 1 2 3 5 8 13 21...
"""

fib = lambda n: fib_iter(n, 0, 1)
fib_iter = lambda c, a, b: a if c == 0 else \
                           fib_iter(c - 1, b, a + b)

c = n
a = 0
b = 1

while c > 0:
    c, a, b = c - 1, b, a + b

print(a)
