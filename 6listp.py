# Pedir al usuario una muestra de números separados por comas
entrada_usuario = input("Ingresa una muestra de números separados por comas: ")

# Dividir la entrada del usuario en una lista de números
numeros = [float(numero) for numero in entrada_usuario.split(',')]

# Convertir la lista de números en una tupla
muestra = tuple(numeros)

# Calcular la media de la muestra
media = sum(muestra) / len(muestra)

# Ordenar la lista de números
numeros_ordenados = sorted(muestra)

# Calcular la mediana de la muestra
n = len(numeros_ordenados)
if n % 2 == 0:
    # Si la longitud de la muestra es par, calcular la mediana como el promedio de los dos valores del medio
    mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
else:
    # Si la longitud de la muestra es impar, la mediana es el valor del medio
    mediana = numeros_ordenados[n // 2]

# Mostrar la media y la mediana por pantalla
print("Media: {:.2f}".format(media))
print("Mediana: {:.2f}".format(mediana))
