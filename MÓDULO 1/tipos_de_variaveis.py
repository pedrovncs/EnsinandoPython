# string 
nome = "pedro"
tipo_da_variavel = type(nome)
print(tipo_da_variavel)

terceira_letra = nome[1] # "pedro"
print(f"\nsegunda letra de {nome} é '{terceira_letra}'")

terceira_letra = nome[-1] # "pedro"
print(f"\núltima letra de {nome} é '{terceira_letra}'")

# métodos de string
frase = "because ignorance is a bliss.\n"

print(f'\nfrase original: {frase}')

print(f'frase maiúscula: {frase.upper()}')

print(f'frase minúscula: {frase.lower()}')

print(f'frase capitalizada: {frase.capitalize()}')

print(f'frase com título: {frase.title()}')

print(f'frase sem quebra de linha: {frase.strip()}')

print(f'frase trocada: {frase.replace("python", "java")}')

# funçoes uteis com string
tamanho_da_frase = len(frase)
print(f'\ntamanho da frase: {tamanho_da_frase} caracteres')

# concatenando string
nova_frase = frase.strip() + " - Gray, Thomas."
print(f'\nfrase concatenada: {nova_frase}')

# int e float
produto_preco = 49.99
quantidade = 3
desconto = 5.0

# cálculos básicos
total_bruto = produto_preco * quantidade
total_com_desconto = total_bruto - desconto

print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto aplicado: R$ {desconto}")

# aumentando o desconto em 2.0
desconto += 2.0  
print(f"\nDesconto atualizado: R$ {desconto}")

#diminuindo a quantidade em 1
quantidade -= 1
print(f"Quantidade atualizada: {quantidade}")

# truques de divisão
print(f"\nDivisão Comum (10 / 3): {10 / 3}")       # 3.333...
print(f"Divisão Inteira (10 // 3): {10 // 3}")     # 3
print(f"Resto da Divisão (10 % 3): {10 % 3}")      # 1

# funções úteis
nota = 8.7654
print(f"\nNota arredondada: {round(nota, 2)}")

# boolean
vivo = True
morto = False
print(f"\nVivo: {vivo}, Tipo: {type(vivo)}")
print(f"Morto: {morto}, Tipo: {type(morto)}")