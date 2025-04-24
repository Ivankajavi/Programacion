# La empresa certifika necesita nuestra ayuda, y nos solicita
# Realizar un programa que cumpla con las siguientes condiciones:
# Alumnos con calificaciones mayor a 6 recibiran un dcto en su matricula de un 20%
# Alumnos con calificaciones mayores a 5 recibiran un dcto en su matricula de un 15%
# Alumnos con calificaciones mayores a 4 recibiran un dcto en su matricula de un 10%
# Y por ultimo los que no cumplan con las notas los invitamos a seguir esforzándose.

# Pedimos la nota al usuario
nota = float(input("Ingresa tu nota: "))

# Verificamos el descuento según la nota
if nota > 6:
    print("¡Felicidades! Tienes un 20% de descuento en tu matrícula.")
elif nota > 5:
    print("¡Muy bien! Tienes un 15% de descuento en tu matrícula.")
elif nota > 4:
    print("¡Bien hecho! Tienes un 10% de descuento en tu matrícula.")
else:
    print("Sigue esforzándote, ¡tú puedes mejorar!")