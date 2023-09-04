def main():
    numero = int(input("Digite um número: "))
    novoNumero = numero
    soma = 0
    while novoNumero%10!=0 and novoNumero!=0:
        soma = soma+(novoNumero%10)
        novoNumero=novoNumero//10
    print("A soma dos algarismos de {} é {}.".format(numero, soma))
main()