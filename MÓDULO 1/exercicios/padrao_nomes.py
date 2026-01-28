"""
crie um programa que recebe um nome como entrada do usuário. seu 
código deve exibir o nome corretamente formatado no terminal, 
removendo espaços em branco, letras incorretamente maiúsculas ou 
minúsculas, etc.
exemplos de entrada:
● joÃO  SILVA!
●    pEDRO paiva 

""" 

nome = input( "FALA TEU NOME: ")
print(nome.split())

nome_formatado = nome.lower().title().strip()

nome_final = "-".join(nome_formatado.split())
print(nome_final)

