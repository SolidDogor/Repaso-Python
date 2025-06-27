#Declaración de funciones
def pedir_numeros():
    cantidad = int(input("Cuantos numeros vas a ingresar? "))
    numeros = []

    print("ADVERTENCIA! Solo se guardaran numeros pares")
    for i in range(cantidad):
        num = int(input(f"Ingrese el numero #{i + 1}: "))
        if(num % 2 == 0):
            numeros.append(num)
        else:
            print("No se guardara este numero.")

    return numeros

def mostrar_lista(lista):
    print("Los numeros ingresados son:")
    for numero in lista:
        print("-", numero)

# Uso de las funciones
numeros_usuario = pedir_numeros()
mostrar_lista(numeros_usuario)