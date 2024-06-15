#Estructuras de control en python
#Hay 2 tipos, condicionales e iterativas
#las condiciones, en pythonson 2 la primera es if
#Operadores arimeticos, logicos y binarios
#aritemeticos
print(1 + 1) #suma
print(1 - 1) #restar
print(1 * 1) #multipliccar
print(1 / 2) #dividir
print(1 % 2) #modulo (resto)
print(1 // 2) #cociente de la division entera
print(1 ** 2) #potencia 1 elevado a 2 (cuadrado)

#Logicos
# and, or y not
#podemos tener 2 valores True y False
#tablas de verdad
#and
print(False and False) #False
print(False and True) #False
print(True and False) #False
print(True and True)#True

#or
print(False or False) # False
print(False or True) # True
print(True or False) # True
print(True or True)# True

#not
print(not True) #False
print(not False) #True

#Operadores de comparacion
print(1 > 2) #False (mayor)
print(1 >= 2) # False (mayor o igual)
print(1 < 2) #True (menor)
print(1 <= 2) #True (menor o igual)
print(1 == 2) #False (igual)
print(1 != 2) #True (distinto)

#Operadores a nivel de bits
# & (and), |(or), ~ (not), ^ (exor), <<, >>
print(4 & 5)
print(4 | 5)

#Los enteros en python
entero = 10
#Tambien soporta numeros en otras bases
#Base hexadecimal es decir 0-9 y A-F es base 16, y se representa
#poniendole delante un 0x al numero
entero = 0x10
print(type(entero))
print(entero)

#Conversion primero usamos la base es 16 acordaros
#0x10 => 1 + 0 #primer paso separamos los digitos y los sumamos
# 0x10 => 1 * 16  + 0 * 16 #segundo paso multiplicamos cada numero por su base
# 0x10 => 1 * 16**1  + 0 * 16**0 #se eleva la base a la posicion que ocupa contando de derecha a izquierda empezando en el 0
#hacemos la cuenta
# 0x10 => 1 * 16  + 0 * 1 = 16 + 0 = 16

#tambien podemos trabaja en binario que es base 2 solo hay 0 y 1
print(0b10)
#0b10 => 1 + 0 #sumamo digito a digito
#0b10 => 1*2 + 0*2 #multiplicar por la base
#0b10 => 1*2**1 + 0*2**0 #elevamos
#0b10 => 1*2 + 0*1 = 2 + 0 = 2

print(4 & 5)
#el and tiene tabla de verdad pero con numeros 0 y 1
print(0 & 0) #0
print(0 & 1) #0
print(1 & 0) #0
print(1 & 1) #1

#4 & 5
#4 => 100
#5 => 101
#& => 100 => 4

print(4 | 5)
#tabla de la verdad del |
print(0 | 0) #0
print(0 | 1) #1
print(1 | 0) #1
print(1 | 1) #1

#4 | 5
#4 => 100
#5 => 101
#| => 101 => 5 

#Condicionaless if
# if CONDICION_BOOLEANA:
#     bloque en caso de verdadero
if 1 < 2:
    print("1 es menor que 2")

#el if puede llevar un bloque else al final que se ejecuta si no se cumple las condiciones previas
if 1 < 2:
    print("1 es menor que 2")
else:
    print("1 es mayor que 2")

#puede llevar entre el if y el else, lo blques elif que nos permiten poner mas condiciones
numero = 10

if(numero == 1):
    print("Numero es 1")
elif(numero ==2):
    print("Numero es 2")
elif(numero == 3):
    print("El numero es 3")
else:
    print("No se cumple ninguna de las anteriores")

#if ternario
#tenemos un if especifico que se usa para la incializacion de variables
# VARIABLE = VALOR_EN_CASO_VERDADERO if CONDICION else VALOR_EN_CASO_FALSO
numero  = 10
variable = "Numero es 10 " if numero == 10 else "Numero no es 10"
print(variable)

#Estructuras de control repetitivas
# while y for
# el bucle while se ejecuta mientras se cumple la condicion
# while CONDICION:

numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1

#Pueden llevar un else que se ejecutara cuando la condicion del bucle se deje de cumplir
numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1
else:
    print("La condicion se ha dejado de cumplir")

#xite palabra resevrada llamada break, es salida incondicional de una
#estructura repetitiva
numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1
    break
else:
    print("La condicion se ha dejado de cumplir")

#Se puede poner dentro de un if
numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1
    if numero ==2:
        break
else:
    print("La condicion se ha dejado de cumplir")

#El bucle for
# for TEMPORAL in ITERABLE
#ITERABLE = a los elementos que tienen dentro otros elementos
# listas, conjuntos, diccionarios, strings, tuplas
#lista
lista = [1,2,3,4]

for numero in lista:
    print(numero)

#tuplas
tupla = (1,2,3,4)
for numero in tupla:
    print(numero)

#string
cadena = "Hola Mundo"

for letra in cadena:
    print(letra)

#conjuntos
conjunto = {1,2,3,4}

for item in conjunto:
    print(item)

#Diccionarios
diccionarios = {"clave":"valor"}

for clave in diccionarios:
    print(clave)

#conjuntamente con la funcion range() para generar rangos
#range(INICIO, FIN, STEP)
# INICIO => optativo desde donde empieza el rango valor por defecto 0
# FIN => obligatorioa hasta donde llega el rango que generamos (y no se incluye en la salida)
# STEP => optativo, salto, numero de posiciones que se mueve entre cada generacion

for numero in range(1,10,1):
    print(numero)
