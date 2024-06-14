def main():
    # Solicitar al usuario que ingrese su nombre, edad, dirección y teléfono
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    direccion = input("Ingrese su dirección: ")
    telefono = input("Ingrese su número de teléfono: ")

    # Crear un diccionario con la información recolectada
    datos_usuario = {
        'nombre': nombre,
        'edad': edad,
        'direccion': direccion,
        'telefono': telefono
    }

    # Mostrar la información recolectada formateada
    print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, "
          f"vive en {datos_usuario['direccion']} y su número de teléfono es {datos_usuario['telefono']}.")

if __name__ == "__main__":
    main()
__annotations__