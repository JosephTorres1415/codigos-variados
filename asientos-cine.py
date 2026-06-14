asientos = {
    "j" : [1,1,1,1,1,1],
    "k" : [1,1,1,1,1,1],
    "M" : [1,1,1,1,1,1],
    "N" : [1,1,1,1,1,1]
    }









def mostrar_asientos():


  print("--------ASIENTOS---------")

  for  fila, lista in asientos.items():
    print(fila.upper(), end="  ")
    for asiento in lista:
      if asiento == 1:
        print("□", end=" ")   # libre
      else:
        print("■", end=" ")   # ocupado
    print()

  print("--------------------------")




def reservar_multiple(entrada):
  lista = entrada.split()

  for asiento in lista:
    if len(asiento) >= 2:
       fila = asiento[0]


       try:
          col = int(asiento[1]) - 1
       except:
          print(f"❌ {asiento} inválido")
          continue

       if fila in asientos and  0 <= col < len(asientos[fila]):

          if asientos[fila][col] == 1:
            asientos[fila][col] = 0
            print(f"✅ {asiento} reservado")

          else:
            print(f"❌ {asiento} ocupado")

       else:
          print(f"❌ {asiento} no existe")

    else:
      print(f"❌ {asiento} inválido")




while True:
    mostrar_asientos()

    opcion = input("\n1. Reservar\n2. Salir\nSeleccione: ")

    if opcion == "1":
        entrada = input("Ingrese asientos (ej: j2 j3 k1): ").lower()
        reservar_multiple(entrada)

        if len(asiento) >= 2:
            fila = asiento[0]
            col = int(asiento[1]) - 1  # ajustar índice

            reservar(fila, col)
        else:
            print("❌ Formato inválido")

    elif opcion == "2":
        print("Saliendo...")
        break

    else:
        print("❌ Opción inválida")






