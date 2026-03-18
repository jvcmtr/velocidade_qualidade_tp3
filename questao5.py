
def teams(candidates, k):
    if k == 1:
        return [[x] for x in candidates]

    array = [*candidates]
    combinacoes = []
    for c in candidates:
        array.remove(c) 
        combinacoes.extend([ [c, *x] for x in teams(array, k-1)])

    return combinacoes


def test(n_candidatos, k):
    todos = ["Alice", "Beatriz", "Caio", "Davi", "Ernesto", "Fernanda", "Geraldo", "Heitor", "Igor", "Joao", "Kelly", "Luiz", "Marcus", "Nicole", "Otavio", "Pedro", "Queiroz", "Rafaela", "Silvio", "Tatiana", "Ulisses", "Viviane", "Welington", "Xavier", "Ziraldo"]
    candidatos = [*todos[:n_candidatos]]

    print(f"+ TESTE: escolha {k} dentre {n_candidatos} candidatos")
    print(f"+ Grupo de candidatos ({len(candidatos)}):")
    print("   " + ", ".join(candidatos))
    print(f"+ Possiveis combinações de grupos com {k} integrantes")

    # Padroniza espaçamento dos nomes
    COL_SIZE= 10
    for i in range(len(candidatos)):
        candidatos[i] =  candidatos[i] +"," + (" "*(COL_SIZE - len(candidatos[i])))

    result = teams(candidatos, k)
    for i in range(len(result)):
        print( f"   Opção {i+1}:\t{''.join(result[i]).strip().strip(",")}.")
    print("_________________________________")


if __name__ == "__main__":
    test(3, 2)
    test(5, 3)
    test(10, 9)