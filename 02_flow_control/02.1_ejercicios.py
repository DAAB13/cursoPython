###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
""""
num1 = int(input("elige el primer número: "))
num2 = int(input("ahora escoge el segundo número: "))

if num1 > num2:
  print(f"el número {num1} es mayor que el número {num2}")
elif num1 < num2:
  print(f"el número {num2} es mayor que el número {num1}")
else:
  print(f"el número {num2} es igual al número {num1}")
"""


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
"""
num_a = float(input("nro 1: "))
operacion = input("escoge una de las siguientes operaciones: * / + -   ")
num_b = float(input("nro 2: "))

if operacion == "*":
  resultado = num_a * num_b
elif operacion == "-":
  resultado = num_a - num_b
elif operacion == "+":
  resultado = num_a + num_b
elif operacion == "/":
  if num_b == 0:
    print("no se puede dividir entre 0")
  else:
    resultado = num_a / num_b
else:
  print("operacion no valida") 

if 'resultado' in locals():
  print(f"el resultado es: {resultado}")
"""


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

""" 
try:
  año = int(input("escribe el año: "))
  if año > 0: 
    if (año % 4 == 0 and año % 100 !=0) or (año % 400 == 0):
      print(f"el año {año} si es bisiesto")
    else:
      print(f"el año {año} no es bisiesto")
  else:
    print("el año debe ser positvo")
except ValueError:
  print("error: introduce un año valido")
"""

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

""" 
try:
  age = int(input("introduce una edad: "))

  if 0 <= age <= 2:
    print("bebé")
  elif 3 <= age <= 12:
    print("niño")
  elif 13 <= age <= 17:
    print("adolescente")
  elif 18 <= age <= 64:
    print("adulto")
  elif age > 65:
    print("adulto mayor")
  else:
    print("introduce un número positivo")
except ValueError:
  print("error: introduce un número")
"""