# CONTADOR INTELIGENTE


lista = []

for a in range(51):
  lista.append(a)


for elemento in lista:
  if elemento % 3 == 0 and elemento % 5 == 0:
    print(f"{elemento} es FizzBuzz")
  elif elemento % 5 == 0:
    print(f"{elemento} es Buzz")
  elif elemento % 3 == 0:
    print(f"{elemento} es Fizz")
  else:
    print(elemento)



