# Crear una matriz 3D con las temperaturas diarias de Guayaquil, Quito y Cuenca durante varias semanas
# Ejemplo: 3 ciudades (Guayaquil, Quito, Cuenca), 7 días de la semana, 4 semanas

# Matriz 3D: [ciudades][días de la semana][semanas]
temperaturas = [
    [  # Guayaquil (Ciudad 1)
        [30, 31, 32, 31, 30, 29, 30],  # Semana 1
        [31, 32, 33, 32, 31, 30, 31],  # Semana 2
        [30, 31, 32, 31, 30, 29, 30],  # Semana 3
        [31, 32, 33, 32, 31, 30, 31],  # Semana 4
    ],
    [  # Quito (Ciudad 2)
        [15, 16, 17, 16, 15, 14, 15],  # Semana 1
        [16, 17, 18, 17, 16, 15, 16],  # Semana 2
        [15, 16, 17, 16, 15, 14, 15],  # Semana 3
[  # Cuenca (Ciudad 3)
        [12, 13, 14, 13, 12, 11, 12],  # Semana 1
        [13, 14, 15, 14, 13, 12, 13],  # Semana 2
        [12, 13, 14, 13, 12, 11, 12],  # Semana 3
        [13, 14, 15, 14, 13, 12, 13],  # Semana 4
    ]
]

# Mostrar la matriz de temperaturas
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"Ciudad {ciudad_idx + 1}:")
    for semana_idx, semana in enumerate(ciudad):
        print(f"  Semana {semana_idx + 1}: {semana}")
    print()

