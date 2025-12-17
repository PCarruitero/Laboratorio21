class OperadorInvalido(Exception):
    pass
operacion = input("Ingrese operación: ")
try:
    partes = operacion.split()
    if len(partes) != 3:
        raise ValueError
    n1 = float(partes[0])
    op = partes[1]
    n2 = float(partes[2])
    if op == "+":
        print(n1, "+", n2)
    elif op == "-":
        print(n1, "-", n2)
    elif op == "*":
        print(n1, "*", n2)
    elif op == "/":
        if n2 == 0:
            raise ZeroDivisionError
        print(n1, "/", n2)
    else:
        raise OperadorInvalido
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Valores inválidos")
except OperadorInvalido:
    print("Operador inválido")