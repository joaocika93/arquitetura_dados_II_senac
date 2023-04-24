import timeit

def fib_iterativo(num):
    start_time = timeit.default_timer()
    #regras de negocio
    final_time = timeit.default_timer() - start_time
    return [num, final_time, fib]

num = int(input('Digite um numero para encontrar o seu fib: '))
num,final_time,fib_i = fib_iterativo(num)
print("Fibonacci Iterativo de %d: %d" % (num,fib_i))
print('Tempo: ' + str(final_time) + ' segundos')

