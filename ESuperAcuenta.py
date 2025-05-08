
"""
El supermercado Acuenta necesita desarrollar un software en python
que le permita llevar la merma y las devoluciones, dentro de la merma
debemos considerar la perdida del 25% de pollo, si el dia miercoles recibimos 1000kg de pollo, el dia jueves 1200kg de pollo
y el sabado solo 500kg de pollo, consideremos la merma de esa semana
realicemos una lista de 10 productos, solo se permitira regresar 3 productos
y no deben superar el 20% el total de productos. Mostraremos en pantalla los productos que cumplen
con el 20%, seguido de la merma. hay que dar la opcion de salir del programa. 

"""

pollo = 1000 + 1200 + 500
print("Merma:", pollo * 0.25, "kg")

p = {"leche": 50, "arroz": 60, "pan": 80, "huevos": 100, "aceite": 40,
     "jabon": 30, "queso": 20, "azucar": 70, "harina": 60, "detergente": 35}

for i in range(3):
    prod = input("Producto (o salir): ")
    if prod == "salir":
        break
    cant = int(input("Cantidad: "))
    if prod in p:
        if cant <= p[prod]*0.2:
            print("Aceptado")
        else:
            print("Excede 20%")
    else:
        print("No existe")
