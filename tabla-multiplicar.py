#TABLA DE MULTIPLICAR

#pide un numero y muestra su tabla del 1 al 10


#a = int(input("ingrese un numero:  "))

#for i in range(0,11):
#  print(f"{a} x {i} = {a * i}")

lista = []

for a in range(12):
    lista.append(a)

print("tabla del 0")
for b in range(0,10):
    print(f"{lista[0]} x {b} = {lista[0]*b}")

print("tabla del 1")
for b in range(0,10):
    print(f"{lista[1]} x {b} = {lista[1]*b}")

print("tabla del 2")
for b in range(0,10):
    print(f"{lista[2]} x {b} = {lista[2]*b}")

print("tabla del 3")
for b in range(0,10):
    print(f"{lista[3]} x {b} = {lista[3]*b}")

print("tabla del 4")
for b in range(0,10):
    print(f"{lista[4]} x {b} = {lista[4]*b}")

print("tabla del 5")
for b in range(0,10):
    print(f"{lista[5]} x {b} = {lista[5]*b}")

print("tabla del 6")
for b in range(0,10):
    print(f"{lista[6]} x {b} = {lista[6]*b}")

