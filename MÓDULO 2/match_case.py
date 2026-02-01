print("""
lista de dias:
segunda
terça 
quarta
quinta
sexta
sábado
domingo""")
day = input("insira o dia da semana: ")

match day:
    case "segunda":
        print("semana começando")
    case "sexta":
        print("quase fim de semana")
    case "sábado" | "domingo":
        print("fim de semana")
    case _:
        print("dia normal")
        
        
""" idade = int(input("qual sua idade: "))

# não é possível usar comparações diretas
match idade:
    case idade > 120:
        print("muito velho")
    case idade >= 18:
        print("adulto")

 """