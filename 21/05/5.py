valorFixo = int(500)
comissao = int(0.06)
valorVendas = int(input("valor em vendas: "))

total = valorFixo + (valorVendas * comissao)

print("{:.2f}" .fomart(total))