ct=0
ctvinte=0
soma=0
n=0
print("Digite -1 para parar a contagem")

while True:
   n= float(input("Digite o numero: "))
   if n ==-1:
       break
   else:
       soma= soma+n
       ct+=1
       if n>20:
           ctvinte+=1
media=soma/ct
print("Você digitou {} números".format(ct))
print("A soma dos números digitados é: {}".format(soma))
print("A média dos números digitados é: {}".format(media))
print("A quantidade de números digitados maior que 20 é: {}".format(ctvinte))