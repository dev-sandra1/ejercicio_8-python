#Contar palabras únicas en una lista Escribe un programa que reciba una lista de palabras e imprima cuántas veces aparece cada palabra (sin contar duplicados).

palabras = input("Introduce una lista de palabras separadas por espacios: ").split()
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Frecuencia de las palabras:")
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")

