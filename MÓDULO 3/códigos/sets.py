numeros = {1,4,5,67,4,334}
print(type(numeros))
print(numeros) 

#set vazio 
conjunto_vazio = set()
#conjunto_vazio = {} isso e um dicionario vazio

bandas_pedro = {"The Smiths", "The Cure", "Lush", "The Doors", "The Beatles"}
bandas_danilo = {"The Beatles", "7Minutoz", "Lush", "MASS OF FERMENTING DREGS"}
bandas_joissi = {"Arctic Monkeys", "The Cure", "Scorpions", "The Smiths", "The Beatles"}
bandas_lorran = {"Gilberto Gil", "Djavan", "Caetano Veloso", "The Beatles"}

bandas_pedro.add("The Smiths") # ignora sem erros

# todas as bandas 
todas_as_bandas = bandas_danilo | bandas_joissi | bandas_pedro | bandas_lorran

print(f"\nTOTAL DE {len(todas_as_bandas)} BANDAS")
print(todas_as_bandas)

# bandas em comum entre pedro & danilo
em_comum_p_d = bandas_danilo.intersection(bandas_pedro)
print(F"\nTOTAL DE {len(em_comum_p_d)} BANDAS EM COMUM pedro & danilo")
print(em_comum_p_d)

# bandas em comum entre pedro & danilo & joissi
em_comum_p_d_j = bandas_pedro & bandas_danilo & bandas_joissi
print(F"\nTOTAL DE {len(em_comum_p_d_j)} BANDAS EM COMUM pedro & danilo & joissi")
print(em_comum_p_d_j)

# bandas em comum entre danilo & lorran
em_comum_d_j = bandas_danilo & bandas_lorran
print(F"\nTOTAL DE {len(em_comum_d_j)} BANDAS EM COMUM danilo & lorran")
print(em_comum_d_j)

# bandas só pedro ouve entre pedro e lorran
somente_p_em_p_l = bandas_pedro - bandas_lorran
print(F"\nTOTAL DE {len(somente_p_em_p_l)} BANDAS UNILATERAIS pedro - lorran")
print(somente_p_em_p_l)

# bandas que só pedro ouve entre pedro e lorran
somente_p_em_p_l = bandas_pedro - bandas_lorran
print(F"\nTOTAL DE {len(somente_p_em_p_l)} BANDAS UNILATERAIS pedro - lorran")
print(somente_p_em_p_l)

# bandas só pedro ou só joissi ouve entre pedro e joissi
somente_um_em_p_j = bandas_pedro.symmetric_difference(bandas_joissi)
print(F"\nTOTAL DE {len(somente_um_em_p_j)} BANDAS EXCLUSICAS pedro ^ joissi")
print(somente_um_em_p_j) 
