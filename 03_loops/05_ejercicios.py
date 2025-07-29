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

""" 
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
"""

### Ejercicio 2: Generador de Listas
# Objetivo: Usar un bucle for y range dentro de una función para crear y devolver una lista.

# Enunciado:
# Escribe una función llamada generar_lista_pares(limite).

# Debe aceptar un número entero, limite, como argumento.

# La función debe devolver una nueva lista que contenga todos los números pares 
# desde el 0 hasta el limite (incluido).

# Pista: Inicializa una lista vacía. Luego, usa un bucle for con range() para recorrer los números. 
# Con un if, comprueba si el número es par y, si lo es, añádelo a la lista.
""" 
def generar_lista_pares(limite):
  lista_pares = []
  for ind in range(limite + 1):
    if ind % 2 == 0:
      lista_pares.append(ind)
  return lista_pares

lista_hasta_10 = generar_lista_pares(10)
print(lista_hasta_10)
"""
""" 
def otra_forma_lista(limite):
  return list(range(0, limite + 1, 2))
lista_hasta_13 = otra_forma_lista(13)
print(lista_hasta_13)
"""

# Ejercicio 3: Petición de Edad Válida
# Objetivo: Combinar while True, input() y try-except 
# dentro de una función para crear un validador de entradas de usuario robusto.

# Enunciado:
# Escribe una función llamada pedir_edad().
# La función no debe aceptar ningún argumento.
# Debe pedirle al usuario que introduzca su edad con el mensaje: "Por favor, introduce tu edad: ".
# El bucle debe repetirse hasta que el usuario introduzca un número entero válido.

# Si el usuario introduce algo que no es un número (ej. "hola"), el programa debe imprimir 
# "Error: Debes introducir un número entero." y volver a preguntar.

# Una vez que el usuario introduce una edad válida, la función debe devolver ese número como un entero.

# Pista: Usa un bucle while True. Dentro, usa un bloque try para intentar convertir la entrada del input() a int. 
# Si falla, el bloque except ValueError se activará. Si tiene éxito, usa return para devolver el número y salir del bucle.

""" 
print("---AGE---")
def pedir_edad():
  while True:
    try:
      respuesta = int(input("Por favor, introduce tu edad: "))
      return respuesta
    except ValueError:
      print("Error: Debes introducir un número entero")
edad_obtenida = pedir_edad()
print(f"¡Gracias! Tu edad es {edad_obtenida} años.") """



### Ejercicio 4: Contador de Vocales
# Objetivo: Recorrer una cadena de texto (que es como una lista de caracteres) dentro de una función.

# Enunciado:
# Escribe una función llamada contar_vocales(texto).
# Debe aceptar una cadena de texto como argumento.

# La función debe devolver el número total de vocales (a, e, i, o, u) que contiene el texto,
# sin diferenciar entre mayúsculas y minúsculas.

# Pista: Crea una variable contador en cero. Recorre cada letra del texto con un bucle for. 
# Para hacer la comparación más fácil, convierte cada letra a minúscula con .lower(). 
# Luego, comprueba si esa letra está en una cadena o lista de vocales como "aeiou".

""" 
def contar_vocales(texto):
  contador = 0
  vocales = "aeiou"
  for letra in texto:
    if letra in vocales:
      contador += 1
  return contador

total_vocales = contar_vocales("hola thiaguito, como estas?")
print(total_vocales)
"""








### Ejercicio 5: Adivina el Número
# Objetivo: Practicar la lógica de un juego simple con un bucle while y 
# condiciones if/elif/else dentro de una función.

# Enunciado:
# Escribe una función llamada juego_adivina(numero_secreto).
# Debe aceptar un número entero numero_secreto como argumento.
# La función debe pedir al usuario que adivine el número.

# Mientras el usuario no adivine el número, el programa debe darle pistas, 
# indicando si el número secreto es "mayor" o "menor" que el intento.

# Cuando el usuario adivine el número, el programa debe imprimir "¡Felicidades, has adivinado!" y 
# la función debe terminar.

# Pista: Usa un bucle while que se ejecute mientras el intento del usuario sea diferente del numero_secreto. 
# No te olvides de convertir la entrada del usuario (input) a un número entero.

def juego_adivina(numero_secreto):
  while True:
    try:
      intento = int(input("Adivina el número secreto: "))
      if intento < numero_secreto:
        print("El número secreto es mayor. ¡Sigue intentando!")
      elif intento > numero_secreto:
        print("El número secreto es menor. ¡Sigue intentando!")
      else:
        print("felicidades, has adivniado")
        break
    except ValueError:
      print("Error: debes introducir un número valido")
    
num_oculto = 23
juego_adivina(num_oculto)