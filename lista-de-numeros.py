#LISTA DE NUMERO

#crea una lista y muestra el mayor, menor y la suma total


import random

lista = []


for a in range(13):
  lista.append(random.randint(0,100))

lista.sort()

print(lista)

#for a in range(10):
#  lista.append(a)


total = sum(lista)

print(f"la suma de todo es {total}")
print(f"el menor es {lista[0]}")
print(f"el mayor es {lista[12]}")
