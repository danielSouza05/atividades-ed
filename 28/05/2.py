N = int(input("termos: "))

if N >= 2:
    lista = [0, 1]
    
    for i in range(2, N):
        proximo = lista[i-1] + lista[i - 2]
        lista.append(proximo)
    print("lista: ", lista)
    
else:
    print("digite um numero maior que 2")