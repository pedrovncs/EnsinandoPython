"""
o sinal de comunicação entre a terra e uma sonda espacial viaja na velocidade da luz (300.000km/s). 
solicite como entrada a distância em quilômetros de uma sonda enviada para marte, 
calcula o tempo em minutos e segundos que uma mensagem leva para chegar até a sonda.
*dica: use // para os minutos e % para segundos.


""" 

VELOCIDADE_LUZ = 300000

distancia_km = float(input("INSIRA A DISTANCIA EM KM: "))

segundos_totais = distancia_km / VELOCIDADE_LUZ

print(f'segundos totais: {segundos_totais:.2f}')

minutos = segundos_totais // 60
segundos_restantes = segundos_totais % 60

print(f'se a sonda estiver a {distancia_km} quilometros de distancia, ela leva {minutos} min e {round(segundos_restantes)}s')




