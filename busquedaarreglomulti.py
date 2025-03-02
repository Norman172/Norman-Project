import numpy as np

def crear_matriz():
    """Crea una matriz 3x3 con valores definidos."""
    return np.array([[4, 7, 1],
                     [8, 3, 6],
                     [5, 9, 2]])

def buscar_valor(matriz, valor):
    """Busca un valor en la matriz y devuelve su posición si se encuentra."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Programa principal
if __name__ == "__main__":
    matriz = crear_matriz()
    print("Matriz:")
    print(matriz)
    
    valor_a_buscar = int(input("Ingrese el valor a buscar: "))
    posicion = buscar_valor(matriz, valor_a_buscar)
    
    if posicion:
        print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")