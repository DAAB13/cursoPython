# Listas
# seciencias mutables de elementos
# pueden contener elementos de diferentes tipos

lista1 = [1, 2 , 3, 4, 5, 6, 7, 8]
lista2 = ["manzana", "pera", "sandia"]
lista3 = [1, "hola", 3.14, True]

Lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1,2], [3,4], [5,6]]
"""
print(matrix)

# Acceso a elementos por índice
print(lista2[0]) # manzana
print(lista2[1]) # pera
print(lista2[-1]) # sandia
print(lista2[-2]) # pera

# Slicing (rebadana) de listas
# print(lista1[1:4])
# print(lista1[:3]) # [1,2,3]

print(lista1[:])
print(lista1[::2])
print(lista1[::-1]) # devuelve indices inversos
"""

# modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

lista1 = lista1 + [4, 5, 6]
print(lista1)

lista1 += [7, 8, 9] # forma eficiente
print(lista1)