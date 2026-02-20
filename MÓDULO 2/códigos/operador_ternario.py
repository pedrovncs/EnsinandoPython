# classificando idade
idade = int(input("digite a idade da pessoa: "))

#condicional
if idade >= 18:
    tipo_de_pessoa = "adulto"
else:
    tipo_de_pessoa = "menor"
print(f"\nessa pessoa é um {tipo_de_pessoa}.")

#ternário
tipo_de_pessoa = "adulto" if idade >= 18 else "menor"
print(f"\nfeito com ternário: essa pessoa é um {tipo_de_pessoa}.")

# par ou impar #
numero = int(input("\ninsira um numero inteiro: "))

#condicional
if numero % 2 == 0:
    tipo_numero = "par"
else:
    tipo_numero = "impar"
print(f"\no numero {numero} é {tipo_numero}.")

#ternário
print(f"\nfeito com ternário: o numero {numero} é {"par" if numero % 2 == 0 else "impar"}.")

# exemplo print
clima = "chuva"
print(f"vou levar um {'guarda-chuva' if clima == 'chuva' else 'boné'}.")


a = 13

eh_par = True if (a % 2 == 0) else False

print(eh_par)
