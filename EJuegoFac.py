"""
Realiza en Python un programa que pueda generar 1 numero aleatorio
dentro de un rango definido por el usuario y ajustándolo
divitiéndola por 4, luego el usuario deberia adivinar numero en un
máximo de 3 intentos:

Condiciones del juego:

1-Ingresos de datos:

A-el usuario Ingresa 2 números enteros
B-el primer numero debe ser menor al segundo

2-generación de números aleatorios:

A-Se elije un numero aleatorio dentro del rango ingresado.
B-el numero se ajusta dividiéndolo entre 4 y 
redondeándolo al múltiplo de 4 mas cercano.

3-Intentos del Usuario:

A-primer intento si el usuario acierta un felicitaciones 
B-Segundo intento si no acierta, se indica si el numero es mayor menor
C-Tercer Intento Si no acierta nuevamente se le da otra pista
D-Resultado Final Si no acierta en los 3 intentos
 el programa nuestra el mensaje "perdiste el numero era:"
 
"""
import random

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 < num2:
    num = round(random.randint(num1, num2) / 4) * 4
    intento = int(input("Adivina el número: "))
    
    if intento == num:
        print("¡Felicitaciones!")
    else:
        print("Fallaste. El número era:", num)
else:
    print("El primer número debe ser menor al segundo.")
