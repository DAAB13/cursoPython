# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista_1 = [1, 2, 3, 4, 5]
lista_1.append(6)
print(lista_1)

lista_1.insert(1, 10)
print(lista_1)

lista_1[0] = 0
print(lista_1)