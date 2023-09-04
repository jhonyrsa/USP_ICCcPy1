import math
numero = int(input("Digite um numero inteiro: "))
i = 2
primo = True
while i<=math.sqrt(numero):
    if (numero%i==0):
        primo=False
        break
    i+=1
if primo and numero>1:
    print("primo")
else:
    print("não primo")