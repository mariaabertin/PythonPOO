numero=0
for soma in range (1, 501, 1):
    if soma%2 != 0 and soma%3 ==0:
        numero+=soma
print("A soma de todos os numeros que são ao mesmo tempo ímpar e múltiplo de três no intervalo de 1 a 500 é: {}".format(numero))