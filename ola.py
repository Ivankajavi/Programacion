"""
#MENU

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

#VENTA SIMPLE

pino = int(input("Empanadas de pino: ")) * 2000
queso = int(input("Empanadas de queso: ")) * 1500
choripan = int(input("Choripanes: ")) * 2500
terremoto = int(input("Terremotos: ")) * 1000

total = pino + queso + choripan + terremoto

if total > 20000:
    print(f"Total: {total} - Descuento 40%. Entradas gratis.")
elif total > 10000:
    print(f"Total con descuento 25%: {total * 0.75}")
else:
    print(f"Total a pagar: {total}")  

#TRIANGULO

print("Calculadora de área de triángulos")

triangulos = int(input("¿Cuantos Triangulos desea calcular?: "))
for i in range(triangulos):
    try:
        base = float(input(f"Ingrese la base del triángulo: "))
        altura = float(input(f"Ingrese la altura del triángulo: "))

        if base > 0 and altura > 0:
            area = (base * altura) / 2
            print(f"El área del triángulo es: {area}")
        else:
            print("La base y la altura deben ser mayores que cero. Intente de nuevo.")
    except ValueError:
        print("Error. Por favor, ingrese un número válido para la base y la altura.")
    
#PACIENTES

pacientes = []

while True:
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
    motivo = input("Motivo de consulta: ")

    pacientes += [{"Nombre": nombre, "Edad": edad, "Motivo": motivo}]

    continuar = input("¿Registrar otro paciente? (si/no): ")
    if continuar != "si":
        break

print("Registro de pacientes:")
for p in pacientes:
    print(p["Nombre"], ",", p["Edad"], "años, Motivo:", p["Motivo"])
"""
print("Bivenido a las fondas de los programadores mas basados del DUOC")
print("A continuacion nuestro menú de productos")
print("**")
print("1.-Empanada de pino $2000")
print("2.-Empanada de queso $1500")
print("3.-Choripan $2500")
print("4.-Terremoto $1000")

cantidad_productos=0
total=0

while True:
    try:
        print("Por favor, si no desea un producto, ingrese 0")
        empanada_pino = int(input("Ingrese la cantidad de E. pino que desea: "))
        empanada_queso = int(input("Ingrese la cantidad de E. queso que desea: "))
        choripan = int(input("Ingrese la cantidad de choripan que desea: "))
        terremoto = int(input("Ingrese la cantidad de terremoto que desea: "))
        if empanada_pino >= 0 and empanada_queso >=0 and choripan >=0 and terremoto >=0:
            print("Compra ingresada con exito")
            break
        else:
            print("Ingrese un numero positivo")
            continue
    except ValueError:
        print("Ingrese un caracter valido")
        continue

cantidad_productos += empanada_pino + empanada_queso + choripan + terremoto
total += empanada_pino 2000
total += empanada_queso 1500
total += choripan 2500
total += terremoto 1000

if total > 20000:
    descuento = total
    total_descuento = total - descuento
    print("Por tu compra, recibiste un descuento del 40%")
elif total > 10000:
    descuento = total * 0.25
    total_descuento = total - descuento
    print("Por tu compra recibiste un descuento del 25%")
else:
    print("Gracias por tu compra. No recibió descuento")

print(f"Tu cantidad de productos fue {cantidad_productos}")
print(f"Tu total a pagar sin descuento es de {total}")
print(f"Tu total a pagar con descuento es {total_descuento}")