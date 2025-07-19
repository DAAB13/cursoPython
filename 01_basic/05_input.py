# la función input permite obtener datos del usuario a través de la consola

# print('hola, ¿como te llmas?')
# nombre = input()  # espera a que el usuario escriba algo y presione enter
# print(f'Hola {nombre}, encantado de conocerte!')

nombre = input('hola, ¿Cómo te llmas?\n')
print(f'Hola {nombre}, encantado de conocerte!')   

age = input("¿Cuántos años tienes?\n")
print(f"asi que tienes {age} años, ¡genial!")

country, city = input("¿En que pais y ciudad vives?\n").split()
print(f"asi que vives en {city}, {country}, ¡que interesante!")
