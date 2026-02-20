fortuna = float(input('qual seu valor acumulado?: '))

if fortuna >= 1000000:
    print("VIP")
elif fortuna >= 500000:
    print("premium")
elif fortuna >= 300000:
    print("deluxe")
elif fortuna >= 100000:
    print("intermediario")
elif fortuna >= 10000:
    print("iniciante")
else:
    print("não classificado")    