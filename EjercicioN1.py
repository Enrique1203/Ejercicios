cvoc=0
frase = input("Escriba frase a usar: ")
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A", "E", "I", "O", "U"]:
            continue
        else:
           cvoc = cvoc + 1
print("""Cantidad vocales:{}""".format(cvoc))

def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)
oracion = input('Escriba una oracion: ')
vocales(oracion.lower())