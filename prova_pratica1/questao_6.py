def soma(num1, num2):
    resultado = num1+num2
    return resultado

def subtracao(num1, num2):
    resultado = num1-num2
    return resultado

def multiplicacao(num1, num2):
    resultado = num1*num2
    return resultado

def divisao(num1, num2):
    resultado = num1/num2
    return resultado

if __name__ == '__main__':
    n1=int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print("1: +\n 2: -\n 3: x\n 4: /")
    operador = int(input("Digite o número correspondente à operação que deseja realizar: "))
    if operador == 1:
        resultado_soma = soma(n1, n2)
        print("A soma de {} com {} é igual: {}".format(n1,n2,resultado_soma))
    elif operador == 2:
        resultado_sub = subtracao(n1, n2)
        print("A subtração de {} com {} é igual: {}".format(n1,n2,resultado_sub))
    elif operador == 3:
        resultado_mult = multiplicacao(n1, n2)
        print("A multiplicação de {} com {} é igual: {}".format(n1,n2,resultado_mult))
    elif operador == 4:
        resultado_div = divisao(n1, n2)
        print("A divisão de {} com {} é igual: {}".format(n1,n2,resultado_div))
    else:
        print("Favor digitar um valor válido!")