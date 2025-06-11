try:
    stringNum = input("string: ")
    intNum = int(stringNum)

    print("numero: ", intNum)

except ValueError:
    print("erro")