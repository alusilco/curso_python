def obtener_nota(alumno: tuple):
    #return alumno[3]
    #return alumno[len(alumno)-1]
    return alumno[-1] # la ultimo pos

def obtener_nombre_completo(alumno: tuple):
    return f"{alumno[1]} {alumno[2]}"

def obtener_todos_los_datos(alumno: tuple):
    datos = '' # variable local
    for dato in alumno:
        datos = datos + str(dato) + "," # datos =1,Juan,Lopez,9.5
    
    return datos.strip(',')

def mostrar_notas(l_alumnos: list):
    for alumno in l_alumnos:
        print(obtener_nota(alumno))


def matricular_alumno(l_alumnos: list, alumno: tuple):
    if l_alumnos is not None and alumno is not None:
        l_alumnos.append(alumno)
        return l_alumnos
    
def calcular_nota_media(l_alumnos: list):
    if l_alumnos is not None and len(l_alumnos) > 0:
        sumatorio_notas = 0
        for alumno in l_alumnos:
            #sumatorio_notas = sumatorio_notas + obtener_nota(alumno)
            sumatorio_notas += obtener_nota(alumno)
        
        return round(sumatorio_notas / len(l_alumnos), 2)

    







