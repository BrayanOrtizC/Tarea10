import numpy as np
from scipy.linalg import lu

# Definir la cuarta matriz
M4 = np.array([[2.1756, 4.0231, -2.1732, 5.1967], [-4.0231, 6.0000, 0, 1.1973], [-1.0000, -5.2107, 1.1111, 0], [6.0235, 7.0000, 0, -4.1561]])

# Factorización LU para la matriz 4
P4, L4, U4 = lu(M4)

# Imprimir los resultados
print("Matriz 4:")
print("\nL:\n", L4)
print("\nU:\n", U4)
