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

def ordenar_fila(matriz, fila):
    """Ordena una fila específica de la matriz en orden ascendente usando Bubble Sort."""
    nueva_matriz = matriz.copy()
    for i in range(len(nueva_matriz[fila])):
        for j in range(len(nueva_matriz[fila]) - 1 - i):
            if nueva_matriz[fila][j] > nueva_matriz[fila][j + 1]:
                nueva_matriz[fila][j], nueva_matriz[fila][j + 1] = nueva_matriz[fila][j + 1], nueva_matriz[fila][j]
    return nueva_matriz

# Programa principal
if __name__ == "__main__":
    matriz = crear_matriz()
    print("Matriz original:")
    print(matriz)
    
    valor_a_buscar = int(input("Ingrese el valor a buscar: "))
    posicion = buscar_valor(matriz, valor_a_buscar)
    
    if posicion:
        print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
    
    fila_a_ordenar = int(input("Ingrese el índice de la fila a ordenar (0-2): "))
    matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)
    
    print("Matriz con la fila ordenada:")
    print(matriz_ordenada)