def valor_absoluto(num):
    if num <0:
        num=num*-1
    return num

if __name__ == '__main__':
    numero=int(input("Digite o número: "))
    modulo = valor_absoluto(numero)
    print("O módulo de {} é: {}".format(numero, modulo))