# linea1
# linea2
# linea3

nombre_completo = 'Ricardo Jaume' # la variable es de tipo cadena o string (str)
nombre_completo2 = 'Pedro López' # la variable es de tipo cadena o string (str)
nombre_completo3 = 'Maria Gomez' # la variable es de tipo cadena o string (str)
nombre_completo4 = 'Monica Plana' # la variable es de tipo cadena o string (str)
nombre_completo5 = 'Luis García' # la variable es de tipo cadena o string (str)
nota_certificacion = 9.5 # tipo decimal (float)

print(nombre_completo) # imprime valor de la variable
print(type(nombre_completo)) # imprime el tipo de la variable

print('-' * 60)

# hacer lo mismo pero con la nota de certificacion
print(nota_certificacion)
print(type(nota_certificacion))

# Crear la cadena completa: Hola, me llamo X y he sacado una nota de Y
print(1, 5, 8, 10, 'Hola', sep="-")
print(nombre_completo, nota_certificacion, sep=":") # sep es un parámetro de la función print

#print('Hola, me llamo', nombre_completo, 'y he sacado una nota de', nota_certificacion)
#print('Hola, me llamo', nombre_completo2, 'y he sacado una nota de', nota_certificacion)
#print('Hola, me llamo', nombre_completo3, 'y he sacado una nota de', nota_certificacion)
#print('Hola, me llamo', nombre_completo4, 'y he sacado una nota de', nota_certificacion)
#print('Hola, me llamo', nombre_completo5, 'y he sacado una nota de', nota_certificacion)

# DRY -> Don't Repeat Yourself
# Usando funciones...

def saludar(nombre,  nota): 
    print('Hola, me llamo', nombre, 'y he sacado una nota de', nota)

saludar(nombre_completo, nota_certificacion) # invocación de una función
saludar(nombre_completo2, nota_certificacion)
saludar(nombre_completo3, nota_certificacion)
saludar(nombre_completo4, nota_certificacion)
saludar(nombre_completo5, nota_certificacion)








