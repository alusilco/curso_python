
lista = [1,2]
lista[0] = 4 #modi
lista.append(3)
lista.insert(0, 5)
print(lista)

data = (1, 2, 3, 4, 5) # tuple
#data = 1, #tuple


print(type(data))



#abrir fichero modo escritura 'w'
f = open('./data/info.txt', 'w')
for numero in data:
    f.write(str(numero))
else:
    f.close()

#abrir fichero modo lectura 'r'
try:
    f = open('./data/info100.txt', 'r')
    info = f.read()
    print(f"Info de fichero: {info}")
    f.close()
except FileNotFoundError as ex:
    print(f"No se ha encontrado el fichero: {ex}")
except:
    print("Error en la operacion de ficheros")








