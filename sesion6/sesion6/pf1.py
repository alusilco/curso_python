

def sumar(x: int, y: int) -> int:
    return x + y


print(sumar(2,7))

#lambda
suma = lambda x, y : x + y

print(suma(2, 7))

multiplicar = lambda x, y : x * y
print(multiplicar(3, 6))

lista_numeros = [1, 2, 3, 4, 5, 6]

print(list(filter(lambda num : num % 2 == 0, lista_numeros)))

print(list(map(lambda num : num * 3, lista_numeros)))

lista_nueva = list()
for numero in lista_numeros:
    res = numero * 3
    lista_nueva.append(res)

print(lista_nueva)



