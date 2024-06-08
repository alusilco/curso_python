def preguntar_datos_usuario():
    # variables locales
    nombre = input('Nombre?:')
    apellido = input('Apellido?:')
    
    return nombre, apellido

def mostrar_datos_usuario(n_usuario, a_usuario):
    print(f"Soy el usuario {n_usuario} {a_usuario}")

def preguntar_identificador():
    identificador = input('ID?:')
    return identificador

def mostrar_identificador(i_usuario):
    print(f"El id del usuario es {i_usuario}")


