saldo_bancario = 1000

valor_saque = float(input("quanto quer sacar: ")) # -100

if (valor_saque <= 0): # o valor é menor ou igual a zero?
    print(f"tentativa de sacar valor {valor_saque} negada, valor nao positivo.")
elif (valor_saque <= saldo_bancario): # o valor digitado é menor que o valor na conta?
    saldo_bancario -= valor_saque
    print(f"saque realizado com sucesso, valor atual em conta {saldo_bancario}")
else:
    print("saldo insuficiente para saque")
