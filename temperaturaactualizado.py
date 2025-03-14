import random

# Definimos los datos de temperatura organizados por ciudad, semana y día.
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear la estructura tridimensional con temperaturas aleatorias entre 10°C y 35°C
temperaturas = {
    ciudad: [
        [{"day": dia, "temp": random.randint(10, 35)} for dia in dias_semana]
        for _ in range(num_semanas)
    ]
    for ciudad in ciudades
}

def calcular_promedio_temperaturas(datos):
    """
    Calcula el promedio de temperatura por ciudad y semana.
    
    Parámetros:
    - datos (dict): Diccionario con temperaturas organizadas por ciudad y semana.
    
    Retorna:
    - dict: Diccionario con los promedios de temperatura por ciudad y semana.
    """
    promedios = {}

    for ciudad, semanas in datos.items():
        promedios[ciudad] = []
        for semana_idx, semana in enumerate(semanas):
            suma_temperaturas = sum(dia["temp"] for dia in semana)
            promedio = suma_temperaturas / len(semana)
            promedios[ciudad].append(promedio)
    
    return promedios

# Calcular los promedios
promedios_ciudades = calcular_promedio_temperaturas(temperaturas)

# Imprimir los resultados
print("\n--- Temperaturas Promedio por Ciudad y Semana ---\n")
for ciudad, promedios in promedios_ciudades.items():
    for semana_idx, promedio in enumerate(promedios):
        print(f"{ciudad}, Semana {semana_idx + 1}: {promedio:.2f}°C")