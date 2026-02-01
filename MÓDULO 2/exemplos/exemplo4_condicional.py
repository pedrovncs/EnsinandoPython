saldo_bancario = 1000

valor_saque = float(input("quanto quer sacar: "))

if (valor_saque <= 0):
    print("deve sacar valor positivo")
elif (valor_saque <= saldo_bancario):
    saldo_bancario -= valor_saque
    print(f"saque realizado com sucesso, valor atual em conta {saldo_bancario}")
else:
    print("saldo insuficiente para saque")
