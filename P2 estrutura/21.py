try:
    arquivo = open("meuarquivo.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)

except FileNotFoundError:
    print("Erro! O arquivo não foi encontrado.")

finally:
    if 'arquivo' in locals():
        arquivo.close()
