
#tuple

numeros = (1, 2, 3, 4, 5) # estructura inmutable

numeros_v2 = numeros[:]

#print(id(numeros))
#print(id(numeros_v2))

nota = 9
nota_v2 = 10
#print(id(nota))
#print(id(nota_v2))


#from operaciones_alumnos import obtener_nota, obtener_nombre_completo
import operaciones_alumnos as ops_alumno 

if  __name__ == "__main__":

    # tuplas
    alumno_data = (1,"Juan", "Lopez", 9.5) # id, nombre, apellido, nota
    alumno2_data = (2,"Maria", "Lopez", 7.0) # id, nombre, apellido, nota
    alumno3_data = (3,"Luis", "Mas", 5.5) # id, nombre, apellido, nota
    alumno4_data = (4,"Jimena", "Perez", 6.5) # id, nombre, apellido, nota


    aula_virtual = [alumno_data, alumno2_data, alumno3_data, alumno4_data] 

    #matricular un nuevo alumno
    alumno5_data = (5,"Alicia", "Perez", 8.0) # id, nombre, apellido, nota
    aula_virtual = ops_alumno.matricular_alumno(aula_virtual, alumno5_data)
    #aula_virtual_dummy = ops_alumno.matricular_alumno(None, None)

    #print(aula_virtual_dummy)

    # mostrar la nota de cada uno de los alumnos del aula
    # HERE
    ops_alumno.mostrar_notas(aula_virtual)

    nota_alumno = ops_alumno.obtener_nota(alumno_data)
    print(f"La nota del alumno es {nota_alumno}")

    nota_alumno = ops_alumno.obtener_nota(alumno2_data)
    print(f"La nota del alumno es {nota_alumno}")

    nombre_completo = ops_alumno.obtener_nombre_completo(alumno_data)
    print(f"Me llamo {nombre_completo}")

    nombre_completo = ops_alumno.obtener_nombre_completo(alumno2_data)
    print(f"Me llamo {nombre_completo}")

    datos_alumno = ops_alumno.obtener_todos_los_datos(alumno_data)
    print(datos_alumno)

    SEPARADOR = ','
    datos_alumno_lista = datos_alumno.split(SEPARADOR) # 1,Juan,Lopez,9.5 -> [1,'Juan','Lopez',9.5]
    print(datos_alumno_lista)

    # obtener la media de las notas de los alumnos del aula virtual
    # dato = round(3.45678,2)

    nota_media = ops_alumno.calcular_nota_media(aula_virtual)
    if nota_media is not None:
        print(f"La nota media del grupo virtual es de {nota_media}")

    

    




    







