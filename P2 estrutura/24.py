letra2 = input("insira uma letra: ")
letra1 = input("insira a letra a ser substituida: ")
strVar = "string pika"
strVarList = list(strVar)
cont = 0

while cont < len(strVar):
    if strVar[cont] == letra1:
        strVarList[cont] = letra2
    cont += 1

strVarList = ''.join(strVarList)

print(strVarList)