try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileExistsError as error:
    print("El archivo no existe", error)
else:
    print("Archivo exitoso")
finally:
    print("Gracias por usar el programa")