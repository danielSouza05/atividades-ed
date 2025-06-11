def aplicar_funcao_lista(lista, funcao):
    return [funcao(item) for item in lista]

def dobrar(x):
    return x * 2

minha_lista = [1, 2, 3, 4]

resultado = aplicar_funcao_lista(minha_lista, dobrar)

print(resultado)