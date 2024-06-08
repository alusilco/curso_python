
def obtener_caracter_por_indice(dato, indice):
    if indice >= 0 and indice < len(dato): 
        return dato[indice]
    else:
        return None

# declaracion e inicializacion de una variable
nombre = 'Pablo Lopez' # coleccion de caracteres


# invocacion d ela funcion
primer_caracter = obtener_caracter_por_indice(nombre, 20)

# print(type(nombre))

print(nombre[0]) # primer caracter
print(primer_caracter) # primer caracter

print(nombre[-1]) # ultimo caracter
print(nombre[-2]) # penultimo caracter

print("Data:", nombre[0:11:3]) # slicing

expresion = "1+7"
operandos = expresion[0:3:2]
print("Operandos:", operandos)

print(nombre[3:-2])
print(nombre[::-1])

# otras operaciones
dato_clima = "cielo nuboso".capitalize()
dato_clima = "cielo nuboso".upper() # lower()
print(dato_clima.isdigit()) # False
dato_clima = '12'
print(dato_clima.isdigit()) # True
print(dato_clima)

nombre_completo = "Maria Lopez Gimenez" #maria lopez gimenez
numero_veces_cadena_lo = nombre_completo.lower().count('lo')
if numero_veces_cadena_lo == 0:
    print("No hay apariciones de la cadena lo")
else:
    print(f"El numero de veces que aparece la cadena lo es de {numero_veces_cadena_lo}")


print(dato_clima.find('3'))

nombre_completo = "David Perez Almeida" 
# nombre = ??
# primer_apelido = ??

ESPACIO_BLANCO = ' '

nombre_pila = nombre_completo[0:nombre_completo.find(ESPACIO_BLANCO)]
cadena_restante = nombre_completo[nombre_completo.find(ESPACIO_BLANCO) + 1:]
pimer_apellido = cadena_restante[:cadena_restante.find(ESPACIO_BLANCO)]
segundo_apellido = cadena_restante[cadena_restante.find(ESPACIO_BLANCO) + 1:]  

print(f"El nombre de pila es {nombre_pila}.\nEl primer apellido es {pimer_apellido}.\nEl segundo apellido es {segundo_apellido}")

# estas operaciones de dado un nombre completo obtener su nombre_pila, primer apellido y su segundo apellido en forma de función
def obtener_nombre_apellido1_apellido2_usuario(nombre_completo: str):
    nombre_pila = nombre_completo[0:nombre_completo.find(ESPACIO_BLANCO)]
    cadena_restante = nombre_completo[nombre_completo.find(ESPACIO_BLANCO) + 1:]
    pimer_apellido = cadena_restante[:cadena_restante.find(ESPACIO_BLANCO)]
    segundo_apellido = cadena_restante[cadena_restante.find(ESPACIO_BLANCO) + 1:]  

    return nombre_pila, pimer_apellido, segundo_apellido # tupla

def obtener_nombre_apellido1_apellido2_usuario(nombre_completo: str, separador: str = ESPACIO_BLANCO):
    nombre_pila = nombre_completo[0:nombre_completo.find(separador)]
    cadena_restante = nombre_completo[nombre_completo.find(separador) + 1:]
    pimer_apellido = cadena_restante[:cadena_restante.find(separador)]
    segundo_apellido = cadena_restante[cadena_restante.find(separador) + 1:]  

    return nombre_pila, pimer_apellido, segundo_apellido # tupla

#nombre, p_apellido, s_apellido = obtener_nombre_apellido1_apellido2_usuario("Ricardo*Jaume*Albacar", "*")
#print(nombre, p_apellido, s_apellido)

def preguntar_nombre_completo():
    n_completo = input("Nombre completo?:")
    return n_completo

def preguntar_separador():
    sep = input("Separador?:")
    return sep

if __name__ == "__main__":

    # v1
    nombre_completo = preguntar_nombre_completo()
    separador = preguntar_separador()
    nombre, p_apellido, s_apellido = obtener_nombre_apellido1_apellido2_usuario(nombre_completo, separador)
    print(nombre, p_apellido, s_apellido)

    # v2
    #nombre, p_apellido, s_apellido = obtener_nombre_apellido1_apellido2_usuario(preguntar_nombre_completo(), preguntar_separador())
    #print(nombre, p_apellido, s_apellido)












    












