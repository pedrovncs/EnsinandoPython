# considerados False em Python
string_vazia = ""
numero_zero_int = 0
numero_zero_float = 0.0
lista_vazia = []
dicionario_vazio = {}
conjunto_vazio = set()
tupla_vazia = ()
none_value = None

print("valores considerados False em Python:\n")
if not string_vazia:
    print("string vazia é considerada False")
if not numero_zero_int:
    print("int zero é considerado False")
if not numero_zero_float:
    print(" float zero é considerado False")
if not lista_vazia:
    print("lista vazia é considerada False")
if not dicionario_vazio:
    print("dict vazio é considerado False")
if not conjunto_vazio:
    print("set vazio é considerado False")
if not tupla_vazia:
    print("tupla vazia é considerada False")
if not none_value:
    print("none é considerado False")
    
# considerados True em Python
string_nao_vazia = "python"
numero_positivo_int = 42
numero_negativo_float = -3.14
lista_com_elementos = [1, 2, 3]
print(lista_com_elementos)
dicionario_com_elementos = {"chave": "valor"}
conjunto_com_elementos = {1,2,3}
tupla_com_elementos = (1, 2, 3)

print("\nvalores considerados True em Python:\n")
if string_nao_vazia:
    print("string não vazia é considerada True")
if numero_positivo_int:
    print("int positivo é considerado True")
if numero_negativo_float:
    print("float negativo é considerado True")
if lista_com_elementos:
    print("lista com elementos é considerada True")
if dicionario_com_elementos:
    print("dict com elementos é considerado True")
if conjunto_com_elementos:
    print("set com elementos é considerado True")
if tupla_com_elementos:
    print("tupla com elementos é considerada True")