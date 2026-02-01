# Perguntar ao usuário sobre as condições
chovendo = input("Está chovendo? (sim/não): ").lower() == "sim"
sol = input("Está sol? (sim/não): ").lower() == "sim"
tiros = input("Ouve tiros? (sim/não): ").lower() == "sim"

# Determinar se deve levar guarda-chuva
levar_guarda_chuva = chovendo and not tiros

# Exibir resultado
if levar_guarda_chuva:
    print("Você DEVE levar guarda-chuva!")
else:
    print("Você NÃO precisa levar guarda-chuva.")