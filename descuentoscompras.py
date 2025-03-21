def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.
    
    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 15%)
    :return: Monto del descuento calculado
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Solicitar entradas del usuario
monto_total_1 = float(input("Ingrese el monto total de la primera compra: "))
monto_total_2 = float(input("Ingrese el monto total de la segunda compra: "))

# Llamada a la función calcular_descuento
descuento_1 = calcular_descuento(monto_total_1)
descuento_2 = calcular_descuento(monto_total_2)

# Mostrar resultados
print(f"Monto total: {monto_total_1}, Descuento: {descuento_1}, Monto final: {monto_total_1 - descuento_1}")
print(f"Monto total: {monto_total_2}, Descuento: {descuento_2}, Monto final: {monto_total_2 - descuento_2}")
