def main():
    numero = int(input("Digite um numero: "))
    dividendo=numero
    soma = 0
    while dividendo!=0:
        soma = soma+dividendo%10
        dividendo = dividendo//10
    print(soma)
main()