altura = float(input("Cual es tu altura ?: "))
peso = float(input("Cual es tu peso ?: "))

imc = round(peso / (altura**2), 2)
print (f"Tu índice de masa corporal es {imc}")