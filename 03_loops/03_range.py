# Perimite crear un rango de números

"""
nums = range(2, 5) # no es una lista (inicio, fin)
print(nums) # = range(2, 5)
for nums in range(5, 10):
  print(nums)

for nums in range(0, 100, 5):  # (inicio, fin, paso)
  print(nums)


for nums in range(-5, 0):
  print(nums)

for n in range(10, 3, -1):
  print(n)


nums = range(10)
list_nums = list(nums)
print(list_nums)
"""


#### hacerlo 5 veces
contador = 0
while contador <= 5:
  print("se hizo 5 veces")
  contador += 1

#----------------
# mejor manera
for _ in range(6): # "_" es una variable que no se usa
  print("fueron 6 ")
