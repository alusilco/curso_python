
def procesar(data: int): #type hinting
    return data * 10


print(f"El resultado es {procesar(10)}")

nombre ='Juan'
nombre_completo = "Juan Palomo" # snake case

# cadena es un conjunto o coleccion de caracteres
#estrucutura iterativa
for caracter in nombre_completo:
    if caracter == ' ':
        continue
    
    print(f"Caracter:{caracter}")

lista_numeros = [1,2,3,4,5,6,7] # iterable
for numero in lista_numeros:
    if numero == 6:
        #continue
        break
    
    print(procesar(numero))
else:
    print("El recorrido se ha completado")

def es_divisible_3(num: int):
    return num % 3 == 0 # True or False

def crear_lista(limite: int, salto: int = 1):
    return list(range(1,limite,salto)) #casting

#lista_200_impares = list(range(1,201,2)) #casting
lista_200_impares = crear_lista(201, 2)
for numero in lista_200_impares[0:15]:
    if es_divisible_3(numero):
        continue
    
    print(numero)
else:
    print("Proceso ok")















