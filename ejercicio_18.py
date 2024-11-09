#Contar vocales en una frase Escribe un programa que cuente cuántas 
# vocales (tanto mayúsculas como minúsculas) hay en una frase introducida por el usuario.

frase = input("Introduce una frase: ").lower()
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print(f"El número de vocales en la frase es: {contador}")
