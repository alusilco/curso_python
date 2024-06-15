#MAnejo de ficheros de texto
# Ficheros de texto plano => .txt
# Ficheros de texto con formato
#       CSV => usados muchos en ML
#       JSON => usados mucho como intercambio de informacion semiestructurada entre sistemas

#Manejos de texto
#Todo parte de una funcion que es open()
# OBJETO = open(RUTA_FICHERO, MODO_FICHERO)
# RUTA_FICHERO => donde va a estar guardado el fichero
# MODO_FICHERO => un parametro que indica como lo vamos a abrir
#       - w => apertura en modo escritura, crea el fichero y en que caso de que exista lo sobrescribe
#       - r => apertura en modo lectura
#       - a => apetura en modo append, es decir para añadir contenidos a un ficheor existente
fichero = open("test.txt","w")

#Los fichero cuando acabeis de trabajar con ellos se deben cerrar
fichero.close()

print("*******************************************************")
print("*************** Añadir contenido **********************")
fichero = open("test.txt","w")
#para escribir contenido en un fichero de texto tenemos varios metodos
fichero.write("Hola Mundo\n")
fichero.write("Adios Mundo")

fichero.close()

print("*******************************************************")
print("*************** Leer contenido **********************")
fichero = open("test.txt","r")
#para leer contenido en un fichero de texto tenemos varios metodos
print(fichero.read())

fichero.close()

print("*******************************************************")
print("*************** Leer contenido con un bucle **********************")
fichero = open("test.txt","r")
#para leer contenido en un fichero de texto tenemos varios metodos
for linea in fichero:
    print(linea, end="")

fichero.close()


#Tenemos fichero de varios formatos, el primero es json
#python nos da un modulo que ya viene instalado
import json

#Un json es una estructura de texto
#sintaxis esta basado en clave:valor
#En python esto es un diccionario que equilalente a un json de JS
alumno = {
    "nombre" : "James",
    "apellido" : "Bond"
}

print(alumno["nombre"])

#Podemos convertirlo a un json superfacil
alumno_json = json.dumps(alumno)
print("Tipo de Alumno",type(alumno))
print("Tipo del JSON del alumno", type(alumno_json))
fichero = open("datos.json","w")
fichero.write(alumno_json)
fichero.close()