try:
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    
    resultado = num1 / num2
    
    print(f"resultado: {resultado}")

except ZeroDivisionError:
    print("não pode dividir por 0")
