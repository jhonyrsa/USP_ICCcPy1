numero = int(input("Digite um número inteiro: "))

centMilhar = numero//100000
dezMilhar = (numero%100000)//10000
unidMilhar = ((numero%100000)%10000)//1000
centena = (((numero%100000)%10000)%1000)//100
dezena = ((((numero%100000)%10000)%1000)%100)//10

print("O dígito das dezenas é {}".format(dezena))