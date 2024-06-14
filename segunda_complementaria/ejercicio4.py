# 14. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
# 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso
# si la divisa no está en el diccionario.e


def main():
    # Definir el diccionario con las divisas y sus símbolos
    divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

    # Pedir al usuario que introduzca una divisa
    divisa_usuario = input("Introduce una divisa (Euro, Dollar o Yen): ")

    # Mostrar el símbolo correspondiente si la divisa está en el diccionario
    if divisa_usuario in divisas:
        print(f"El símbolo de {divisa_usuario} es {divisas[divisa_usuario]}")
    else:
        print("La divisa introducida no está en el diccionario.")

if __name__ == "__main__":
    main()
