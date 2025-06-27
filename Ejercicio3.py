#Declaración de funciones
def pedir_numeros():
    cantidad = int(input("Cuantos numeros vas a ingresar? "))
    numeros = []

    for i in range(cantidad):
        num = int(input(f"Ingrese el numero #{i + 1}: "))
        numeros.append(num)

    return numeros

def max(lista):
    max = lista[0]
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

def min(lista):
    min = lista[0]
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min

# Uso de las funciones
numeros_usuario = pedir_numeros()
max = max(numeros_usuario)
min = min(numeros_usuario)
print("El mayor numero es ", max, " y el menor numero es ", min)