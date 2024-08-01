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

# Matriz 1
A1 = np.array([[4, 2, 6], [3, 0, 7], [-2, -1, -3]])

# Calcular la inversa de la Matriz 1
inversa_A1 = calcular_inversa(A1)
if inversa_A1 is not None:
    print(f"La inversa de la Matriz 1 es:\n{inversa_A1}")
