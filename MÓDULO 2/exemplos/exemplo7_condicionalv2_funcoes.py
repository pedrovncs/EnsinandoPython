def validar_idade():
    idade = int(input("digite a idade: "))
    if idade >= 14:
        print("idade verificada ✅")
        return True
    else:
        return False

def validar_rg():
    resp = input("tem rg? sim / nao")
    if resp == "sim":
        print("rg verificado ✅")
        return True
    else: 
        return False
    
def validar_membro():
    resp = input("é membro? sim / nao")
    if resp == "sim":
        print("membro verificado ✅")
        return True
    else: 
        return False
    
def validar_autorizacao():
    resp = input("sua mae deixa? sim / nao")
    if resp == "sim":
        print("autorizacao verificada ✅")
        return True
    else: 
        return False

def validar_horario_do_dia():
    resp = input("tade dia?")
    if resp == "sim": return True  
    
    return False

print("\n** verificacao de idade para chat de voz no roblox... **\n")

if (validar_idade() and validar_membro() and validar_rg() and validar_autorizacao() and validar_horario_do_dia()):
    print("acesso liberado")
else: 
    print("acceso restrito")