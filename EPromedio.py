# Solicita las notas al usuario
nota1 = float(input("Ingresa tu primera nota: "))
nota2 = float(input("Ingresa tu segunda nota: "))
nota3 = float(input("Ingresa tu tercera nota: "))

# Calcula el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Mensaje según el promedio
if promedio >= 4.0:
    print("¡Aprobaste!")
else:
    print("Reprobaste.")

print("Tu promedio es:", round(promedio, 2))
