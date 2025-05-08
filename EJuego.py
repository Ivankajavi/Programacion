"""
Desarrolla un programa en Python que permita ingresar
2 números enteros que indiquen un rango numérico. 
El primer valor debe ser menor que el segundo. 
El programa generará un número aleatorio dentro de ese rango. 
Luego, el usuario intentará adivinar el número generado en 3 intentos.

Si el usuario adivina en el primer intento, el programa mostrará el mensaje: "Felicitaciones, adivinaste en el primer intento."
Si no acierta en el primer intento, el programa indicará si el número es mayor o menor que el intento del usuario.
En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: "Perdiste, el número era [número]."

"""

import random

num1, num2 = int(input("Primer número: ")), int(input("Segundo número: "))

if num1 < num2:
    num = random.randint(num1, num2)

    for cada in range(3):
        if int(input("Adivina el número: ")) == num:
            print("¡Felicitaciones!")
            break
    else:
        print(f"Perdiste, el número era {num}")
else:
    print("El primer número debe ser menor que el segundo.")

