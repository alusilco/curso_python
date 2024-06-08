#listas
numeros = [1, 2, 3, 4, 5, 4, 6, 7, 8]
print(type(numeros))
numeros[0] = 10
numeros[-1] = 9
print(numeros)

# añadir un elemento (append)
numeros.append(12)
print(numeros)
# añadir un elemento (insert)
numeros.insert(1, 20)
print(numeros)

# borrado
numeros.remove(4)
print(numeros)

del numeros[0]
print(numeros)

lista_numeros = list((1, 2, 3, 4))
print(lista_numeros)

mi_tupla = tuple([1, 2, 3, 4, 5, 6, 7])
print(mi_tupla)

# conjuntos / set
conjunto = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto2 = {6,7,8,9}
print(conjunto)
print(type(conjunto))

#comunes = conjunto.intersection(conjunto2)
comunes = conjunto & conjunto2
print(comunes)

for item in comunes:
    print(item)

# union_conjuntos = conjunto.union(conjunto2) # 1,2,3,4,5,6,7,8,6,7,8,9
union_conjuntos = conjunto | conjunto2
print(union_conjuntos)


lista = [1,2,3,4,4,4,5,6,7,7,7,8,9,0]
lista_sin_duplicados = list(set(lista))
print(lista_sin_duplicados)

comunes.add(10)
if 1 in comunes:
    comunes.remove(1)
comunes.discard(1)

