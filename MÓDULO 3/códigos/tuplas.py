coordenadas = (-22.95009428252824, -43.210176394896514) 
print(f'coordenadas: {coordenadas}')

animais_e_numeros = ("gato", "cachorro", 42, "papagaio", 3.14, 0, 42, 42)

numeros = (1, 2, 3, 4, 5)

 # a vírgula é necessária para criar uma tupla de um elemento do contrário representa a precedencia de operadores
tupla_um_elemento = (42,)
#tupla_um_elemento = (42) tipo inteiro e não tupla 

print(f'tupla de um elemento: {tupla_um_elemento}')

# slicing tuplas são imutáveis, mas podemos acessar seus elementos e fazer slicing normalmente
print(animais_e_numeros[0::])

# métodos principais

#count
print(f'contagem de vezes do número 42 na tupla animais_e_numeros: {animais_e_numeros.count(42)}') # 3

#index
print(f'índice do elemento "papagaio" na tupla animais_e_numeros: {animais_e_numeros.index("papagaio")}') # 3

#burlando a imutabilidade das tuplas

#type casting
tupla = ("A", "B", "C")
print(f'tupla original: {tupla}')

lista = list(tupla)
lista[0] = "X"
tupla = tuple(lista)

print(f'tupla modificada: {tupla}') 

#listas dentro de tuplas
tupla_com_lista = (["A", "B", "C"],)
tupla_com_lista[0][0] = "X"
print(f'tupla com lista modificada: {tupla_com_lista}')

# erros 
""" numeros[0] = 10 
animais_e_numeros.append("leão") """
