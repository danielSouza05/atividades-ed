a = int(input("lado a:"))
b = int(input("lado b:"))
c = int(input("lado c:"))

if a == b == c:
    print("Equilátero (3 lados iguais)")
elif a == b or a == c or b == c:
    print("Isósceles (2 lados iguais)")
else:
    print("Escaleno (todos lados diferentes)")