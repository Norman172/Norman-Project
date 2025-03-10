import random

# Definir dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

# Crear matriz 3D (ciudades x días x semanas) con temperaturas aleatorias (entre 10°C y 35°C)
temperaturas = [[[random.randint(10, 35) for _ in dias_semana] for _ in range(num_semanas)] for _ in ciudades]

# Calcular promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas en {ciudad}:")
    for semana in range(num_semanas):
        promedio_semana = sum(temperaturas[i][semana]) / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")
    print()
