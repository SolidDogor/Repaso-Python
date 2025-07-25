#Pídele al usuario que ingrese una cadena de texto. 
#Tu programa debe contar y mostrar cuántas vocales (a, e, i, o, u, sin importar mayúsculas o minúsculas)
# hay en esa cadena.

cadena = input("Ingrese una cadena a continuacion: ")
cadena_minusculas = cadena.lower()
cantidadVocales = 0
vocales = "aeiou"

for caracter in cadena_minusculas:
    if caracter in vocales:
        cantidadVocales += 1

print(f"La cantidad de vocales (alternativa) en: '{cadena}' es: {cantidadVocales}")
