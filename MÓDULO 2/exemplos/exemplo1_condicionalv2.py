idade = int(input("digite idade: "))

print("verificando se a pessoa é maior de idade... (essa mensagem sempre é exibida)")

if idade > 120:
    print("voce me parece velho demais...")
elif idade >= 18:
    print("voce é maior de idade")
elif idade < 0:
    print("voce ainda não nasceu!")
else:
    print("voce é menor de idade")