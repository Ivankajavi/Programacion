# La tienda falabella necesita desarrollar un programa, para saber cuantos pts tiene acumulado cada usuario
# Por cada 1.000 pesos que realice una compra un usuario recibe 10 pts
# Cuando un usuario alcanza la puntuacion de 1000 pts esta en el nivel premium, por lo tanto recibe un dscto del 25%
# Cuando un usuario alcanza la puntuacion de 500 pts esta en el nivel oro, por lo tanto recibe un dcto del 10%
# Cuando un usuario alcanza la puntuacion de 250 pts, no recibe dcto pero si premios como audifonos, relojes y mucho mas

# Perfiles de usuarios:

# Marco tiene 1500 pts a canjear, ¿que niveles les corresponde?.
# Jose luis tiene 2500 pts, ¿que niveles les corresponde?
# Sebastian solo tiene 300 pts, ¿que niveles les corresponde?

# Mostrar en pantalla la informacion (nivel en que se encuentra) y que al final le de un msj para seguir usando los pts de la tienda falabella


def mostrar_nivel(nombre, puntos): # Función para mostrar el nivel según los puntos
    print(f"Usuario: {nombre}")
    print(f"Puntos: {puntos}")

    if puntos >= 1000:
        print("Nivel: PREMIUM, tienes un descuento del 25%")
    elif puntos >= 500:
        print("Nivel: ORO, tienes un descuento del 10%")
    elif puntos >= 250:
        print("Nivel: STANDAR, los premios que puedes optar son: Audífonos, relojes y más")
    else:
        print("Aun no tienes nivel, ¡Sigue acumulando puntos!")

    print("¡Sigue usando tus puntos en Falabella!")

# Datos de los usuarios
mostrar_nivel("Marco", 1500)
mostrar_nivel("Jose Luis", 2500)
mostrar_nivel("Sebastian", 300)