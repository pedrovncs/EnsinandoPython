# enxergando variáveis
minha_banda_favorita = "siouxsie and the banshees"
print(minha_banda_favorita)

# adicionando lógica no paramêtro
print("- ● -" * 10)

minha_musica_favorita = "sweetest chill"
print("minha música favorita:")
print(minha_musica_favorita)

print("- ● -" * 10)

ano_de_fundacao = 1976
# passagem multipla de parâmetros
print("ano de fundação:", ano_de_fundacao + 1) # data errada adicionando + 1

# string formatada
print(f"banda favorita: {minha_banda_favorita}")

a = 1
b = 666
print(f'{a} + {b} = {a + b}')

# string formatada com quebra de linha \n
print(f"ano de fundação:\n{ano_de_fundacao}\nmusica favorita:{minha_musica_favorita}")

# string formatada com quebra de linha por formatacao
print(f'''ano de fundação: {ano_de_fundacao}
      musica favorita:{minha_musica_favorita}''')

# print vazio pulando linha
print("inicio do programa")
print()
print("fim do programa")

# print tabulado com \t
print("itens:\n\t- item 1\n\t- item 2\n\t- item 3 \t- item 4")

print()

# print formatado com casas decimais
pi = 3.14159265359
print(f'Valor de pi: {pi:.4f}')
