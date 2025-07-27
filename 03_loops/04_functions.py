### bloques de código reutilizables y parametrizazbles para hacer tareas especificas
""" 
# definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional
"""
# ejemplo de una función para imprimir en consola
""" 
def saludar():
  print("holi q tal")
saludar() 
"""


# ejemplo de una función con parametro
# el parametro es lo que acepta la función: {nombre}
# el argumento es lo que se le pasa a la función: "diego" 
""" 
def saludar_a(nombre):
  print(f"hola {nombre}")
saludar_a("diego")
saludar_a("toshi")
saludar_a("thiago")
""" 


# funciones con más parámetros
""" 
def la_suma(a, b):
  suma = a + b
  return suma

result = la_suma(2, 3)
print(result) """

# documentar las funciones con docstring

# def la_resta(a, b):
#   """Resta dos números y retorna el resultado"""
#   return a - b


# parámetros por defecto
""" 
def multiplicar(a, b = 2):
  return a * b
"""

# argumentos por posición
""" 
def describir_personas(nombre, edad, sexo):
  print(f"nombre => {nombre}   edad => {edad}   sexo => {sexo}")

describir_personas("diego", 34, "hombre")
"""

# argumentos por clave
# parametros nombrados
""" 
def persona(nombre = "diego", edad = 34, sexo = "hombre"):
  print(f"Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}")

persona()
"""