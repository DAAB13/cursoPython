# Ejercicio
# escribe un programa que use un bucle while para contar y mostrar en pantalla los números del 1 al 5,
# cada uno en una línea nueva.
"""
a = 1

while a <= 5:
  print(a)
  a = a + 1
"""


# Ejercicio
# Crea un programa que guarde una "palabra secreta" (por ejemplo, "python"). 
# El programa debe pedirle al usuario que adivine la palabra. 
# Mientras el usuario no escriba la palabra secreta correcta, 
# el programa debe seguir pidiéndosela una y otra vez.
""" 
secret = "python"
intento = ""

while secret != intento:
  intento = input("ingrese la contraseña: ")
  if intento != secret:
    print("intentelo de nuevo")
print("correcto")
"""
###-----------------------------------------------------------------------------------------

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
""" 
a = 10

while a >= 1:
  print(a)
  a -= 1

print("listo!")
"""

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusido el 20) usando un bucle while.
""" la_suma 1 la_suma = 0

while a <= 20:
  if a % 2 == 0:
    suma = suma + a
  a += 1
print(f"la suma es: {suma}")
"""


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

""" 
try:
  num = int(input("introduce un número positivo: "))

  if num < 0:
    print("el factorial no está definido en números negativos")
  else:
    factorial = 1
    cont = 1
    while cont <= num:
      factorial *= cont
      cont += 1
    print(f"el factorial de {num} es: {factorial}")
except ValueError:
  print("Se debe introducir un número entero") 
"""


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
""" 
while True:
  contraseña = input("introduce la contraseña: ")
  if len(contraseña) >= 8:
    print("----contraseña valida----")
    break
  else:
    print("Error: faltan caracteres")
"""

""" 
contraseña = "diego"
login = ""

while login != contraseña:
  login = (input("introduce la constraseña: "))
  if login != contraseña:
    print("intentalo de nuevo")
print("contraseña valida")
"""

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
""" 
contraseña = ""

while len(contraseña) < 8:
  contraseña = input("introduce una contraseña (min 8 caracteres)\n")
  if len(contraseña) < 8:
    print("incorrecto: al menos debe tener 8 caracteres")
print("contraseña valida") 
"""

""" 
while True:
  contraseña = input("introduce la constraseña\n")
  if len(contraseña) >= 8:
    print("contraseña valida")
    break
  else:
    print("la contraseña debe tener al menos 8 caracteres") 
"""

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

"""
try:
  num = int(input("introduce un número: "))
  producto = 1

  while producto <= 10:
    resultado = num * producto
    print(f"{num} x {producto} = {resultado}")
    producto += 1
except ValueError:
  print("error: introduce un número") 
"""


"""
while True:
  try:
    num = int(input("introduce un número: \n"))
    break
  except ValueError:
    print("introduce un número entero\n")

print(f"\n------tabla de multiplicar para el número: {num} --------\n")
producto = 1
while producto <= 10:
  resultado = num * producto
  print(f"{num} x {producto} = {resultado}")
  producto += 1
"""

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# Un número es primo si es divisible por sólo uno de los números enteros entre 1 y él mismo, incluido.



### MINI PROYECTO -----------------------

""" 
Crea un programa que muestre un menú de opciones y se repita hasta que el usuario elija "salir".

Comportamiento esperado:

--- MENÚ ---
1. Saludar
2. Contar hasta 5
3. Salir
Elige una opción: 1
¡Hola, qué tal!

--- MENÚ ---
1. Saludar
2. Contar hasta 5
3. Salir
Elige una opción: 2
1
2
3
4
5

--- MENÚ ---
1. Saludar
2. Contar hasta 5
3. Salir
Elige una opción: 3
Adiós. 
"""

""" 
while True:
  print("1. Saludar")
  print("2. Contar hasta 5")
  print("3. Salir")

  opcion = input("escoge la opción: ")

  if opcion == "1":
    print("hola q tal?")
  elif opcion == "2":
    print("___contando___")
    contador = 1
    while contador <= 5:
      print(contador)
      contador += 1
  elif opcion == "3":
    print("good bye")
    break
  else:
    print("error - opción no valida. escoger '1' o '2' o '3'")
"""