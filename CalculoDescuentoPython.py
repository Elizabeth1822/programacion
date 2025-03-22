# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función
# Caso 1: Usando el porcentaje de descuento por defecto
monto_total1 = 100
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1

# Caso 2: Proporcionando un porcentaje de descuento específico
monto_total2 = 200
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2

# Mostrar resultados
print(f"Para una compra de ${monto_total1}, con un descuento del 10%, el monto del descuento es ${descuento1:.2f} y el monto final a pagar es ${monto_final1:.2f}.")
print(f"Para una compra de ${monto_total2}, con un descuento del {porcentaje_descuento2}%, el monto del descuento es ${descuento2:.2f} y el monto final a pagar es ${monto_final2:.2f}.")
