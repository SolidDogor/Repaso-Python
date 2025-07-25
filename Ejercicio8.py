#Crea un programa interactivo para una lista de la compra. El programa debe permitir al usuario:
#1.- Añadir un producto a la lista.
#2.- Ver la lista completa.
#3.- Marcar un producto como comprado (eliminándolo de la lista o moviéndolo a otra lista de "comprados", 
#     tú decides la implementación).
#4.- Salir del programa.

def lista_de_la_compra():
    """
    Programa interactivo para gestionar una lista de compras.
    Permite añadir, ver y marcar productos como comprados.
    """
    productos = [] # Aquí almacenaremos los productos de nuestra lista

    print("--- ¡Bienvenido a tu Lista de la Compra! ---")

    while True:
        # Mostramos las opciones al usuario
        print("\n--- Menú ---")
        print("1. Añadir producto")
        print("2. Ver lista de compras")
        print("3. Marcar producto como comprado")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            # Añadir producto
            producto_nuevo = input("¿Qué producto quieres añadir? ").strip() # .strip() para quitar espacios extra
            if producto_nuevo: # Aseguramos que el usuario no ingrese una cadena vacía
                productos.append(producto_nuevo.capitalize()) # .capitalize() para que la primera letra sea mayúscula
                print(f"'{producto_nuevo.capitalize()}' ha sido añadido a la lista.")
            else:
                print("No puedes añadir un producto vacío.")

        elif opcion == '2':
            # Ver lista de compras
            if not productos: # Verificamos si la lista está vacía
                print("Tu lista de compras está vacía.")
            else:
                print("\n--- Tu Lista de Compras ---")
                for i, producto in enumerate(productos):
                    # enumerate nos da el índice y el valor, útil para mostrar números de lista
                    print(f"{i + 1}. {producto}") # i + 1 para que empiece en 1 y no en 0

        elif opcion == '3':
            # Marcar producto como comprado (eliminarlo de la lista)
            if not productos:
                print("Tu lista de compras está vacía. Nada que marcar como comprado.")
                continue # Volver al inicio del bucle

            print("\n--- Productos para Marcar como Comprados ---")
            for i, producto in enumerate(productos):
                print(f"{i + 1}. {producto}")

            try:
                # Pedimos al usuario el número del producto a eliminar
                num_a_eliminar = int(input("Introduce el número del producto a marcar como comprado: "))
                # Ajustamos el número a un índice de lista (restamos 1)
                indice_a_eliminar = num_a_eliminar - 1

                # Verificamos que el índice sea válido
                if 0 <= indice_a_eliminar < len(productos):
                    producto_eliminado = productos.pop(indice_a_eliminar) # .pop() elimina y devuelve el elemento
                    print(f"'{producto_eliminado}' ha sido marcado como comprado y eliminado de la lista.")
                else:
                    print("Número de producto inválido. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, introduce un número.")

        elif opcion == '4':
            # Salir del programa
            print("¡Gracias por usar tu Lista de la Compra! ¡Hasta pronto!")
            break # Salir del bucle while y terminar el programa

        else:
            # Opción inválida
            print("Opción no válida. Por favor, elige un número del 1 al 4.")

# Llamamos a la función para ejecutar el programa
lista_de_la_compra()