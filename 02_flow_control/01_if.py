"""
Sentencias condicionales (if, elif, else)
permite ejercutar bloques de código solo si se cumplen ciertas condiciones.
"""

import os
os.system("clear")
"""
print("\nSentencia simple condicional")
age = 18
if age >= 18:
  print("eres mayor de edad")
"""

"""
print("\nSentencia condicional con else")
age = 13
if age >= 18:
  print("eres mayor de edad")
else:
  print("eres menor de edad")
"""

""""
print("\nSentencia condicional con elif")
nota = 6

if nota >= 9:
  print("sobresaliente")
elif nota >= 7:
  print("notable")
elif nota >= 5:
  print("aprobado")
else:
  print("desaprobado")
"""

###condiciones multiples
""""
age = 10
tiene_Carnet = False

if age >= 18 and tiene_Carnet:
  print("puedes conducir")
else:
  print("no puedes conducir")

if age >= 18 or tiene_Carnet:
  print("puedes conducir")
else:
  print("llama a la policia")

fin_de_semana = True
if not fin_de_semana:
  print("puedes dormir hasta tarde")
else:
  print("debes ir a trabajar")
"""


"""
# print("anidar condicionales")
age = 19
tiene_dinero = True

if age >= 18:
  if tiene_dinero:
    print("puedes comprar una cerveza")
  else:
    print("mejorar ahorra dinero")
else:
  print("no puedes comprar una cerveza, eres menor de edad")


if age < 18:
  print("no puedes comprar una cerveza, eres menor de edad")
elif tiene_dinero:
  print("puedes comprar una cerveza")
else:
  print("mejorar ahorra dinero")
"""

#nunmber = 5
#if nunmber:
#  print("el número es positivo")

number = 0
if number:
  print("no entraras nunca")


#condicion ternaria
age = 17
mensaje = "eres mayor de edad" if age >= 18 else "eres menor de eedad"
print(mensaje)