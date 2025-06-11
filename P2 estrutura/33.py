def potencias_de_2(expoente_maximo):
    lista_potencias = []
    
    for i in range(expoente_maximo + 1): 
        lista_potencias.append(2 ** i) 
    
    return lista_potencias

expoente_maximo = int(input("expoente: "))

resultado = potencias_de_2(expoente_maximo)
print(f"resultado: {resultado}")
