def fatorialRecursiva(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * fatorialRecursiva(n - 1)


## teste fatorial recursiva
n = int(input("Digite um valor de N: "))
f = fatorialRecursiva(n)
print("Fatorial de %d eh: %d" % (n, f))