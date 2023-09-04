nomeCliente = input("Digite o nome do cliente: ")
diaVencimento = input("Digite o dia de vencimento: ")
mesVencimento = input("Digite o mês de vencimento: ")
valorFatura = input("Dia o valor da fatura: ")

print("Olá, {}".format(nomeCliente))
print("A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(diaVencimento,mesVencimento,valorFatura))