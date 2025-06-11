n = int(input("Insira n: "))
lista = []

for num in range(0, n):
    if num % 2 == 0:
        lista.append(num)

print(lista)