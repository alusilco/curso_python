# 13. Juguemos al juego de adivinar el numero, generaremos un número entre 1 y 100.
# Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que
# el número buscado. También poner el número de intentos requeridos.
import random

#12def juego_adivina_numero():
    #numero_secreto = random.randint(1, 100)
    #intentos_realizados = 0
    #numero_adivinado = False
    
    #print("¡Bienvenido al juego de adivinar el número!")
    #print("He pensado en un número entre 1 y 100. ¡Adivina cuál es!")

    #while not numero_adivinado:
       # intento = int(input("Introduce tu número: "))
       # intentos_realizados += 1
        
        #if intento == numero_secreto:
          #  print(f"¡Felicidades! ¡Has adivinado el número en {intentos_realizados} intentos!")
          #  numero_adivinado = True
        #elif intento < numero_secreto:
           # print("El número secreto es mayor. Sigue intentándolo.")
        #else:
           # print("El número secreto es menor. Sigue intentándolo.")

    #print("¡Gracias por jugar!")

# Llamamos a la función para iniciar el juego
#juego_adivina_numero()


 #este modulo inclye incluye funciones y metodos para generar numeros aleatorios
aleatorio = random.randint(1,101) #numeros aleatorios entre 1 a 100
intentos = 1
numero = int(input("Introduce tu numero "))
while numero != aleatorio:
    if numero > aleatorio:
        print("El numero que has introducido es mas grande que aleatorio")
    elif numero < aleatorio:
        print("El numero que has introducido es mas pequeño que aleatorio")
    numero = int(input("Introduce tu numero "))
    intentos = intentos + 1
else:
    print("Felicidades has acertado con el numero ", numero)
    print("Has necesitado ", intentos) 

# 18. Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
# 19. Escribir un programa que pregunte al usuario los números ganadores de la lotería
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a
# mayor.
