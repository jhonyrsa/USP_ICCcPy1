def main():
    decrescente = True #Indicador de passagem é uma variável do tipo booleana
    valor = int(input("Digite o início da sequencia: "))
    anterior = valor
    while valor!=0 and decrescente:
        valor = int(input("Digite um valor da sequência: "))
        if(valor>anterior):
            decrescente = False
        anterior = valor
    if decrescente:
        print("A sequência está em ordem DECRESCENTE.")
    else:
        print("A sequência NÃO está em ordem DECRESCENTE.")    
main()