from usuario import (
    preguntar_datos_usuario, 
    mostrar_datos_usuario, 
    preguntar_identificador, 
    mostrar_identificador)

# punto de entrada
if __name__ == "__main__":
    # preguntar el nombre y el apellido de un usuario
    # variables principales del programa
    nombre_usuario, apellido_usuario = preguntar_datos_usuario()
    mostrar_datos_usuario(nombre_usuario, apellido_usuario)

    # preguntar el identificador del usuario para luego mostrarlo
    id_usuario = preguntar_identificador()
    mostrar_identificador(id_usuario)


    




    
    