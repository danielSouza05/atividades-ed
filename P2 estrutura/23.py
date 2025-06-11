strVar = input("insira uma palavra: ")
strVarInv = list(strVar)
cont1 = 0
cont2 = len(strVar) - 1

while cont2 > 0:
    strVarInv[cont1] = strVar[cont2] 
    cont1 += 1
    cont2 -= 1
    
strVarInv = ''.join(strVarInv)
    
if strVarInv == strVar:
    print("palindromo")
else:
    print("não é palindromo")