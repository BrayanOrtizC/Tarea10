import numpy as np

# Función para realizar la descomposición LU
def lu_decomposition(A):
    """
    Realiza la descomposición LU de una matriz A.
    """
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()

    for i in range(n):
        for j in range(i + 1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j] = U[j] - L[j, i] * U[i]

    return L, U

def forward_substitution(L, b):
    """
    Realiza la sustitución hacia adelante para resolver Ly = b.
    """
    n = L.shape[0]
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    return y

def backward_substitution(U, y):
    """
    Realiza la sustitución hacia atrás para resolver Ux = y.
    """
    n = U.shape[0]
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x

def solve_lu(A, b):
    """
    Resuelve el sistema Ax = b utilizando la descomposición LU.
    """
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

# Definir las matrices para el sistema a
A1 = np.array([[1, 0, 0], [2, 1, 0], [-1, 0, 1]], dtype=float)
B1 = np.array([[2, 3, -1], [0, -2, 1], [0, 0, 3]], dtype=float)
b1 = np.array([2, -1, 1], dtype=float)

# Calcular la matriz combinada A para el sistema a
A_combined_1 = A1 @ B1

# Resolver el sistema
solucion_a = solve_lu(A_combined_1, b1)
print(f"Solución del sistema a: {solucion_a}")
