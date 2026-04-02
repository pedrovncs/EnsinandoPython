lista_convidados = ("pedro", "tiago", "joão", "maria", "volodmyr zelensky")

nome = input('digite nome de quem quer verificar: ').lower().strip()

if nome not in lista_convidados:
    print(f'{nome} não tá na lista de convidados')
else:
    print(f'{nome} tá na lista de convidados')
    

