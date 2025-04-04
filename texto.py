# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt y escribimos tres líneas de notas personales
with open('my_notes.txt', 'w') as file:  # 'w' significa modo escritura (write)
    file.write("Primera nota: Hoy es un día soleado.\n")  # Escribimos la primera línea
    file.write("Segunda nota: Tengo que hacer la compra más tarde.\n")  # Escribimos la segunda línea
    file.write("Tercera nota: No olvidar llamar a la familia.\n")  # Escribimos la tercera línea

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt y leemos el contenido línea por línea
with open('my_notes.txt', 'r') as file:  # 'r' significa modo lectura (read)
    line = file.readline()  # Leemos la primera línea
    while line:  # Mientras haya líneas por leer
        print(line.strip())  # Mostramos la línea en la consola sin el salto de línea al final
        line = file.readline()  # Leemos la siguiente línea