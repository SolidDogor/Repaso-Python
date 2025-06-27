#Declaración de funciones
def pedir_numeros():
    cantidad = int(input("Cuantos numeros vas a ingresar? "))
    numeros = []

    for i in range(cantidad):
        num = int(input(f"Ingrese el numero #{i + 1}: "))
        numeros.append(num)

    return numeros

def mostrar_lista(lista):
    print("Los numeros ingresados son:")
    for numero in lista:
        print("-", numero)

def calcular_promedio(lista):
    suma = sum(lista)
    return suma / len(lista)

# Uso de las funciones
numeros_usuario = pedir_numeros()
mostrar_lista(numeros_usuario)
prom = calcular_promedio(numeros_usuario)
print(f"El promedio de los numeros es: {prom}")
