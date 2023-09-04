def main():
    meuCartao = int(input("Digite o numero do seu cartão: "))
    encontreiCartao = False
    cartoesEncontrados = 1
    while cartoesEncontrados!=0 and not encontreiCartao:
        cartoesEncontrados = int(input("Digite o cartao encontrado: "))
        if(cartoesEncontrados==meuCartao):
            encontreiCartao = True
    if encontreiCartao:
        print("Encontrei meu cartao perdido.")
    else:
        print("Não encontrei meu cartão.")
main()