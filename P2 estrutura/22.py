letra = input("insira uma letra: ")
strVar = "string pika"
cont = 0

while cont < len(strVar):
    if strVar[cont] == letra:
        contador += 1
    cont += 1

print(contador)