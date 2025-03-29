# Creación de un diccionario llamado informacion_personal con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modifícarlo con una ciudad diferente
print("Ciudad original:", informacion_personal["ciudad"])  # Mostrar la ciudad original
informacion_personal["ciudad"] = "Guayaquil"  # Modificar la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])  # Mostrar la ciudad modificada

# Agregar una nueva clave-valor al diccionario para la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"  # Actualizar la profesión

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Agregar un número de teléfono ficticio

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]  # Eliminar la clave "edad"

# Imprimir el diccionario final
print("\nDiccionario final:")
print(informacion_personal)