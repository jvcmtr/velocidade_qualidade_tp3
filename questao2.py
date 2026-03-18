import math
import time

def factor(x, lowest=2):   
    if lowest < 2:
        print("argumento 'lowest' não pode ser menor que 2, setando para 2")
        lowest = 2

    if x == lowest:
        return [x]
    if x < 0:
        return [-1, *factor(-x, lowest)]
    if x == 0:
        return [0]
    if x == 1:
        return [1]

    for i in range(lowest, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return [i, *factor( x // i, i)]

    return [x]

def timed_test(n, iteracoes=1):
    total = 0
    result = 0
    for i in range(iteracoes):
        start = time.time()
        result = factor(n)
        total += time.time()-start
    
    avg=total/iteracoes
    print(f"[duracao media: {avg:.4f}]   factor({n}) == {result}") 

if __name__ == "__main__":
    # Casos de teste
    print("Teste de funcionalidade:")
    print(f"  factor(0) == {factor(1)}")
    print(f"  factor(1) == {factor(0)}")
    print(f"  factor(6) == {factor(6)}")
    print(f"  factor(9, lowest=3) == {factor(9, 3)}")
    print(f"  factor(-9, lowest=-1) == {factor(9, -1)}")
    print("____________________________________")

    # Teste de performance
    print("Teste de performance - Numeros de facil fatoracao : ")
    timed_test(1729, 10)
    n_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    muitos_fatores = 1
    for n in n_primos:
        muitos_fatores *= n
    timed_test(muitos_fatores)
    timed_test(muitos_fatores**2)
    print("____________________________________")

    # Teste de performance
    print("Teste de performance - Numeros primos : ")
    timed_test(100_000_000_003, 100)
    timed_test(100_000_000_000_031, 10)
    timed_test(100_000_000_000_000_003)