contador = 0

while contador < 10:
    print(f"contando: {contador}")
    contador+=1
    
# loop infinito
""" while True:
    print("este loop nunca vai acabar a menos que a gente use um break") """

while True:
    algo = input("digite algo: ")
    if algo == "sair":
        print("saindo do loop")
        break
    
lista_de_tarefas = ["limpar casa", "estudar python", "fazer compras", "ir ao médico"]

while lista_de_tarefas:
    lista_de_tarefas.pop(0)
    print(f"tarefa finalizada, tarefas restantes: {len(lista_de_tarefas)}")
else: 
    print("todas as tarefas foram finalizadas")

