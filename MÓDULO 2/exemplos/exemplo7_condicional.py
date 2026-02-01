idade = int(input("digite a idade: "))

print("\n** verificacao de idade para chat de voz no roblox... **\n")
if idade >= 14:
    print("idade verificada ✅")
    has_id = input("voce tem rg (sim / não): ")
    
    if has_id == "sim":
        print("rg verificado ✅")
        is_member = input("voce é membro (sim / não): ")

        if is_member == "sim":
            print("acesso concedido, pode usar o chat de voz 🎉")
        else:
            print("apenas membros tem acesso ao chat de voz")
    else:
        print("rg necessario")
else:
    print("voce precisa ter no minimo 14 anos para usar o chat de voz")
