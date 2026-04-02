# usando loop
num_pares = []
for i in range(10):
    if i % 2 == 0:
        num_pares.append(i)
print(f"com loop: {num_pares}")

#comprehension
num_pares_comprehension = [i for i in range ( 10) if i % 2 == 0]
print(f"com comprehension: {num_pares_comprehension}")

print("--"*20)

#loop 
frutas = ["abacaxi", "banana", "acerola", "uva", "ameixa", "melancia"]
frutas_com_a= []

for x in frutas:
  if x.startswith("a"):
    frutas_com_a.append(x)
print(f"com loop: {frutas_com_a}")

#comprehension
frutas_com_a_comprehension = [x for x in frutas if x.startswith("a")]
print(f"com comprehension: {frutas_com_a_comprehension}")

print("--"*20)

# com loop
numeros = []
for i in range(20):
    numeros.append(i)
print(f"com loop: {numeros}")

#comprehension
numeros_comprehension = [i for i in range(20)]
print(f"com comprehension: {numeros_comprehension}")