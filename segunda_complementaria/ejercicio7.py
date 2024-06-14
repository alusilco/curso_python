# 17. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
# contenido del diccionario.
def main():
    # Crear un diccionario vacío para almacenar la información de la persona
    persona = {}

    # Solicitar información al usuario y llenar el diccionario
    print("Por favor ingrese la información de la persona:")

    # Solicitar y añadir el nombre
    nombre = input("Nombre: ")
    persona['nombre'] = nombre
    print(persona)

    # Solicitar y añadir la edad
    edad = input("Edad: ")
    persona['edad'] = edad
    print(persona)

    # Solicitar y añadir el sexo
    sexo = input("Sexo: ")
    persona['sexo'] = sexo
    print(persona)

    # Solicitar y añadir el teléfono
    telefono = input("Teléfono: ")
    persona['telefono'] = telefono
    print(persona)

    # Solicitar y añadir el correo electrónico
    email = input("Correo electrónico: ")
    persona['email'] = email
    print(persona)

if __name__ == "__main__":
    main()
