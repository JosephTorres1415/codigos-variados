class Estudiante:
  def __init__(self,nombre,notas):
    self.nombre = nombre
    self.notas = notas

  def agregar_nota(self,notas):
    self.notas.append(notas)

  def promedio(self):
    return sum(self.notas) / len(self.notas)

  def aprobar_o_no(self):
    if self.promedio() >= 11:
      print("aprobaste")

    else:
      print("no aprobaste")



nombre = input("ingrese el nombre del estudiante: ")

notas= []




while True:
    entrada = input("Ingrese un número (o 'fin'): ")

    if entrada == "fin":
        break

    try:
        notas.append(int(entrada))
    except:
        print("Dato inválido")



p1 = Estudiante(nombre,notas)
print("nombre: ", p1.nombre)
print("notas", p1.notas)
print("promedio", p1.promedio())
p1.aprobar_o_no()