# lista 
paises_brics = ["Brasil", "Rússia", "India", "China", "África do Sul"]

print("Brasil" in paises_brics)
print("Estados Unidos" in paises_brics)

# tupla
mega_da_virada_2025 = (59,21,32,13,9,33)

print(59 in mega_da_virada_2025)
print(9 in mega_da_virada_2025)

# dicionario
charmander = {"nome": "Charmander", "tipo": "fogo", "nivel": 5}

print("nome" in charmander) # encontra a chave

print("Charmander" in charmander) # nao encontra pois nao e chave
print(charmander.values())
print("Charmander" in charmander.values()) # encontra pois o retorno de .values() é uma "lista"

#lista de dicionarios
pokemons = [
    {"nome": "Charmander", "tipo": "fogo", "nivel": 5},
    {"nome": "Squirtle", "tipo": "água", "nivel":5},
    {"nome": "Bulbasaur", "tipo": "grama", "nivel": 5}
    ]

print("nome" in pokemons)# nao encontra, agora temos uma lista de dicionarios
print("nome" in pokemons[0]) # encontra pois pokemons[0] acessa o elemento da lista

string = "o sabor banana caiu como uma luva"
print("banana" in string) # encontra a string
print("ana" in string) # encontra a substring
print("a" in string) # encontra o caractere
print("uva" in string) # encontra a substring na palavra "luva"
print(" uva " in string) # não encontra pois procuramos com espaços

# set
inteiros = {1, 2, 3, 4, 5, 86456}
print(3 in inteiros) # true esta presente
print(10 in inteiros) # false nao esta presente
print(10 not in inteiros) # true nao esta presente

# not in e uso em condicional
paises_brics = ["Brasil", "Rússia", "India", "China", "África do Sul"]

pais_buscado = "Suriname"
if pais_buscado not in paises_brics:
    print(f"{pais_buscado} não faz parte dos países do BRICS")
else:
    print(f"{pais_buscado} faz parte dos países do BRICS")
    
