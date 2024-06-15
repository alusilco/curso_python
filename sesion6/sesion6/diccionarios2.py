def calcular_media(d_alumnos: dict) -> float:
    sumatorio = 0
    media = 0.0
    for alumno in d_alumnos.items():
        nota_alumno = alumno[-1][-1] #('1234H', ('Juan', 21, 8.5))
        sumatorio += nota_alumno #sumatorio = sumatorio + nota_alumno
    else:
        media = round(sumatorio / len(d_alumnos),2)
    
    return media

if __name__ == "__main__":
    alumnos = { 
        '1234H' : ('Juan', 21, 8.5),
        '1234J' : ('Maria',20, 9.5),
        '1234F' : ('Berta',19,7.5),
        '1234A' : ('Lucas',22,8.5)
        
    }

    media_clase = calcular_media(alumnos)
    print(f"La media de la clase es: {media_clase}")