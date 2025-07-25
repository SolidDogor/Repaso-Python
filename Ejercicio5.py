#Escribe un programa que pida al usuario un número entero positivo. 
#Luego, calcula la suma de todos los números pares desde 1 hasta ese número (inclusive).

numero = int(input("Ingrese un numero a continuacion: "))
suma = 0
for i in range(numero):
    if (i % 2 == 0):
        suma += i

print("La suma de los numeros pares desde 0 hasta ", numero, " es: ", suma)