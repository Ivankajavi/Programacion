"""
with open ("datos.txt","w") as archivo:
    archivo.write("Nombre : Maria \n")
    archivo.write("Edad : 10 \n")
    archivo.write("carrera : ing \n") 

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileExistsError as error:
    print("El archivo no existe", error)
else:
    print("Archivo exitoso")
finally:
    print("Gracias por usar el programa")


Los dueños del vivero san joaquin necesitan realizar un programa en python
y para ello cuenta su talento como desarrolladores, cuyo programa
les va a corroborar el inventario de planta y las ventas
a continuacion los 10 productos mas vendidos:
1- Rosas blancas: excelente para esta primavera $2.000
2- Planta de navidad: para recordar el milagro de la navidad $5.000
3- Orquídea: planta parasitaria muy bella, sobrevive de otras plantas $3.000
4- Copihue: tradicional de la región $10.000
5- Rosas rojas: excelente eleccion para el 14F $7.000

Genera un archivo txt que almacene tus primera 5 plantas en tu 
inventario y que pueda quedar abierto para almacenar infinitamente
"""

with open ("datos.txt","w") as archivo:
    archivo.write("Rosas blancas $2.000  \n")
    archivo.write("Planta de navidad $5.000 \n")
    archivo.write("Orquidea $3.000  \n") 
    archivo.write("Copihue $10.000 \n")
    archivo.write("Rosas rojas $7.000 \n")
    