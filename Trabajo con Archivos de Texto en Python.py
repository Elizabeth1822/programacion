#Crear y escribir en el archivo my_notes.txt

with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Terminar el proyecto de programación.\n")
    file.write("Nota 2: Estudiar para el examen de matemáticas.\n")
    file.write("Nota 3: Comprar más café para la oficina.\n")

# Leer el contenido del archivo línea por línea
with open("my_notes.txt", "r") as file:
    # Leer y mostrar cada línea del archivo
    for line in file:
        print(line.strip())  # strip() para eliminar los saltos de línea adicionales al final de cada línea
