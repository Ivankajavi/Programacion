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

#el supermercado Acuenta necesita desarrollar un software en python
#que le permita llevar la merma y las devoluciones, dentro de la merma
#debemos considerar la perdida del 25% del pollo
#si el dia miercoles recibimos 1000kg de pollo, el dia jueves 1200kg de pollo
# y el sabado solo 500kg de pollo, consideremos la merma de esa semana
#realicemos una lista de 10 productos, solo se permitira regresar 3 productos
#y no deben superar el 20% el total de productos. Mostraremos en pantalla los productos que cumplen
#con el 20%, seguido de la merma. hay que dar la opcion de salir del programa. 