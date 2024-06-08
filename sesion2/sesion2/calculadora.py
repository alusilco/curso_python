from operaciones import sumar, restar, multiplicar, dividir

def pedir_operandos():
    op_1 = int(input('Op1?')) # casting de str a int
    op_2 = int(input('Op2?')) # casting de str a int

    return op_1, op_2

def pedir_operador():
    oper = input("+,-,*,/?:")
    return oper


if __name__ == "__main__":
    
    operando_1, operando_2 = pedir_operandos()
    operador = pedir_operador()

    if operador == "+":
        resultado = sumar(operando_1, operando_2)
    elif operador == "-":
        resultado = restar(operando_1, operando_2)
    elif operador == "*":
        resultado = multiplicar(operando_1, operando_2)
    elif operador == "/":
        resultado = round(dividir(operando_1, operando_2),2)
    else:
        resultado = None

    
    if resultado is not None:
        print(f"El resultado es {resultado}")
    else:
        print("Operacion no permitida")



