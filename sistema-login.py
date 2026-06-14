#SISTEMA LOGIN

class Usuario:
  def __init__(self,nombre,contraseña):
    self.nombre = nombre
    self.contraseña = contraseña



class Login:
  def __init__(self,):
    self.usuarios = []

  def agregar_usuarios(self,usuario):
    self.usuarios.append(usuario)




  def login(self, nombre, contraseña):
    for usuario in self.usuarios:
        if usuario.nombre == nombre:
            if usuario.contraseña == contraseña:
                print("Login correcto")
                return True
            else:
                print("Contraseña incorrecta")
                return False

    print("Usuario no encontrado")
    return False





print("REGISTRATE")
print("--------------------------")
a = input("ingrese el nombre de usuario: ")
b = input("ingrese la contraseña: ")

usuario1 = Usuario(a,b)
usuario2 = Usuario("juan","hola2")

i = Login()
i.agregar_usuarios(usuario1)
i.agregar_usuarios(usuario2)

intentos = 0

while True:

  print("----MENU----")
  print("1. login")
  print("2. salir")
  print("---------------------------")

  opcion = input("ingrese un numero: ")

  print("---------------------------")

  if opcion == "1":
   intentos = 0
   while True:

      user = input("ingrese el nombre de usuario: ")
      contra = input("ingrese la contraseña: ")

      intentos += 1
      if i.login(user,contra) and intentos < 3 :
        print("pasaste")
        break

      elif intentos == 3:
        print("se acabaron los intentos")
        break

  elif opcion == "2":
    break

  else :
    print("ingrese una opcion valida")




