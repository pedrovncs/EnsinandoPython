lista_convidados = ["pedro", "tiago", "joão", "maria", "volodmyr zelensky"]

nome = input('digite nome de quem quer verificar: ').lower().strip()

respostas_sim = ['sim', 's', 'yes', 'y' "si"]
respostas_nao = ['não', 'nao', 'n', 'no']

if nome not in lista_convidados:
    print(f'{nome} não tá na lista de convidados')
    print('deseja adicionar a pessoa na lista?')
    
    resposta = input('responda sim ou não: ').lower().strip()
    if resposta in respostas_sim:
        lista_convidados.append(nome)
        print(f'{nome} adicionado a lista de convidados')
        print(f'lista de convidados atualizada: {lista_convidados}')
        
    elif resposta in respostas_nao:
        print(f'{nome} não adicionado a lista de convidados')
        
    else:
        print('resposta inválida, por favor responda sim ou não')
else:
    print(f'{nome} tá na lista de convidados')
    

