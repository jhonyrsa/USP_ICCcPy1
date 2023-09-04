###
    #Soma iterada, entrada pelo usuário
###

def main():
    print("Digite uma sequencia de valores terminada por zero.")
    soma=0
    valor = 1
    while valor != 0:
        valor=float(input("Digite um valor: "))
        soma = soma + valor
    print("S = {}".format(soma))
main()