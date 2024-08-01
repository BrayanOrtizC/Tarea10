import numpy as np

def calcular_inversa(A):
    """
    Calcula la inversa de una matriz A si es no singular.
    """
    det = np.linalg.det(A)  # Calcular el determinante de A
    if det != 0:
        inv = np.linalg.inv(A)  # Calcular la inversa de A
        return inv
    else:
        print("La matriz proporcionada es singular y no tiene inversa.")
        return None

# Matriz 3
A3 = np.array([[1, 1, -1, 1], [1, 2, -4, -2], [2, 1, 1, 5], [-1, 0, -2, -4]])

# Calcular la inversa de la Matriz 3
inversa_A3 = calcular_inversa(A3)
if inversa_A3 is not None:
    print(f"La inversa de la Matriz 3 es:\n{inversa_A3}")
