""" Programa que calcule la tabla de multiplicar de cualquier número entero, dado por el usuario.
    Debe calcular la tabla desde el 0 hasta el 10.  """


def tablaDeMultiplicar(num1, num2):
    return str(num1) + " * " + str(num2) + " = " + str(num1*num2)

num = int(input("Ingresa un número entero: "))

for i in range (0, 11):
    print(tablaDeMultiplicar(num, i))