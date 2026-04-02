"""
solicite que o usuário insira seu nome e sua senha, faça a validação da 
senha verificando as condições:
● deve ter no minimo 6 caracteres 
● no maximo 16 caracteres
● não pode conter ter espaços
informa a situação da senha.
"""

nome = input()
senha = input()

if len(senha) > 16:
    print("senha nao aprovada, nao pode ter mais de 16")
elif len(senha) < 6:
    print("senha nao aprovada, nao pode ter menos de 6")
elif len(senha) != len(senha.replace(" ", "")):
    print("senha nao aprovada, nao pode ter espaco")
else: 
    print("senha aprovada")
    
    
    

