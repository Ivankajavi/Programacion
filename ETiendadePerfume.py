#tienda de perfumes blogger
#el representante de ventas de la tienda necesita organizar el formulario de ventas
#el piensa, que representando el siguiente formulario
#podria mejorar sus ventas ya que el formulario tiene 10 items para atender
#a continuacion los cargos que desea implementar:

#numero de boleta/factura
#Rut
#nombre cliente
#Productos del pedido
#10 productos dentro del inventario:
a = """
♥ Perfume damas♥ :
1. Perfume organza
2. Perfume katy perry
3. Mañana fresca
4. La mejor noche
5. Sueño intrusivo

♥ Perfume hombre ♥ :
6. Ahora si voy  
7. Antonio bandera
8. Lacoste
9. Hugo boss
10. a que te quito el sueño
"""
#todos los de 50ML estan a $10.000
#todos los de 100ML estan a $18.000
#añadir el pedido, sacar el total y sacar iva

#Precios
precio_50ml = 10000
precio_100ml = 18000


print("Bienvenido a la tienda Blogger")

nombre = input("Dime tu nombre: ")
rut = input("Dime tu rut sin guión: ")
boleta = input("Número de boleta/factura: ")


print("Selecciona el perfume a escoger")
print(a)
perfume_num = input("Ingresa el número del perfume que escogiste (1 al 10): ")


print("El perfume que escogiste tiene 2 formatos, ¿Cuál deseas escoger?")
print("Opción 1: 50 ML $10.000")
print("Opción 2: 100 ML $18.000")
formato = input("Escribe 1 o 2: ")


if formato == "1":
    total = precio_50ml
    tamaño = "50 ML"
elif formato == "2":
    total = precio_100ml
    tamaño = "100 ML"
else:
    print("Opción inválida. Se tomará como 50 ML por defecto.")
    total = precio_50ml
    tamaño = "50 ML"


iva = int(total * 0.19)
total_final = total + iva


print("RESUMEN DE COMPRA")
print(f"Boleta N°: {boleta}")
print(f"Nombre cliente: {nombre}")
print(f"RUT: {rut}")
print(f"Perfume número: {perfume_num} - Tamaño: {tamaño}")
print(f"Subtotal: ${total}")
print(f"IVA (19%): ${iva}")
print(f"Total a pagar: ${total_final}")
print("Gracias por tu compra ¡Vuelve pronto!")



