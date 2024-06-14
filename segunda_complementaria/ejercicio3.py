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