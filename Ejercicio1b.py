import numpy as np

def multiplicar(A, B):
    # Multiplicar las matrices A y B usando la función dot de numpy
    C = np.dot(A, B)
    
    # Imprimir el resultado de la multiplicación
    print(C)
    
    # Devolver el resultado
    return C

# Definir las matrices A y B
A = np.array([[2, -3], [3, 1]])
B = np.array([[1, 5, -4], [-3, 2, 0]])

# Imprimir el ejercicio
print("Ejercicio  b")

# Llamar a la función multiplicar con las matrices A y B
multiplicar(A, B)
