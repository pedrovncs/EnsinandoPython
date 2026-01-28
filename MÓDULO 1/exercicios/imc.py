"""
calculadora IMC
solicite ao usuário seu peso e altura. realize o cálculo do imc e exiba o 
valor encontrado no terminal.

"""
peso = input("insira o peso: ")

altura = input("insira a altura: ")

calculo =  float(peso) / (float(altura) ** 2 )

print(f'imc: {calculo:.2f}')