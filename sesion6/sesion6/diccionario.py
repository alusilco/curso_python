def escribir_log(l_errores: list, nombre_fichero: str = "errores.log"):
    with open(f'data/{nombre_fichero}', 'a') as f:
        f.writelines(l_errores)
    


conjunto = {1,3,4,5,6,7}

diccionario = { 
    '1234H' : 'Juan',
    '1234J' : 'Maria',
    '1234F' : 'Berta',
    '1234A' : 'Lucas',
    
    }

#print("0.03".replace(".",","))

data = diccionario['1234A'] 
print(data)

# inicializar una lista vacia
errores = list()


dni = input("DNI?:")
try:
    print(diccionario[dni.upper()])
except KeyError as kex:
    print("Error en clave")
    errores.append(f"La clave que ha dado error es:{kex}\n") 
except:
    print("Operacion imposible")

if len(errores) > 0:
    escribir_log(errores)



alumnos = { 
    '1234H' : ('Juan', 21, 8.5),
    '1234J' : ('Maria',20, 9.5),
    '1234F' : ('Berta',19,7.5),
    '1234A' : ('Lucas',22,8.5)
    
}

def calcular_media(d_alumnos: dict) -> float:
    sumatorio = 0
    media = 0.0
    for alumno in d_alumnos.items():
        nota_alumno = alumno[-1][-1] #('1234H', ('Juan', 21, 8.5))
        sumatorio += nota_alumno #sumatorio = sumatorio + nota_alumno
    else:
        media = round(sumatorio / len(d_alumnos),2)
    
    return media

media_clase = calcular_media(alumnos)
print(f"La media de la clase es: {media_clase}")
