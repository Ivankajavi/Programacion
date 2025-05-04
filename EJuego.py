#Desarrolla un programa en Python que permita generar un número aleatorio dentro de un rango definido por el usuario y ajustarlo dividiéndolo por 4. Luego, el usuario deberá adivinar el número en un máximo de tres intentos.

#Condiciones del juego:

#Ingreso de datos:
#El usuario ingresa dos números enteros que representan el rango numérico.
#El primer número debe ser menor que el segundo.
#Generación del número aleatorio:
#Se elige un número aleatorio dentro del rango ingresado.
#El número se ajusta dividiéndolo por 4 y redondeándolo al múltiplo de 4 más cercano.
#Intentos del usuario:
#Primer intento: Si el usuario acierta, se muestra el mensaje: "Felicitaciones, adivinaste en el primer intento."
#Segundo intento: Si el usuario no acierta, se le indica si el número es mayor o menor.
#Tercer intento: Si no acierta nuevamente, se le vuelve a dar una pista.
#Resultado final: Si no acierta en los tres intentos, el programa muestra el mensaje: "Perdiste, el número era [número]."

import random

inicio = int(input("Ingresa el número menor del rango: "))
fin = int(input("Ingresa el número mayor del rango: "))

if inicio >= fin:
    print("El primer número debe ser menor que el segundo.")
else:
    numero = random.randint(inicio, fin)

    if numero % 4 != 0:
        while numero % 4 != 0:
            numero -= 1

    for intento in range(1, 4):
        adivina = int(input("Adivina el número: "))

        if adivina == numero:
            if intento == 1:
                print("¡Felicitaciones, adivinaste en el primer intento!")
            else:
                print("¡Bien hecho, adivinaste!")
            print("Fin del juego.")
            exit()

        elif adivina < numero:
            print("Pista: el número es mayor.")
        else:
            print("Pista: el número es menor.")

    print("Perdiste, el número era", numero)
