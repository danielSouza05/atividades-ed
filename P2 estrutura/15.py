saldo = 20
valorSaque = int(input("valor que deseja sacar: "))

if valorSaque <= saldo:
    print("saque realizado com sucesso")
else:
    print("saldo insuficiente")