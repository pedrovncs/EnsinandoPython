pessoa1 = {"nome": "Pedro", "sobrenome": "Vinicius", "idade": 24}

print(pessoa1["nome"])
print(pessoa1["sobrenome"])
print(pessoa1["idade"])

print(pessoa1.get("name", "chave não encontrada"))

items = pessoa1.items()
print(type(items))

# dicionario simulando json
twin_peaks_data = {
    "serie": "Twin Peaks",
    "ano": 1990,
    "criadores": ["David Lynch", "Mark Frost"],
    "ativa": False,                           
    "protagonista": {
        "nome": "Dale Cooper",
        "coisas_favoritas": ("Café Preto", "Torta de Cereja") 
    },
    "episodios": [
        {
            "num": 1,
            "titulo": "Pilot",
            "diretor": "David Lynch",
            "tags": ["assassinato", "investigacao"] 
        }
    ]
}

print(f"\nSérie: {twin_peaks_data['serie']}")

print(f"\nPrimeiro episódio: {twin_peaks_data['episodios'][0]['titulo']}")

print(f"\nProtagonista: {twin_peaks_data['protagonista']['nome']}")

print(f"\nCoisas favoritas do protagonista: {twin_peaks_data['protagonista']['coisas_favoritas']}")

print(f"\nDiretor do episódio 1: {twin_peaks_data['episodios'][0]['diretor']}")

# dicionario simulando json pokemon 
time_ash_kanto = {
    "nome": "Ash Ketchum",
    "regiao": "Kanto",
    "idade": 10,
    "time": [
    {
        "pokemon": "Pikachu",
        "golpes": ["Choque do Trovão", "Ataque Rápido", "Trovão", "Agilidade"],
        "tipos": ("Elétrico",)
    },
    {
        "pokemon": "Charizard",
        "golpes": ["Lança-chamas", "Arremesso Sísmico", "Ataque de Asa", "Fúria do Dragão"],
        "tipos": ("Fogo", "Voador")
    },
    {
        "pokemon": "Bulbasaur",
        "golpes": ["Chicote de Cipó", "Folha Navalha", "Semente Sanguessuga", "Raio Solar"],
        "tipos": ("Planta", "Venenoso")
    },
    {
        "pokemon": "Squirtle",
        "golpes": ["Jato de Água", "Bolhas", "Retrair", "Giro Rápido"],
        "tipos": ("Água",)
    },
    {
        "pokemon": "Pidgeot",
        "golpes": ["Ventania", "Ataque de Areia", "Ataque Rápido", "Agilidade"],
        "tipos": ("Normal", "Voador")
    },
    {
        "pokemon": "Butterfree",
        "golpes": ["Pó do Sono", "Pó de Paralisia", "Psíquico", "Vento de Prata"],
        "tipos": ("Inseto", "Voador")
    }]
}

print(f"\nNome do treinador: {time_ash_kanto['nome']}")
print(f"\nPrimeiro Pokémon do time: {time_ash_kanto['time'][0]['pokemon']}")
print(f"\nGolpes do Charizard: {time_ash_kanto['time'][1]['golpes']}")
print(f"\nTipos do Bulbasaur: {time_ash_kanto['time'][2]['tipos']}")
print(f"\nSegundo golpe do Squirtle: {time_ash_kanto['time'][3]['golpes'][1]}")
print(f"\nTipos do Pidgeot: {time_ash_kanto['time'][4]['tipos']}")
print(f"\nGolpes do Butterfree: {time_ash_kanto['time'][5]['golpes']}")

#gerando relatorio do time do ash
for pokemon in time_ash_kanto['time']:
    nome = pokemon['pokemon']
    tipos = ", ".join(pokemon['tipos'])
    
    print(f"\nRelatório de{nome}")
    
    # loop aninhado pelos golpes de cada pokemon
    print("Golpes disponíveis:")
    for golpe in pokemon['golpes']:
        print(f"  - {golpe}")
    print("-" * 20)
