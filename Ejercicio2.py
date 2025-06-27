#Declaración de funciones
def pedir_numeros():
    cantidad = int(input("Cuantos numeros vas a ingresar? "))
    numeros = []

    for i in range(cantidad):
        num = int(input(f"Ingrese el numero #{i + 1}: "))
        numeros.append(num)

    return numeros

def buscar_numero(lista, num):
    encontrado = False
    for i in range(len(lista)):
        if lista[i] == num:
            print(f"Se encontró una instancia del número en la posición {i + 1}")
            encontrado = True

    if not encontrado:
        print("No se encontró el número.")

# Uso de las funciones
numeros_usuario = pedir_numeros()
numero = int(input("Ingrese el numero a buscar: "))
buscar_numero(numeros_usuario, numero)