# mi_Tupla = ("Banana", "Manzana", "Cereza")
# print (mi_Tupla[0])

# Lista de supermercado
# Mensaje de bienvenida 
# agregar 2 productos, msj de añadir el producto
# solicitar modificar el producto
# como eliminar algun poroducto
# imprimir lista resultado (print)

import random
print("Bienvenido")
Agrega = input("Agrega tu producto ")
list = ("pera", "manzana", Agrega)
print("tu lista es: ", list)
NoDisponible = random.choice(list)
print("por favor modifique su compra, ", NoDisponible, "no esta disponible")
print("Desea eliminar ", NoDisponible, "?")



