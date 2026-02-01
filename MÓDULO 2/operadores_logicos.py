peixe = "Pirarucu"
agua_doce = True
peso = 4.754

ensolarado = True
temperatura = 38

#operadors lógicos sempre retornam true ou false

#operador "and" retorna True se ambas forem verdadeiros
print('"\noperador lógico "and" ')
print(f"Está ensolarado e a temperatura é maior que 30?: {ensolarado and temperatura > 30}")
print(f"Não está ensolarado e a temperatura é maior que 30?: {not ensolarado and temperatura > 30}")

#operador "or" retorna True se uma for verdadeira
print('"\noperador lógico "or" ')
print(f'Peixe é de agua doce ou é Pirarucu?: {agua_doce or peixe == "Pirarucu"}')
print(f'Está ensolarado ou a temperatura é maior que 32?: {ensolarado or temperatura > 32}')

#operador "not" inverte o valor lógico
print('"\noperador lógico "not" ')
print(f'Peixe não é de agua doce?: {not agua_doce}')
print(f'Não está ensolarado?: {not ensolarado}')