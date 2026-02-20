# type casting combinado
numA = int(input("insira um número inteiro: "))
print(f"valor: {numA}, tipo: {type(numA)}")

# type casting posterior
numB_raw = input("insira um número decimal (ex: 1.5): ")
numB = float(numB_raw)
print(f"valor: {numB}, tipo: {type(numB)}")

# type casting em etapas
# tentar int("1.8") não funciona diretamente
texto_decimal = "1.8"
resultado = int(float(texto_decimal)) 
print(f"de string '{texto_decimal}' para int: {resultado}")

# booleanos inesperados, sempre verifica a existencia de algum valor e não o conteúdo
print(bool("qualquer texto")) # True
print(bool(""))               # False (Vazio)

# mas com binários é diferente
a = 0
b = 1
print(bool(a))  # retorna False
print(bool(b))  # retorna True

# erros Comuns
# int("vinte")      # ValueError: texto não é numeral
# int("3.14")       # ValueError: int não entende o ponto decimal diretamente

