# EJERCICIO TIPO EXAMEN 2:
"""
Construya un programa que permita gestionar un sistema simple de venta 
de entradas para un cine, por medio de un menú.

El programa debe mostrar un menú de opciones, que permita dar la bienvenida al usuario,
mostrar cuántas entradas quedan, comprar una cantidad de entradas según la elección del usuario,
preguntar disponibilidad de la cantidad de entradas y dar salida al menú, con un mensaje de despedida.
"""

entradas = 100

while True:
    print("\n1. Ver entradas\n2. Comprar\n3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Entradas disponibles: {entradas}")
    elif opcion == "2":
        cantidad = int(input("Cantidad a comprar: "))
        if cantidad > entradas:
            print("No hay suficientes entradas.")
        else:
            entradas -= cantidad
            print(f"Compra realizada. Quedan {entradas} entradas.")
    elif opcion == "3":
        print("¡Gracias por tu visita!")
        break
    else:
        print("Opción no válida.")

