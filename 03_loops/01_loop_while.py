### Bucle = while
# permiten ejecutar un bloque de código repetitivamente
# mientras se cumpla una condición

# contador = 0
"""
while contador < 5:
  print(contador)
  contador += 1 # importante para evitar un bucle infinito
"""

# while con break
"""
while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # romper o salir del bucle

contador = 0
while contador <= 100:
  contador += 1
  print(contador)
  if contador % 5 == 0: # El símbolo % no calcula la división, 
                        # sino el residuo que queda después de dividir un número entre otro.
    print("el número es multiplo de 5")
    break
"""

# while y continue
# hace saltarse una iteración en concreto y continue el bucle
"""
contador = 0
while contador < 10:
  contador += 1
  if contador % 2 == 0:
    continue
  print(contador)
"""

# while y else
"""
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("el bucle ha terminado")
"""



### Ejercicio :
# perdile al usurio que ingrese un número positivo
# por que si no, no se le dejará en paz
"""
num = -1
while num <=0:
  num = int(input("ingrese un número posito\n"))
  if num <= 0:
    print("el número debe ser positivo, intentalo nuevamente")
print (f"el numero que ingresaste es: {num}")
"""

num = -1
while num <= 0:
  try:
    num = int(input("introduce un número positivo\n"))
    if num <=0:
      print("el numero debe ser positivo, intentelo nuevamente")
  except:
    print("tienes que ingresar un número si o si")
print(f"el número ingreso es: {num}")

