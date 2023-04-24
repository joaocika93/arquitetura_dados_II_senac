def fatorial_SemRecursao(n):
    fat = 1
    while( n > 1):
        fat *= n
        n -= 1
    return fat

## teste fatorial sem recursão
n = int(input("Digite um valor de N: "))
f = fatorial_SemRecursao(n)
print("Fatorial de %d eh: %d" % (n, f))