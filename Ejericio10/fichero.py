# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.


try: 
    f = open(r"C:\Users\Lucas\Documents\GitHub\OpenBootCamp_PY\Ejericio10/text.txt", "x")
    f.close
except FileExistsError:
    pass

    f = open(r"C:\Users\Lucas\Documents\GitHub\OpenBootCamp_PY\Ejericio10/text.txt", "w")

    f.writelines("Prueba de Writelines\n")

f.close()

