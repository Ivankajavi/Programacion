#Desarrolla un programa en Python que permita calcular el subsidio de gas según el quintil
#de ingresos al que pertenece la familia del solicitante y su condición laboral.

#Condiciones socioeconómicas:
#Quintil de ingresos: Hay 5 quintiles en total (1 = menores ingresos, 5 = mayores ingresos).
#Condición laboral: Se considera si la persona está desempleada o empleada
#1- desempleado $15.000
#2- empleado $10.000
#3- desempleado $8000
#4- empleado $6000
#5- cualquiera $1500

#Bonos Adicionales:
#Si el solicitante pertenece al Quintil 1 o 2, recibe un bono adicional de $2,000.
#Si además tiene más de 65 años, recibe un bono extra de $3,000.
#Desarrolla un programa en Python que permita generar un número aleatorio dentro de un rango definido por el usuario y ajustarlo dividiéndolo por 4. Luego, el usuario deberá adivinar el número en un máximo de tres intentos.

#Condiciones del juego:

#Ingreso de datos:
#El usuario ingresa dos números enteros que representan el rango numérico.
#El primer número debe ser menor que el segundo.
#Generación del número aleSatorio:
#Se elige un número aleatorio dentro del rango ingresado.
#El número se ajusta dividiéndolo por 4 y redondeándolo al múltiplo de 4 más cercano.
#Intentos del usuario:
#Primer intento: Si el usuario acierta, se muestra el mensaje: "Felicitaciones, adivinaste en el primer intento."
#Segundo intento: Si el usuario no acierta, se le indica si el número es mayor o menor.
#Tercer intento: Si no acierta nuevamente, se le vuelve a dar una pista.
#Resultado final: Si no acierta en los tres intentos, el programa muestra el mensaje: "Perdiste, el número era [número]."


quintil = int(input("Ingresa tu quintil: "))
condicion = input("ingresa tu condicion: ")
edad = int(input("Dime tu edad: "))

subsidio = 0
bono = 0

if quintil in (1, 2):
    if condicion == "desempleado":
        subsidio = 15000
    elif condicion == "empleado":
        subsidio = 10000
elif quintil == 3:
    if condicion == "desempleado":
        subsidio = 8000 
    elif condicion == "empleado":
        subsidio = 6000

if quintil in (1, 2):
    bono += 2000

if edad > 65:
    subsidio = 3000
    total = subsidio + bono

print("el subsidio total que te corresponde es: $", subsidio)
