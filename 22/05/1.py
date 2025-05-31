texto = input("frase com pelo menos 1 numero: ")

tem_numero = False

for char in texto:
    if char.isdigit():
        tem_numero = True
        break

if tem_numero:
    print("tem número")
else:
    print("não tem número")
