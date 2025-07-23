"""
lista_1 = ["a", "b", "c", "d"]

lista_1.append("e") #añade un elemento al final
print(lista_1)

lista_1.extend(["x", "y"])
print(lista_1)

lista_1.insert(1, "@") # inserta un elemento en la posición que indiquemos
print(lista_1)

lista_1.remove("b") # eliminar la primera apración "b"
print(lista_1)

ultimo = lista_1.pop()
print(ultimo)

lista_1.clear() # eliminar todos los elementos de la lista
print(lista_1)  

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)

num = [3, 10, 2, 8, 99, 101]
num.sort() # ordenar lista modificando la original
print(num)

num = [3, 10, 2, 8, 99, 101] # ordenar listas creando una nueva lista
sorted_numer = sorted(num)
print(sorted_numer)
"""
"""
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
frutas_ordenadas = sorted(frutas)
print(frutas_ordenadas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)
"""

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False
