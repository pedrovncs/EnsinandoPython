from random import randint

nome = "pedro"
num_especifico = 3
num_aleatorio = randint(1, 3)#numero aleatorio de 1 a 3

# operadores relacionais sempre retornam true ou false

# operador "==" verifica se o valor é igual
print("\noperador de igualdade ==")
print(f'numero {num_aleatorio}  e {num_especifico} são iguais?: {num_aleatorio == num_especifico}')
print(f'nome é igual a pedro?: {nome == "pedro"}' )
print(f'nome é igual a Pedro?: {nome == "Pedro"}' )

# operador "!=" verifica se o valor é diferente
print("\noperador de diferença !=")
print(f'numero {num_aleatorio}  e {num_especifico} são diferentes?: {num_aleatorio != num_especifico}')
print(f'nome é diferente de Maria?: {nome != "Maria"}' )
print(f'nome é diferente de pedro?: {nome != "pedro"}' )

# operador ">" verifica se o valor é maior
print("\noperador de maior >")
print(f'numero {num_aleatorio}  é maior que {num_especifico}?: {num_aleatorio > num_especifico}')
print(f'nome é maior que pedro paiva?: {nome > "pedro paiva"}' )
print(f'nome é maior que pedro?: {nome > "pedro"}' )
print(f'nome é menor que pedro?: {nome < "pedro"}' ) # operador ">=" verifica se o valor é maior ou igual

# operador "<" verifica se o valor é menor
print("\noperador de menor <")
print(f'numero {num_aleatorio}  é menor que {num_especifico}?: {num_aleatorio < num_especifico}')
print(f'nome é menor que pedro paiva?: {nome < "pedro paiva"}' )
print(f'nome é menor que pedro?: {nome < "pedro"}' )
print(f'nome é menor que pedro?: {nome < "pedro"}' )# operador "<=" verifica se o valor é menor ou igual

# em casos de comparação entre strings e números devemos usar a funcao len()
print("\ncomparação entre strings e números usando len()")
# print(f'nome é maior que 5?: {nome > 5}' ) nao funciona
print(f'comprimento do nome é maior que 5?: {len(nome) > 5}' )
print(f'comprimento do nome é menor que 5?: {len(nome) < 5}' )
print(f'comprimento do nome é menor ou igual 5?: {len(nome) <= 5}' )
print(f'comprimento do nome é igual a 5?: {len(nome) == 5}' )
print(f'comprimento do nome é diferente que 5?: {len(nome) != 5}' )

# case sensitive
filme = "The Goodfellas"
filme_input_usuario = "the Goodfellas"

filme == filme_input_usuario  # False
filme == filme_input_usuario.lower() # True 
