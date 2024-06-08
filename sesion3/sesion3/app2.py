# recorridos

nota_obtenida = "Notable"

#recorrer la coleccion
# estructuras iterativas

#for caracter in nota_obtenida:
#    if caracter != 'e': 
#        print(caracter, end="")


# tupla
dato = (1,2,3,4)
print(type(dato))

print(dato[0], dato[-1])

palabras = ('hola', 1, 'adios', 'python', 'idfo', 'android')

# por cada palabra de la tupla palabras, mostrar la longitud de cada una de ellas
#for palabra in palabras:
#    print(f"Longitud:{len(palabra)}")

#print(palabras[0])
#print(palabras[-1])

#palabras[0] = 'android'

def procesar_data(data: tuple): # type hinting
    for item in data:
        if type(item) != int and type(item) != float :
            print(f"Longitud:{len(item)}")

procesar_data(palabras)  #invocacion
    