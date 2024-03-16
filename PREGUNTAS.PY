##PREUNTA 01
for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        print(numero)
##PREGUNTA 02
# Se define el tamaño del patrón
tamano_maximo = 5
# Para ejecutar la primera parte del patrón
for i in range(1, tamano_maximo + 1):
    print('* ' * i)
# Ejecutar la última parte del patrón
for i in range(tamano_maximo - 1, 0, -1):
    print('* ' * i)
##PREGUNTA 03
# Almacenar números pares o impares
numeros_pares = []
numeros_impares = []
# Ingreso de datos
while True:
    respuesta = input("Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() == 'NO':
        break  # Salir del bucle while si el usuario responde 'NO'
    elif respuesta.upper() != 'SI':
        print("Respuesta no válida. Por favor, ingrese 'SI' o 'NO'.")
        continue  # Si la respuesta no es 'SI' se continúa con el bucle
    # Solicitar al usuario que ingrese un número
    numero = int(input("Ingrese el número: "))
    # Validar si el número es par o impar
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
# Imprimir los números ingresados
print("Números ingresados:", numeros_pares + numeros_impares)
# Imprimir la cantidad de números pares e impares ingresados
print("Cantidad de números pares:", len(numeros_pares))
print("Cantidad de números impares:", len(numeros_impares))
##PREGUNTA 04
lista_alumnos = []

num_alumnos = int(input("Ingrese el número de alumnos: "))

for i in range(num_alumnos):
    nombre = input("Ingrese el nombre del alumno {}: ".format(i + 1))
    calificaciones = []
    for j in range(3):
        calificacion = float(input("Ingrese la calificación {} para {}: ".format(j + 1, nombre)))
        calificaciones.append(calificacion)
    alumno = {"Alumno": nombre, "Notas": calificaciones}
    lista_alumnos.append(alumno)
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print("Alumno:", alumno["Alumno"])
    print("Notas:", alumno["Notas"])
    print()
##PREGUNTA 05
def contar_digitos(numero, digito):
    numero_str = str(numero)
    cantidad = numero_str.count(str(digito))
    return cantidad

# uso de la función
numero = 977781535
digito = 7
cantidad = contar_digitos(numero, digito)
print("Cantidad de veces {} en el número {}: {}".format(digito, numero, cantidad))
##PREGUNTA 06
def fibonacci(n):
    a, b = 0, 1
    fibonacci_series = []
    fibonacci_series.append(a)
    fibonacci_series.append(b)
    while b < n:
        a, b = b, a + b
        if b < n:
            fibonacci_series.append(b)
    return fibonacci_series
serie_fibonacci = fibonacci(50)
print("Serie de Fibonacci hasta 50:", serie_fibonacci)
##PRGUNTA 07
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False 
    return True

# Uso de la función
numero = 20
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")
##PRGUNTA 08
def factorial(numero):
    # Para validar si el número es negativo
    if numero < 0:
        return "El factorial no está definido para números negativos"
    # Inicializar el factorial como 1
    resultado = 1
    # Calculando el factorial
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Uso de la función
numero = 200
print("El factorial de", numero, "es:", factorial(numero))
##PREGUNTA 09
def omitir_vocales(cadena):
    resultado = ""
    for caracter in cadena:
        if caracter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += caracter
    return resultado
texto = input("Ingrese una cadena de texto: ")
resultado = omitir_vocales(texto)
print("Texto sin vocales:", resultado)
