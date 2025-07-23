###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
"""
num1 = int(input("escribe el primer número\n"))
num2 = int(input("escribe el segundo número\n"))

if num1 > num2:
  print(f"el número {num1} es mayor que el {num2} número")
elif num1 == num2:
  print("los números son iguales")
else:
  print(f"el número {num1} es menor que el número {num2}")
"""



# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
"""
num1 = float(input("Introduce el primer número\n"))
num2 = float(input("Introduce el segundo número\n"))
operation = input("Introduce la operación deseada: +, -, *, /\n")

if operation == "+":
  resultado = num1 + num2
elif operation == "-":
  resultado = num1 - num2
elif operation == "*":
  resultado = num1 * num2
elif operation == "/":
  if num2 == 0:
    print('No se puede dividir entre 0')
  else:
    resultado = num1 / num2
else:
  print("operación no valida")

if "resultado" in locals(): #Comprueba si la variable resultado existe.
  print(f"el resultado es {resultado}")
"""

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
"""
year = int(input("introduce el año para conocer si es biciesto o no\n"))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"el año {year} es biciesto")
else:
  print(f"el año {year} no es biciesto")
"""  

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("introduce una edad\n"))

if 0 <= age <= 2:
  print("bebé")
elif 2 < age <= 12:
  print("niño")
elif 12 < age <= 17:
  print("adolecente")
elif 17 < age <= 64:
  print("adulto")
elif 64 < age:
  print("adulto mayor")
else:
  print("no valido")
