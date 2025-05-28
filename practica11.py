# EJERCICIO 2:

"""
Construir un programa que permita gestionar un programa simple de ventas para una fonda,
que presente al usuario los siguientes productos:

1. Empanada de pino: 2000

2. Empanada de queso: 1500

3. Choripan: 2500

4. Terremoto: 1000

Por su compra de más de 10000, recibe un descuento del 25%.
Por su compra mayor a 20000, recibe un decsuento del 40%
Por su compra mayor a los precios anteriores, sus entradas son gratis.
"""
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
