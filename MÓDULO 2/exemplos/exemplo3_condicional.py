login = input('insira seu login: ')
senha = input('insira sua senha: ')

LOGIN_USUARIO = 'admin'
SENHA_USUARIO = "2345678"

if (not login or not senha):
    print("voce deve inserir login e senha")
elif (login == LOGIN_USUARIO and senha == SENHA_USUARIO):
    print("acesso permitido")
else:
    print("acesso negado")