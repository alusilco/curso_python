# 12. Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas y con
# los 2 primeros caracteres intercambiados. Por ejemplo, hola mundo pasaría a mula
# hondo

# Pedir al usuario que ingrese las dos cadenas
# Pedir al usuario que ingrese las dos cadenas
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

# Intercambiar los dos primeros caracteres de cada cadena
nueva_cadena1 = cadena2[:2] + cadena1[2:]
nueva_cadena2 = cadena1[:2] + cadena2[2:]

# Mostrar ambas cadenas con un espacio entre ellas
resultado = nueva_cadena1 + " " + nueva_cadena2
print("Resultado:", resultado)

# 13. Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
# Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que
# el número buscado. También poner el número de intentos requeridos.
import random

def juego_adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0
    numero_adivinado = False
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("He pensado en un número entre 1 y 100. ¡Adivina cuál es!")

    while not numero_adivinado:
        intento = int(input("Introduce tu número: "))
        intentos_realizados += 1
        
        if intento == numero_secreto:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos_realizados} intentos!")
            numero_adivinado = True
        elif intento < numero_secreto:
            print("El número secreto es mayor. Sigue intentándolo.")
        else:
            print("El número secreto es menor. Sigue intentándolo.")

    print("¡Gracias por jugar!")

# Llamamos a la función para iniciar el juego
juego_adivina_numero()

# 14. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
# 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso
# si la divisa no está en el diccionario.
# 15. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
# guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
# tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
# 16. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
# pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre
# del mes.
# 17. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
# contenido del diccionario.
# 18. Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
# 19. Escribir un programa que pregunte al usuario los números ganadores de la lotería
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
# mayor.
