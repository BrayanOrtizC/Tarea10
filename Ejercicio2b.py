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

# Matriz 2
A2 = np.array([[1, 2, 0], [2, 1, -1], [3, 1, 1]])

# Calcular la inversa de la Matriz 2
inversa_A2 = calcular_inversa(A2)
if inversa_A2 is not None:
    print(f"La inversa de la Matriz 2 es:\n{inversa_A2}")
