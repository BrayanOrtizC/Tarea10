import sympy as sp

# Definir el símbolo alfa
alfa = sp.symbols('alfa')

# Definir la matriz A con el parámetro alfa
A = sp.Matrix([
    [1, -1, alfa],
    [2, 2, 1],
    [0, alfa, -3/2]
])

# Calcular el determinante de la matriz A
det_A = A.det()

# Resolver para encontrar los valores de alfa que hacen que el determinante sea cero (matriz singular)
valores_singulares = sp.solve(det_A, alfa)

# Imprimir los valores de alfa que hacen la matriz singular
print("Valores de α que hacen la matriz singular:", valores_singulares)
