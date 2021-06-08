def Fibonacci(n):
    print('-'*30)
    print('Fibonnaci')
    print('-'*30)
    n = int(input('Digite os termos: '))
    t1 = 0
    t2 = 1
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(f' - {t3}', end='')
        t1 = t2 
        t2 = t3
        cont += 1

n1 = int(input)

Fibonacci(n1)