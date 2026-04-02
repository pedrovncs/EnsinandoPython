numeros = [1,2,3,4,5,6,7,8,9,10]

for n in numeros:
    print(n)
else:
    print("Fim do loop")

#dicionarios    
country = {"nome": "Brasil", "capital": "Brasília", "populacao": 213000000}

for chave in country:
    print(chave)

# usando .items() retorna uma tupla com chave e valor
print(country.items())
for chave, valor in country.items():
    print(f"{chave}: {valor}")
    

# enumerate para obter o indice e o item
frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"]

for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
    
    
# range para criar loops sem uma colecao pre definida

print("\n de 0 a 4")
for i in range(5):
    print(i)

print("\n de 0 a 9 de 2 em 2")
for i in range(0, 10, 2):
    print(i)

print("\n de 1 a 9")
for i in range(1, 10):
    print(i)
    
print("\n iterando sobre os indices da lista frutas")
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")
    
# zip() para juntar listas 

print("\n iterando sobre lista1 - letras e lista2 - numeros")
lista1 = ["a", "b", "c"]
lista2 = [3,2,1]

for letra, numero in zip(lista1, lista2):
    print(f"{letra}: {numero}")
    
#. items() para iterar sobre dicionarios
print("\n iterando sobre o dicionario usando .items()")

games_mais_vendidos = {"PSP": "GTA: Liberty City Stories", 
                       "PS2": "GTA: San Andreas",  
                       "NDS": "New Super Mario Bros",
                       "3DS": "Mario Kart 7"}

print(f"RESULTADO .ITEMS(): {games_mais_vendidos.items()}")
for console, jogo in games_mais_vendidos.items():
    print(f"{console}: {jogo}")

#loop for aninhado
matriz = [
    [65, 212], 
    [1113, 42]
    ]

for linha in matriz:
    for item in linha:
        print(item)
        
