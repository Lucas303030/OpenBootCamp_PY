from Ejercicio8.operaciones import *

num1, num2 = int(input("Ingrese primer valor: ")), int(input("Ingrese segundo valor: "))

print(f"{num1} + {num2} = {suma(num1, num2)}")
print(f"{num1} - {num2} = {resta(num1, num2)}")
print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
print(f"{num1} / {num2} = {round(division(num1, num2), 2)}")