num = 1
lista = []

while num != 0:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    
    posicao = 0
    while posicao < len(lista) and lista[posicao] < num:
        posicao += 1
        
    lista.insert(posicao, num)

print("Lista final", lista)