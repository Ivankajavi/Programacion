# EJERCICIO 1:
"""
Construir un programa que permita registrar los libros prestados 
en una biblioteca. Y contar cuáles fueron prestados por más de 15 días.

1. Ingresar la cantidad de libros a registrar. [Número Entero]
2. Para cada libro se debe pedir el título del libro y la cantidad de días a prestar.
3. El programa debe indicar si el libro tiene un préstamo de 15 o más días, o préstamo de menos días.
4. Finalmente, se deben mostrar cuántos libros tienen préstamo de 15 o más días, y cuántos no.
5. Todos los números ingresados deben ser verificados con "try" y "except".
"""

try:
    cantidad = int(input("Cantidad de libros: "))
    mas_15, menos_15 = 0, 0

    while cantidad > 0:
        try:
            titulo = input("Título del libro: ")
            dias = int(input("Días de préstamo: "))

            if dias >= 15:
                mas_15 += 1
            else:
                menos_15 += 1
            
            cantidad -= 1
        except:
            print("Entrada inválida, usa un número.")

    print(f"Libros con préstamo ≥15 días: {mas_15}")
    print(f"Libros con préstamo <15 días: {menos_15}")

except:
    print("Entrada inválida, usa un número entero.")
