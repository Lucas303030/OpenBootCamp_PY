from calendar import isleap

def biciesto(anio):
    if isleap(anio) == True:
        return f"El {anio} es biciesto"
    else: 
        return f"El {anio} no es biciesto"

anio = int(input("Ingrese año: "))
print(biciesto(anio))