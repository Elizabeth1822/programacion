# Crea una matriz bidimensional de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f'Valor {valor} encontrado en la posición ({i}, {j})'
    return f'Valor {valor} no encontrado en la matriz'

# Valor a buscar
valor_a_buscar = 5

# Llama a la función y muestra el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)
