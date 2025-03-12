import re

fichero = "clientes.txt"

# Pedimos el nombre a buscar al usuario
nombre = input("Introduzca los primeros caracteres del nombre a buscar: ")

# Leemos el contenido del fichero y lo guardamos en una variable
with open(fichero, "r", encoding="utf-8") as fichero:
    contenido = fichero.read()
fichero.close

# Buscamos la coincidencia con expresiones regulares
# Preparamos el patrón con el texto a buscar
# Si lo encontramos, buscamos también las tres líneas siguientes (apellido1, apellido2 y edad)
patron = r"Nombre:\W+\b%s\w+\b\n[^\r\n]+\n[^\r\n]+\n[^\r\n]+" % nombre
# Usamos findall para buscar todas las coincidencias en todo el fichero
# Con el flag re.IGNORECASE para que no tenga en cuenta mayúsculas/minúsculas
resultado = re.findall(patron, contenido, re.IGNORECASE)
if resultado != None and resultado != []:
    print("Los resultados obtenidos son los siguientes:")
    for linea in resultado:
        print(linea)    
else:
    print("No se han encontrado coincidencias")