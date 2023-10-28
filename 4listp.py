# Crear una lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Crear un diccionario para almacenar las notas
notas = {}

# Pedir al usuario las notas para cada asignatura
for asignatura in asignaturas:
    nota = float(input("Ingresa la nota de {}: ".format(asignatura)))
    notas[asignatura] = nota

# Mostrar las notas ingresadas por el usuario
for asignatura, nota in notas.items():
    print("En {} has sacado {:.2f}".format(asignatura, nota))
