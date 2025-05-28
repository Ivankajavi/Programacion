# EJERCICIO TIPO EXAMEN 1:
"""
Se necesita desarrollar un programa que permita calcular el área de varios triándulos.
Para esto, se le va a solitar al usuario cuántos triángulos desea procesar. 
Luego, por cada triángulo, se debe ingresar la base y la altura, ambos positivos y reales.
El área del triángulo se calcula midiendo la base x la altura / 2.
Si su usuario ingresa un valor inválido, se debe mostrar un mensaje de error.
"""
try:
    cantidad = int(input("Cantidad de triángulos: "))
    
    while cantidad > 0:
        try:
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            
            if base > 0 and altura > 0:
                print(f"Área: {base * altura / 2}")
                cantidad -= 1
            else:
                print("Los valores deben ser positivos.")
        except:
            print("Entrada inválida, usa números.")
except:
    print("Entrada inválida, usa un número entero.")
