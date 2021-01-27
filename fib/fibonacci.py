def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1:
        print(fib(int(argv[1])))
    else:
        if fib(8) == 21:
            print('fib(8) vale 21 (correcto)')
        else:
            print('fib(8) vale', fib(8), '(incorrecto)')
