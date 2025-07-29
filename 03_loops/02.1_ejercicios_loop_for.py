# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
""" 
for a in range(2, 21, 2):
  print(a)
"""

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
""" 
list_1 = [10, 20, 30, 40, 50]
la_suma = 0
for idx in list_1:
  la_suma += idx
media = la_suma / len(list_1)
print(media) 
"""

""" 
numeros = [10, 20, 30, 40, 50]
suma = 0

for a in numeros:
  suma = suma + a

media = suma / len(numeros)
print(media) 
"""

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
""" 
numeros = [15, 5, 25, 10, 20]
maxi = numeros[0]

for n in numeros:
  if n > maxi:
    maxi = n
print("de la lista numeros")
print(f"el número máximo es: {maxi}")
"""

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
""" 
palabras = ["casa", "arbol", "sol", "elefante", "luna", "florero"]
mayor5 = []
for word in palabras:
  if len(word) > 5:
    mayor5.append(word)
print(f"lista de palabras con más de 5 caracteres: {mayor5}")

other_way = [word for word in palabras if len(word) > 5]
print(f"otra forma de optener las palabras mayores de 5 caracteres es asi: {other_way}")
"""


# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
""" 
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("introduce la letra: ")
contador = 0
for word in palabras:
  if word.lower().startswith(letra):
    contador += 1
print(contador) 
"""

lista_1 = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("introduce la letra para el filtrar la lista: ")

filtro = [idx for idx in lista_1 if idx.lower().startswith(letra.lower())]
print(filtro)

