

alumnos = { 
        '1234H' : ('Juan', 21, 8.5),
        '1234J' : ('Maria',20, 9.5),
        '1234F' : ('Berta',19,7.5),
        '1234A' : ('Lucas',22,8.5)
}

#update
alumnos['1234H'] = ('Juan', 21, 9.0)

#alta
alumnos['1111H'] = ('Mario', 20, 7.0)

print(alumnos)
del alumnos['1111H']
print(alumnos)

data_alumno = alumnos.get('1234X', "Sin data")
if data_alumno == "Sin Data":
    print("Alumno no existe")


