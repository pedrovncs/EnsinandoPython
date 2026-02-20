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
    case "terça" | "quarta" | "quinta":
        print("dia normal")
    case _:
        print("insira um dia valido")
    
""" #idade = int(input("qual sua idade: "))

# não é possível usar comparações diretas
""" """ match idade:
    case 1:
        print("muito velho")
    case "eee":
        print("adulto")
"""