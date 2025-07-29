### Ejercicio 1: Calculadora Básica --------

# Objetivo: Crear una función que reciba dos números y un operador para devolver el resultado.
# Servirá para practicar if/elif/else y el uso de return.

# -----------Enunciado-------------
# Escribe una función llamada operacion_basica(num1, num2, operador).

# Debe aceptar tres argumentos: 
# dos números y una cadena de texto que será el operador ("suma", "resta", "multiplicacion", "division").

# La función debe devolver el resultado de la operación matemática.
# Si el operador no es válido, debe devolver el mensaje: "Operador no reconocido".

# Extra: Si se intenta una "division" por cero, debe devolver "No se puede dividir por cero".

# Pista: Dentro de la función, usa una serie de if/elif/else 
# para comprobar qué valor tiene el parámetro operador.


def operacion_basica(num_1, num_2, operador):
  if operador == "+":
    return num_1 + num_2
  elif operador == "-":
    return num_1 - num_2
  elif operador == "*":
    return num_1 * num_2
  elif operador == "/":
    if num_2 == 0:
      return "no se puede divir entre 0, intentelo de nuevo"
    else:
      return num_1 / num_2
  else:
    return "operador no reconocido"

resultado = operacion_basica(2, 3, "-")
print(resultado)



### Ejercicio 2: Generador de Listas
# Objetivo: Usar un bucle for y range dentro de una función para crear y devolver una lista.

# Enunciado:
# Escribe una función llamada generar_lista_pares(limite).

# Debe aceptar un número entero, limite, como argumento.

# La función debe devolver una nueva lista que contenga todos los números pares 
# desde el 0 hasta el limite (incluido).

# Pista: Inicializa una lista vacía. Luego, usa un bucle for con range() para recorrer los números. 
# Con un if, comprueba si el número es par y, si lo es, añádelo a la lista.

def generar_lista_pares(limite):
  lista_pares = []
  for ind in range(limite + 1):
    