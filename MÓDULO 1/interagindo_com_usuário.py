# input()
nome = input("qual é o seu nome? ")
print(f"\nolá, {nome}!")

print("qual é sua idade?")
idade = input()
print(f"\nvocê tem {idade} anos.")

# utilizando o input 
numA = input("insira o valor do número 1: ")
numB = input("insira o valor do número 2: ")
print(f"\nnumA: {numA}")
print(f"numB: {numB}")

#verificando os tipos
print("numA é do tipo:", type(numA))
print("numB é do tipo:", type(numB))

# somando os valores 
soma = numA + numB
print(f"\nsoma (concatenação): {soma}")

# multiplicando os valores 
multiplicacao = numA * numB
print(f"\nmultiplicação: {multiplicacao}")

