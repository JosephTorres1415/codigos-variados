



n = int(input("introduzca la cantidad de elementos del vector: "))


m = []

v = []




def creacion_elementos(a,b,n):

    for i in range(n):
     i = int(input("introduzca los numeros del vector: "))
     a.append(i)

    for i in range(n):
      i = int(input("introduzca los numeros del vector: "))
      b.append(i)




# def imprimir_el_cuadrado_de_los_primeros_10_numeros_enteros():

  #for i in range(11):
    #v.append(i)

  #for i in range(len(v)):
     #v[i] = v[i]**2

def suma(a,b):

  c = []

  for i in range(len(a)):
    c.append(b[i] + a[i])

  return c

def resta(a,b):

  c = []

  for i in range(len(a)):
    c.append(b[i] - a[i])

  return c


def multiplicacion_escalar(a,b):

    suma = 0

    for i in range(len(a)):
        suma += a[i] * b[i]

    return suma


def division(a,b):

    c = []

    for i in range(len(a)):

        if b[i] == 0:
            c.append("No se puede dividir")
        else:
            c.append(a[i] / b[i])

    return c


creacion_elementos(v,m,n)


while True:
    print("------------------------------")
    print("MENU")
    print("------------------------------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion escalar")
    print("4. Division")
    print("5. Salir")


    print("///////////////////////////////////")
    opcion = int(input("Elija una opcion: "))
    print("///////////////////////////////////")

    if opcion == 1:
        print("-------------------------------")
        print(suma(v, m))
        print("-------------------------------")

        continuar = int(input("Desea continuar? 1 = si, 0 = no: "))

        if continuar == 1:
            continue

        if continuar == 0:
            break




    if opcion  == 2:

        print("-------------------------------")
        print(resta(v,m))
        print("-------------------------------")

        continuar = int(input("Desea continuar? 1 = si, 0 = no: "))

        if continuar == 1:
            continue

        if continuar == 0:
            break


    if opcion == 3:

        print("-------------------------------")
        print(multiplicacion_escalar(v,m))
        print("-------------------------------")

        continuar = int(input("Desea continuar? 1 = si, 0 = no: "))

        if continuar == 1:
            continue

        if continuar == 0:
            break

    if opcion == 4:

        print("-------------------------------")
        print(division(v,m))
        print("-------------------------------")

        continuar = int(input("Desea continuar? 1 = si, 0 = no: "))

        if continuar == 1:
            continue

        if continuar == 0:
            break


    if opcion == 5:
       break


