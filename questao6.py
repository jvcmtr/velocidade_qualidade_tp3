# Primeira versão que eu fiz. FUnciona somente com numeros inteiros
def knapsack_somente_positivos(target, weights, depth=0):
    if target == 0:
        return [[]]
    if len(weights)==0:
        return[]

    array = [*weights]
    combinacoes = []

    for c in weights:
        if c > target: continue
        array.remove(c)
        combinacoes.extend([ [c, *x] for x in knapsack(target-c, array, depth+1)])

    return combinacoes


def knapsack(target, weights, depth=0):
    array = [*weights]
    combinacoes = []

    if target == 0 and depth>0:
        return [[]]
    if target == 0:
        combinacoes.append([])
    if len(weights)==0:
        return[]

    for c in weights:
        array.remove(c)
        combinacoes.extend([ [c, *x] for x in knapsack(target-c, array, depth+1)])

    return combinacoes

def test(target, weights):

    print(f"+ TESTE: quais combinações somam {target}?")
    print("    Valores : ", [*weights])
    print("    Soma    : ", target)

    result = knapsack(target, weights)
    print(f"+ Combinações encontradas: ({len(result)}):")
    
    for i in range(len(result)):
        s = [f"{x}" for x in result[i]]
        print( f"    Opção {i+1}:\t ( {' + '.join(s)} ) = {target}")
    if len(result) < 1:
        print("    nenhuma")
        
    print("_________________________________")


if __name__ == "__main__":
    test( 5, [1, 2, 3] )
    test( 5, range(6, 10) )
    test( 99, range(5) )
    test( 0, range(-1, 2) )