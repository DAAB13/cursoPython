### bucles (for)
# permiten ejecutar un bloque de código repetidamente mientas ITERA un iterable o una lista

""" 
frutas = ["mandarina", "manzana", "pera"]
for frutas in frutas:
  print(frutas)

word = "Thiago"
for a in word:
  print(a)

"""

# enumerate()
""" 
frutas = ["mandarina", "manzana", "pera"]
for b, a in enumerate(frutas): # a = indice ; b = valoe
  print(f"el indice es {b} y la fruta es {a}")
"""

#bucles anidados
""" 
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for l in letras:
  for n in numeros:
    print(f"{l}{n}")


# break
print(f"\n____break____")
animales = ["perro", "gato", "ratón", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  print(animal)
  if animal == "ratón":
    print(f"el ratón está escondido en indice {idx}")
    break


# continue
print(f"\n____continue____")
animales = ["perro", "gato", "ratón", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro":
    continue
  print(animal)
print("'se salto el loro'")
"""


#comprensión de listas (list comprehension)
animales = ["perro", "gato", "ratón", "loro", "pez", "canario"]
animales_mayus = [a.upper() for a in animales]
print(animales_mayus)

# muestra los números pares de una lista
pares = [b for b in [1, 2, 3, 4, 5, 6] if b % 2 == 0]
print(pares) 