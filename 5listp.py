# Crear una lista vacía para almacenar los números de cuenta
numeros_de_cuenta = []

# Pedir al usuario los números de cuenta de al menos 10 alumnos
while len(numeros_de_cuenta) < 10:
    numero_cuenta = input("Ingresa el número de cuenta del alumno: ")
    
    # Verificar si el número ingresado es un número entero positivo
    if numero_cuenta.isdigit():
        numeros_de_cuenta.append(int(numero_cuenta))
    else:
        print("Por favor, ingresa un número de cuenta válido.")

# Ordenar la lista de números de cuenta de menor a mayor
numeros_de_cuenta.sort()

# Mostrar los números de cuenta ordenados
print("Números de cuenta ordenados de menor a mayor:")
for numero in numeros_de_cuenta:
    print(numero)
