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

# Definir las matrices para el sistema b
A2 = np.array([[2, 0, 0], [-1, 1, 0], [3, 2, -1]], dtype=float)
B2 = np.array([[1, 1, 1], [0, 1, 2], [0, 0, 1]], dtype=float)
b2 = np.array([-1, 3, 0], dtype=float)

# Calcular la matriz combinada A para el sistema b
A_combined_2 = A2 @ B2

# Resolver el sistema
solucion_b = solve_lu(A_combined_2, b2)
print(f"Solución del sistema b: {solucion_b}")
