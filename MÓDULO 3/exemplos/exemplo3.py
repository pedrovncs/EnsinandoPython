estoque = {
    "banana": 19,
    "laranja": 12,
    "coca-cola": 5,
    "urânio enriquecido": 0,
    "memória ram ddr5": 1
}

busca = input("qual produto quer verificar: ").lower().strip()

if busca not in estoque:
    print(f"não vendemos o produto: {busca}")
elif busca in estoque and estoque[busca] > 0:
    print(f"temos {estoque[busca]} unidades de {busca} em estoque. {"corre ta acabando" if estoque[busca] <= 2 else ""}")
else:
    print(f"o produto {busca} está esgotado no momento")
