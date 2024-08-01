import numpy as np

# Función para realizar la descomposición LU de una matriz
def lu_decomposition(A):
    n = A.shape[0]  # Obtener el tamaño de la matriz (n x n)
    L = np.eye(n)   # Inicializar la matriz L como una matriz identidad de tamaño n x n
    U = A.copy()    # Hacer una copia de la matriz A para usarla como U

    # Realizar la descomposición LU
    for i in range(n):
        for j in range(i+1, n):
            # Calcular los elementos de la matriz L
            L[j, i] = U[j, i] / U[i, i]
            # Actualizar los elementos de la matriz U
            U[j] = U[j] - L[j, i] * U[i]

    return L, U  # Devolver las matrices L y U

# Función para realizar la sustitución hacia adelante
def forward_substitution(L, b):
    n = L.shape[0]   # Obtener el tamaño de la matriz L (n x n)
    y = np.zeros(n)  # Inicializar el vector y con ceros

    # Realizar la sustitución hacia adelante
    for i in range(n):
        # Calcular el valor de y[i]
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    return y  # Devolver el vector y

# Función para realizar la sustitución hacia atrás
def backward_substitution(U, y):
    n = U.shape[0]   # Obtener el tamaño de la matriz U (n x n)
    x = np.zeros(n)  # Inicializar el vector x con ceros

    # Realizar la sustitución hacia atrás
    for i in range(n-1, -1, -1):
        # Calcular el valor de x[i]
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x  # Devolver el vector x

# Función principal para resolver un sistema de ecuaciones usando la descomposición LU
def solve_lu(A, b):
    L, U = lu_decomposition(A)  # Obtener las matrices L y U de la descomposición LU
    y = forward_substitution(L, b)  # Realizar la sustitución hacia adelante
    x = backward_substitution(U, y)  # Realizar la sustitución hacia atrás
    return x  # Devolver la solución del sistema

# Definir una lista de matrices A para diferentes ejercicios
A_list = [
    np.array([[2, -1, 1], [3, 3, 9], [3, 3, 5]], dtype=float),  # Matriz del ejercicio a
    np.array([[1.012, -2.132, 3.104], [-2.132, 4.096, -7.013], [3.104, -7.013, 0.014]], dtype=float),  # Matriz del ejercicio b
    np.array([[2, 0, 0, 0], [1, 1.5, 0, 0], [0, -3, 0.5, 0], [2, -2, 1, 1]], dtype=float),  # Matriz del ejercicio c
    np.array([[2.1756, 4.0231, -2.1732, 5.1967], [-4.0231, 6.0000, 0, 1.1973], [-1.0000, -5.2107, 1.1111, 0], [6.0235, 7.0000, 0, -4.1561]], dtype=float)  # Matriz del ejercicio d
]

# Definir una lista de vectores b correspondientes a cada matriz A
b_list = [
    np.array([-1, 0, 4], dtype=float),  # Vector del ejercicio a
    np.array([1.984, -5.049, -3.895], dtype=float),  # Vector del ejercicio b
    np.array([3, 4.5, -6.6, 0.8], dtype=float),  # Vector del ejercicio c
    np.array([17.102, -6.1593, 3.0004, 0], dtype=float)  # Vector del ejercicio d
]

# Resolver cada sistema de ecuaciones usando la descomposición LU
solutions = [solve_lu(A, b) for A, b in zip(A_list, b_list)]

# Imprimir las soluciones de cada sistema
for i, solution in enumerate(solutions):
    print(f"Solución del ejercicio {chr(97+i)}: {solution}")
