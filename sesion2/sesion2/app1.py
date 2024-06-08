
nombre = 'Juan'
apellido1 = 'Garcia'
apellido2 = 'Ibañez'

# forma clasica
nombre_completo = nombre + " " + apellido1 + " " + apellido2
print(nombre_completo)

# forma recomendada
nombre_completo = f"{nombre} {apellido1} {apellido2}"
print(nombre_completo)

# forma recomendada
nombre_completo = "{0} {1} {2}".format(nombre, apellido1, apellido2)
print(nombre_completo)

# saber la edad del usuario
# edad = input('Escriba su edad:')
edad = 45
#print(f"Tengo {edad} años")
#print(type(edad))

edad_numerica = int(edad) # casting / cast
print(edad_numerica)
print(type(edad_numerica))

tiene_hijos = False # bool (boolean)
print(type(tiene_hijos))

#diez_en_numero = int('Hola')
#print(type(diez_en_numero))

info_hijos = input('Tienes hijos?(S/N):')

# estructuras condicionales (if)
#si el usuario me ha dicho S entonces: 
# version de intro a los condicinales (no correcta)

# if info_hijos.lower() == 's':
#    tiene_hijos = True
#    print('Tiene hijos') 

# if info_hijos.lower() == 'n':
#    tiene_hijos = False
#    print('No tiene hijos') 


# version correcta condicional
tiene_hijos = info_hijos.lower() == 's' # bool

if tiene_hijos == True:
    print('Tiene hijos') 
elif tiene_hijos == False:
    print('No tiene hijos') 
else:
    print("Opción incorrecta")

print(tiene_hijos)







