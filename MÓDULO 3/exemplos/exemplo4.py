viagens_feitas = ["RJ", "SP", "SP", "SP", "RJ", "SP", "MG", "PE", "RJ"]

total_de_viagens = len(viagens_feitas)
print(f"total de viagens: {total_de_viagens}")

estados_visitados = set(viagens_feitas)
total_estados_visitados = len(estados_visitados)
print(f"total de estados visitados: {total_estados_visitados}")

print(f"estados visitados: {estados_visitados}")
