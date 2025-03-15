def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante varias semanas.

    Parámetros:
    temperaturas (dict): Un diccionario donde las claves son las ciudades y los valores son listas de temperaturas durante varias semanas.

    Retorna:
    dict: Un diccionario con la ciudad como clave y su temperatura promedio como valor.
    """
    promedios = {}  # Diccionario donde guardaremos los promedios de cada ciudad

    # Recorremos las ciudades y sus temperaturas
    for ciudad, datos in temperaturas.items():
        promedio = sum(datos) / len(datos)  # Calcula el promedio de temperaturas para la ciudad
        promedios[ciudad] = promedio  # Guarda el promedio de la ciudad en el diccionario

    return promedios


# Ejemplo con 4 semanas de datos para 3 ciudades
temperaturas = {
    'Quito': [20, 22, 21, 23],  # Quito
    'Cuenca': [15, 16, 17, 18],  # Cuenca
    'Guayaquil': [30, 32, 31, 33]  # Guayaquil
}

# Llamada a la función para calcular los promedios
promedios = calcular_promedio_temperaturas(temperaturas)

# Imprimir los resultados de los promedios
print(promedios)






