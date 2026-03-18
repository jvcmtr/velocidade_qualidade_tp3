
def mult_base(x, y):
    if y == 0:
        return 0
    if(y < 0):
        y = -y
        return -x - mult(x, y-1)
    return x + mult(x, y-1)


def mult(x, y, depth=0):
    print(("│   "*depth) + f"┌ Calculando {x} * {y}")

    if y == 0:
        print(("│   "*depth) + f"└ Retornando: 0")
        return 0

    if(y < 0):
        y = -y
        print(("│   "*depth) + f"│ Chamando recursão: {x} * -{y} = -{x} - ({x} * {y-1})")
        som = mult(x, y-1, depth+1)
        result = -x - som

        print(("│   "*depth) + f"└ Retornando: {result}")
        return result
 
    print(("│   "*depth) + f"│ Chamando recursão: {x} * {y} = {x} + ({x} * {y-1})")
    som = mult(x, y-1, depth+1)
    result = x + som
    print(("│   "*depth) + f"└ Retornando: {result}")
    return result


if __name__ == "__main__":
    print("Teste 2 x 3 - Registro de chamadas")
    print(f"Valor retornado da função: {mult(2, -3)}")

    # Casos de teste
    # print(f"mult(1, 0) = {mult_base(1, 0)}")
    # print(f"mult(0, 1) = {mult_base(0, 1)}")
    # print(f"mult(1, 2) = {mult_base(1, 2)}")
    # print(f"mult(2, 3) = {mult_base(2, 3)}")
    # print(f"mult(2, -3) = {mult_base(2, -3)}")
    # print(f"mult(-2, -3) = {mult_base(-2, -3)}")
    # print(f"mult(-2, 3) = {mult_base(-2, 3)}")