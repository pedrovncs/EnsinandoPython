import math
print(math.sqrt(16))

print("Calculadora de Área de Triângulos")
print("\nTipos de triângulos:")
print("1. Equilátero")
print("2. Isósceles")
print("3. Escaleno")
print("4. Retângulo")

tipo = input("\nEscolha o tipo de triângulo (1-4): ")

if tipo == "1":
    lado = float(input("Digite o comprimento do lado: "))
    area = (lado ** 2 * math.sqrt(3)) / 4
    print(f"Área do triângulo equilátero: {area:.2f}")

elif tipo == "2":
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    area = (base * altura) / 2
    print(f"Área do triângulo isósceles: {area:.2f}")
    
elif tipo == "3":
    a = float(input("Digite o lado a: "))
    b = float(input("Digite o lado b: "))
    c = float(input("Digite o lado c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Área do triângulo escaleno: {area:.2f}")

elif tipo == "4":
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    area = (base * altura) / 2
    print(f"Área do triângulo retângulo: {area:.2f}")

else:
    print("Opção inválida!")
