# Lista de supermercado:
# Mensaje de bienvenida 
# agregar 2 productos, msj de añadir el producto
# solicitar modificar el producto
# como eliminar algun poroducto
# imprimir lista resultado


# Mensaje de bienvenida
print("¡Bienvenido a tu lista de supermercado!")

# Lista vacía
lista = []

# Agregar 2 productos
producto1 = input("Ingresa el primer producto: ")
lista.append(producto1)
print(f"Producto '{producto1}' añadido.")

producto2 = input("Ingresa el segundo producto: ")
lista.append(producto2)
print(f"Producto '{producto2}' añadido.")

# Modificar un producto
modificar = input("¿Qué producto quieres modificar? ")
if modificar in lista:
    nuevo = input("¿Por qué producto lo quieres cambiar? ")
    index = lista.index(modificar)
    lista[index] = nuevo
    print(f"Producto '{modificar}' cambiado por '{nuevo}'.")
else:
    print("Ese producto no está en la lista.")

# Eliminar un producto
eliminar = input("¿Qué producto quieres eliminar? ")
if eliminar in lista:
    lista.remove(eliminar)
    print(f"Producto '{eliminar}' eliminado.")
else:
    print("Ese producto no está en la lista.")

# Mostrar la lista final
print("Tu lista final de supermercado es:")
print(lista)

