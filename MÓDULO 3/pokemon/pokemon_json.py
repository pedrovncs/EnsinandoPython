from urllib import response
import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"

while True:
    response = requests.get(url)

    next_page = response.json().get("next", url)
    previous_page = response.json().get("previous", url)
    pokemons = response.json().get("results", [])
    
    with open(r"MÓDULO 3\pokemon\pokemons.json", "w") as f:
        json.dump(pokemons, f, indent=4)

    for i, pokemon in enumerate(pokemons):
        print(f'{i}: {pokemon["name"]}')
    
    print("n - avançar / p - retornar")
    opt = input("ou escolha um pokemon: ")
    
    if opt == "n":
        url = next_page
        continue
    elif opt == "p":
        url = previous_page
        continue
    else: 
        response = requests.get(pokemons[int(opt)]["url"])
        image_url = response.json().get("sprites").get("front_default")
        pokemon_name = response.json().get("name")
        image_req = requests.get(image_url)
        print(image_req)
        
        with open(fr'MÓDULO 3\pokemon\{pokemon_name}.png', "wb") as f:
            f.write(image_req.content)
    break