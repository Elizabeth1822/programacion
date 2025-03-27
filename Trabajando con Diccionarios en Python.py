# Crear un diccionario con los datos de María González
informacion_personal = {
    "nombre": "María González",
    "edad": 25,
    "telefono": "0963000201",
    "ciudad": "Guayaquil",
    "profesion": "Ingeniera"  # Profesión incluida desde el inicio
}

# Acceder y modificar el valor de la clave 'ciudad'
informacion_personal["ciudad"] = "Quito"  # Cambiar la ciudad a 'Quito'

# Verificar si la clave 'telefono' existe; si no, agregarla
# En este caso, la clave ya existe, por lo que no se necesita agregarla

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)

# Resultado esperado:
# Diccionario final: {'nombre': 'María González', 'telefono': '0963000201', 'ciudad': 'Quito', 'profesion': 'Ingeniera'}

