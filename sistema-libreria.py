class Libro:
  def __init__ (self, titulo, autor, disponible=True):
    self.titulo = titulo
    self.autor = autor
    self.disponible = disponible


class Biblioteca:
  def __init__ (self,nombre):
    self.nombre = nombre
    self.libros = []

  def agregar_libro(self, libro):
        self.libros.append(libro)

  def prestar_libro(self,titulo,autor):
    for libro in self.libros:
      if libro.titulo == titulo and libro.autor == autor:
        if libro.disponible:
          libro.disponible = False
          print("prestar libro")

        else:
          print("el libro ya esta prestado")
        return

    print("No se encontró el libro")



  def devolver_libro(self, titulo, autor):
    for libro in self.libros:
      if libro.titulo == titulo and libro.autor == autor:
        libro.disponible = True
        print("libro devuelto")
        return
    print("no se encontro el libro")




  def mostrar_libro(self):
   for libro in self.libros:
      print(f"autor: {libro.titulo} - titulo: {libro.titulo} - estado: {libro.disponible}" )




biblioteca1 = Biblioteca("biblioteca1")
biblioteca1.agregar_libro(Libro("a1","b1"))
biblioteca1.agregar_libro(Libro("a2", "b2"))
biblioteca1.agregar_libro(Libro("a3", "b3"))



while True:
  print("----MENU----")
  print("1. prestar libro")
  print("2. devolver libro")
  print("3. mostrar libros")
  print("4. salir")
  print("---------------------")

  opcion = input("ingrese un numero: ")

  if opcion == "1":

    titulo = input("ingrese el titulo del libro: ")
    autor = input("ingrese el autor del libro: ")

    biblioteca1.prestar_libro(titulo,autor)


  elif opcion == "2":

    titulo = input("ingrese el titulo del libro: ")
    autor = input("ingrese el autor del libro: ")
    biblioteca1.devolver_libro(titulo, autor)

  elif opcion == "3":

    biblioteca1.mostrar_libro()

  elif opcion == "4":

    break








