import random


numero  = random.randint(1,100)
intentos = 0

while True:

  print("----ADIVINA EL NUMERO----")
  print("1. juego con 10 intentos")
  print("2. juego con 20 intentos")
  print("3. salir")

  print("---------------------------")

  try:
    opcion = int(input("ingrese un numero: "))
  except:
    print("ingrese un numero valido")
    continue

  print("---------------------------")

  if opcion == 1:
    print("---EL JUEGO YA EMPEZO----")
    intentos = 0
    while True:

      intentos += 1
      try:
         adivinar = float(input("ingrese un numero: "))

      except:
        print("ingrese un numero valido")
        continue
      print("--------------------")
      if intentos < 10:
          if adivinar == numero:
            print("--------------------")
            print(f"adivinaste en {intentos} intentos")
            print("--------------------")
            break
          elif adivinar < numero:
           print("--------------------")
           print("el numero es mayor")
           print("--------------------")
          elif adivinar > numero:
           print("--------------------")
           print("el numero es menor")
           print("--------------------")
          else:
            print("ingrese un numero valido")

          print(f"intentos usados {intentos}")
      else :
        print("se acabaron los intentos")
        break

  elif opcion == 2:
    print("---EL JUEGO YA EMPEZO----")
    intentos = 0
    while True:

      intentos += 1

      try:
         adivinar = float(input("ingrese un numero: "))
      except:
        print("ingrese un numero valido")
      continue
      if intentos < 20:
          if adivinar == numero:
            print(f"adivinaste en {intentos} intentos")
            break
          elif adivinar < numero:
           print("el numero es mayor")
          elif adivinar > numero:
           print("el numero es menor")
          else:
            print("ingrese un numero valido")
          print(f"intentos usados {intentos}")
      else :
        print("se acabaron los intentos")
        break
  elif opcion == "3":
    break
  else :
    print("ingrese una opcion valida")
