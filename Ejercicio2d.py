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

# Matriz 4
A4 = np.array([[4, 0, 0, 0], [6, 7, 0, 0], [9, 11, 1, 0], [5, 4, 1, 1]])

# Calcular la inversa de la Matriz 4
inversa_A4 = calcular_inversa(A4)
if inversa_A4 is not None:
    print(f"La inversa de la Matriz 4 es:\n{inversa_A4}")
