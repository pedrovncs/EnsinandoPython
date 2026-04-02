# dicionário com os quadrados dos números

# usando loop
quadrados_loop = {}
for x in range(6):
    quadrados_loop[x] = x**2
print(f"com loop: {quadrados_loop}")

# comprehension
quadrados_comprehension = {x: x**2 for x in range(6)}
print(f"com comprehension: {quadrados_comprehension}")

print("--"*20)

# filtrando dicionario já existente, apenas alunos com nota na media ou acima

# loop 
alunos_notas = {"Ana": 8, "João": 5, "Maria": 9, "Pedro": 6, "Lucas": 7}
aprovados_loop = {}
media = 7

for aluno, nota in alunos_notas.items():
    if nota >= media:
        aprovados_loop[aluno] = nota
print(f"com loop: {aprovados_loop}")

# comprehension
aprovados_comprehension = {aluno: nota for aluno, nota in alunos_notas.items() if nota >= media}
print(f"com comprehension: {aprovados_comprehension}")

print("--"*20)

# criando dicionário com o tamanho das palavras

# com loop
palavras = ["paralelepipedo", "abacaxi", "aeronave", "velocidade", "computador"]
tamanho_palavras_loop = {}
for palavra in palavras:
    tamanho_palavras_loop[palavra] = len(palavra)
print(f"com loop: {tamanho_palavras_loop}")

# comprehension
tamanho_palavras_comprehension = {palavra: len(palavra) for palavra in palavras}
print(f"com comprehension: {tamanho_palavras_comprehension}")
