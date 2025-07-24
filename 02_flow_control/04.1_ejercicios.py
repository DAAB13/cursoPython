# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
"""
lista_1 = [1, 2, 3, 4, 5]
lista_1.append(6)
print(lista_1)

lista_1.insert(1, 10)
print(lista_1)

lista_1[0] = 0
print(lista_1)
"""

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
print(lista_a)

lista_a.remove(1)
print(lista_a)

deleted_num = lista_a.pop(3)
print(f"el número eliminado es: {deleted_num}")

lista_b.clear()

print("Lista a = ", lista_a)
print("Lista b = ", lista_b)
"""

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
"""
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista_1[2:5]
print(lista_1)
"""

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
"""
num = [5, 2, 8, 1, 9, 4, 2]

num.sort()
print(num)

count = num.count(2)
print(count)

siete = 7 in num
print(f"¿está el 7 en la lista?", siete)
"""

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
"""
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()

referencia = original
referencia[0] = 10

print("original: ", original)
print("copia_1: ", copia_1)
print("copia_2: ", copia_2)
print("referencia: ", referencia)
"""

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
"""
frutas = ["Manzana", "pera", "BANANA", "naranja", "arandano"]
frutas.sort()
print(frutas)

frutas.sort(key=str.lower)
print(frutas)
"""


