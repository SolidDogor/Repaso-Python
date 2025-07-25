#Desarrolla un programa que genere una contraseña aleatoria simple. 
#El usuario debe especificar la longitud deseada de la contraseña. La contraseña debe contener una mezcla de:
#Letras minúsculas
#Letras mayúsculas
#Dígitos (0-9)

import random

def generar_password(longitud):
    contrasena = []
    cantidadGrupo = 0
    mod = 0
    # Conjuntos de caracteres
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
            
    # Se busca que haya la misma cantidad de tipo de caracter si es que la cantidad es múltiplo de 3
    cantidadGrupo = int(longitud / 3)
    mod = longitud % 3
            
    cantMayus = cantidadGrupo
    cantMinus = cantidadGrupo
    cantNum = cantidadGrupo

    if mod >= 1:
        cantMayus += 1

    if mod == 2:
        cantNum += 1

    # Agregando la cantidad equitativa de caracteres a la contraseña
    for i in range(cantMayus):
        contrasena.append((random.choice(mayusculas)))

    for i in range(cantMinus):
        contrasena.append((random.choice(minusculas)))

    for i in range(cantNum):
        contrasena.append((random.choice(numeros)))

    # Intercambiando caracteres de manera al azar
    random.shuffle(contrasena)

    # Unimos los caracteres para formar la contraseña final
    contrasena_final = "".join(contrasena)
    return contrasena_final

# --- Parte principal del programa ---
print("Bienvenido al generador de claves!")
while True:
    try:
        cantCar_str = input("Ingrese la cantidad de digitos que quiere que su clave tenga (mínimo 1): ")
        cantidadCaracteres = int(cantCar_str)
        if cantidadCaracteres < 1:
            print("Por favor, ingrese un número positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

clave_generada = generar_password(cantidadCaracteres)
print(f"Tu clave generada es: {clave_generada}")


