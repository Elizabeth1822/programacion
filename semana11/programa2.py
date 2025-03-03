# Crea una matriz bidimensional de 3x3
matriz = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    matriz[fila].sort()
    return matriz

# Fila a ordenar (index 0, 1, 2 para filas 1, 2, 3 respectivamente)
fila_a_ordenar = 1

# Muestra la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordena la fila especificada
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Muestra la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
