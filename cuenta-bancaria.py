class Cuenta_Bancaria:
  def __init__(self,titular,saldo):
    self.titular = titular
    self.__saldo = saldo

  def depositar(self):
    deposito = int(input("ingrese el monto a depositar"))
    self.__saldo += deposito

  def retirar(self):
    retiro = int(input("ingrese el monto a retirar"))
    if retiro <= self.__saldo:
       self.__saldo -= retiro
  def ver_saldo(self):
    print(f"el saldo de {self.titular} es de {self.__saldo}")


  a = input("ingrese el nombre del titular:")
  b = int(input("ingrese el saldo del titular"))
  p1 = Cuenta_Bancaria(a,b)

while True:

  print("----MENU----")
  print("1. depositar")
  print("2. retirar")
  print("3. ver saldo")
  print("4. salir")

  opcion = input("ingrese un numero: ")

  if opcion == "1":

    p1.depositar()



  elif opcion == "2":

    p1.retirar()


  elif opcion == "3":

    p1.ver_saldo()

  elif opcion == "4":
    break
  else :
    print("ingrese una opcion valida")



