def soma (num1, num2, num3):
    resultado = num1+num2+num3
    return resultado

if __name__ == '__main__':
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    n3 = int(input("Digite o terceiro numero: "))

    resultado_soma = soma(n1, n2, n3)
    print("A soma dos três numeros é: {}".format(resultado_soma))