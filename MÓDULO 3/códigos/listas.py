livros_mistborn = ["O Império Final", "O Poço da Ascensão", "O Herói das Eras"]
print(livros_mistborn)

livro1_imperio_final = livros_mistborn[0]
# exemplo de acesso a um elemento da lista (listas assim como string começam com índice 0)
print(f'o livro na posição 0 é: {livro1_imperio_final}')

frutas_e_numeros = ["limão", "laranja", 334, "abacaxi", 12.4, 0] # deve ser evitado misturar
pessoas = ["Joel", "Ellie", "Tommy", "Tess", "Bill", "Marlene"]
notas = [9.5, 8.0, 7.5, 10.0, 6.0, 8.0]

#m métodos principais
# count
nota_buscada = 8
print(f'contagem de vezes da nota {nota_buscada} na lista notas: { notas.count(nota_buscada)}') # 2 

# append
pessoas.append("Abby")
print(f'último elemento da lista pessoas: {pessoas[-1]}') # o ultimo elemento deve ser o que adicionamos: "Abby"

# pop
print(f'elemebto removido do final da lista pessoas: {pessoas.pop()}') #Abby 
pos = 2
print(f'elemento removido da lista frutas_e_numeros na posicao {pos}: {frutas_e_numeros.pop(pos)}') # 334

#insert
pos = 1
frutas_e_numeros.insert(pos, "banana")
print(f'elemento na posição {pos} da lista frutas_e_numeros: {frutas_e_numeros[pos]}') # banana

# extend (também pode ser feito com operador + ou +=, mas o extend é mais eficiente)
mais_frutas = ["uva", "melancia"]
frutas_e_numeros.extend(mais_frutas)
print(f'lista frutas_e_numeros após extensão: {frutas_e_numeros}')

# sum
print(f'soma da lista notas: {sum(notas)}')

# len
print(f'tamanho da lista pessoas: {len(pessoas)}')
print(f'tamanho da lista frutas_e_numeros: {len(frutas_e_numeros)}')

# indes
print(f'índice do elemento "Tommy" na lista pessoas: {pessoas.index("Tommy")}') # 2
print(f'índice do elemento 12.4 na lista frutas_e_numeros: {frutas_e_numeros.index(12.4)}') # 5

# sort vs sorted
numeros1 = [5, 2, 9, 1, 5, 6]

numeros_ordenados = sorted(numeros1)
print(f'lista numeros apos sorted(): {numeros_ordenados}')# nada mudou

numeros1.sort()
print(f'lista numeros apos .sort(): {numeros1}') # foi modificada


# slicing (lembra que começa em 0 e o último pode ser acessado com -1)
#formato do slicing: lista[inicio:fim:passo]
print(pessoas[0:3]) #do primeiro ao 3: Joel, Ellie, Tommy
print(frutas_e_numeros[1:5]) # do segundo ao quinto: laranja, 334, abacaxi, 12.4
print(notas[::2]) # do primeiro ao último com passo 2: 9.5, 7.5, 6.0
print(livros_mistborn[-1]) # do último: O Herói das Eras
print(pessoas[-3:]) # dos últimos 3: Tess, Bill, Marlene
print(livros_mistborn[::-1]) # do último ao primeiro: O Herói das Eras, O Poço da Ascensão, O Império Final

# copiando lista 
lista_exemplo = ["A", "B", "C"]
# com slicing 
copia_lista = lista_exemplo[:] # sem especificar o início e o fim, pega toda a lista

copia_lista[0] = "X"
print(f'lista original: {lista_exemplo}') 
print(f'copia da lista: {copia_lista}') 

# com método copy
copia_lista = lista_exemplo.copy() # por baixo dos panos segue a mesma lógica do slicing

copia_lista[0] = "Z"
print(f'lista original: {lista_exemplo}') 
print(f'copia da lista: {copia_lista}') 

# copiando lista aninhada, copy ou slicing não funciona nesse caso
lista_exemplo_aninhado = [["A", "B"], ["C", "D"]]

import copy
copia_lista_aninhada = copy.deepcopy(lista_exemplo_aninhado) # deepcopy é necessario

