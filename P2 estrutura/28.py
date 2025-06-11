tupla1 = (20, 40, 50)
tupla2 = ("daniel", "edu", "miguel")

maior = max(tupla1)

cont = 0
while cont < len(tupla1):
    if maior == tupla1[cont]:
        print(tupla2[cont])
    cont += 1