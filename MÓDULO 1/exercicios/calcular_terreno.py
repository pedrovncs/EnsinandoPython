"""
receba como entrada os valores de base e altura de terrenos  
quadrados ou retangulares.

calcule a área total do terreno e exiba no terminal.

solicite o valor por metro quadrado do terreno e use para calcular o valor 
total do terreno. 

ao final exiba o tamanho do terreno e valor total com 2 casas decimais 
no terminal.

"""

base = float(input("insira a base: "))
altura = float(input("insira a altura: "))

area = (base * altura)

print(f"A ÁREA TOTAL DO TERRENO É DE {area}m2")

valor_m2 = float(input("insira o valor por m2 do terreno: "))

valor_total = area * valor_m2

print(f"O tamanho total é de {area} - total R${valor_total:.2f}")