
### ejercicio 1
# name = "Diego Alberto Alvarado Benel"
# city = "Lima"
# print(name)
# print(city)

# print(f"{name}\n{city}")

#name = input("escribe tu nombre\n")
#city = input("escribe tu ciudad\n")

#print("--- tus datos son: ---")
#print(f"{name}\n{city}")

#---------------------------------------

### ejercicio 2
"""
a = 15
b = 3.1416
c = "hola mundo"
d = True
e = None  

lista = [type(a), type(b), type(c), type(d), type(e)]
for t in lista:
    print(t)    
"""

### ejercicio 3
"""
cadena = "1234"
print(f"number es: '{cadena}'")

numero_entero = int(cadena)
print(f"numero entero es: {numero_entero}")

numero_float = float(numero_entero)
print(f"numero float es: {numero_float}")


cadena2 = "3.99"
print(f"cadena2 es : {cadena2}")

numero_float = float(cadena2)
print(f"numero float es: {numero_float}")

numero_entero = int(numero_float)
print(f"numero entero es: {numero_entero}")
"""

### Ejercicio 4
"""
name = "Diego Alberto Alvarado Benel"
age = 33
high = 1.71

print(f"hola a todos, me llamo {name}, tengo {age} de edad y mido {high} metros")
"""


### Ejercicio 5
import math
numero_pi = math.pi
print(f"El valor de pi es: {numero_pi}")

redondear = round(numero_pi)
print(f"el numero pi redondeado es: {redondear}")

division = redondear // 2
print(f"la division de {redondear} entre 2 es: {division}")