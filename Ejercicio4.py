#Declaración de funciones
def pedir_numeros():
    cantidad = int(input("Cuantos numeros vas a ingresar? "))
    numeros = []

    for i in range(cantidad):
        num = int(input(f"Ingrese el numero #{i + 1}: "))
        numeros.append(num)

    return numeros

def calcular_promedio(lista):
    suma = 0
    cantidad = 0
    for i in range(len(lista)):
        suma += lista[i]

    return suma / len(lista)


def mayores_al_promedio(lista, promedio):
    cantidad = 0
    for i in range(len(lista)):
        if lista[i] > promedio:
            cantidad += 1

    return cantidad


# Uso de las funciones
numeros_usuario = pedir_numeros()
promedio = calcular_promedio(numeros_usuario)
print(promedio)
mayor_promedio = mayores_al_promedio(numeros_usuario, promedio)
print("La cantidad de numeros mayores al promedio son: ", mayor_promedio)