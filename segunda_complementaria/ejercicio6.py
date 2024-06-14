# 16. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
# pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre
# del mes.

# Importamos el módulo datetime para manejar fechas
from datetime import datetime

def main():
    # Solicitar al usuario que ingrese una fecha en formato dd/mm/aaaa
    fecha_str = input("Ingrese una fecha en formato dd/mm/aaaa: ")

    try:
        # Convertir la cadena de entrada a un objeto datetime
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')

        # Obtener el día, mes y año por separado
        dia = fecha.day
        mes_numero = fecha.month
        anio = fecha.year

        # Lista de nombres de los meses en español
        nombres_meses = [
            'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
            'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
        ]

        # Obtener el nombre del mes correspondiente al mes_num
        mes_nombre = nombres_meses[mes_numero - 1]

        # Mostrar la fecha en el formato solicitado
        print(f"{dia} de {mes_nombre} de {anio}")

    except ValueError:
        print("Formato de fecha incorrecto. Debe ser dd/mm/aaaa.")

if __name__ == "__main__":
    main()
