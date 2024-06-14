##Imprimir “Hola mundo” por pantalla.
print("Hola mundo")

##Crear dos variables numéricas, sumarlas
# Crear dos variables numéricas
numero_uno = 5
numero_dos= 10

# Sumar las variables
suma = numero_uno + numero_dos

# Imprimir el resultado
print("La suma de", numero_uno, "y", numero_dos, "es", suma)

##Mostrar el precio del IVA de un producto con un valor de 100 y su precio final.
# Definir el valor del producto
valor_producto = 100

# Definir la tasa de IVA (por ejemplo, 21%)
iva = 0.21

# Calcular el precio del IVA
precio_iva = valor_producto * iva

# Calcular el precio final
precio_final = valor_producto + precio_iva

# Mostrar el precio del IVA y el precio final
print("El precio del IVA es:", precio_iva)
print("El precio final es:", precio_final)

##De dos números, saber cual es el mayor.
# Definir dos números
numero_uno = 45
numero_dos = 30

# Comparar los números y determinar cuál es el mayor
if numero_uno > numero_dos:
    print("El mayor es:", numero_uno)
elif numero_uno < numero_dos:
    print("El mayor es:", numero_dos)
else:
    print("Ambos números son iguales.")


##Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.
# Primeo crear una variable numérica
numero = 7  
# Verificar si el número está entre 0 y 10
if 0 <= numero <= 10:
    print(f"El número {numero} está entre 0 y 10.")
else:
    print(f"El número {numero} no está entre 0 y 10.")
##Mostrar con un while los números del 1 al 100
# Inicializar el contador
numero = 1
# Mostrar los números del 1 al 100 utilizando un bucle while
while numero < 101:
    print(numero)
    numero = numero + 1
##Mostrar con un for los números del 1 al 100.
for numero in range(1, 101):
    print(numero)

##Mostrar los números pares entre 1 al 100.
# Mostrar los números pares entre 1 y 100
for numero in range(2, 101, 2):
    print(numero)

##Mostrar los caracteres de la cadena “Hola mundo”.
# Cadena de texto
cadena = "Hola mundo"

# Mostrar cada caracter de la cadena
for caracter in cadena:
    print(caracter)

##Mostrar los caracteres de la cadena “Hola mundo” al reves.
# Cadena de texto
cadena = "Hola mundo"

# Mostrar los caracteres al revés
cadena_al_reves = cadena[::-1]
print(cadena_al_reves)

##Generar un rango entre 0 y 10
import random
aleatorio = random.randint(1,101)
print(aleatorio)