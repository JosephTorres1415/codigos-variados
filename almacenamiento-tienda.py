class Producto:
  def __init__ (self,nombre,precio,cantidad):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad


class Inventario:
  def __init__(self,nombre):
    self.nombre = nombre
    self.productos = []




  def agregar_productos(self,producto):
    self.productos.append(producto)

  def ver_productos(self):
    for producto in self.productos:
      print("nombre", producto.nombre)
      print("precio", producto.precio)
      print("cantidad",producto.cantidad)

  def eliminar_producto(self,nombre):
    for producto in self.productos:
      if producto.nombre == nombre:
        self.productos.remove(producto)

  def actualizar_precio(self,nombre,nuevo_precio):
    for producto in self.productos:
      if producto.nombre == nombre:
        producto.precio = nuevo_precio

  def valor_total_del_inventario(self):

    total = 0
    for producto in self.productos:
        total += producto.precio * producto.cantidad
    return total



p = Producto("leche",10,5)
b = Producto("cafe",10,5)
i = Inventario("bodega")
i.agregar_productos(p)
i.agregar_productos(b)
i.ver_productos()

print("----------------")

print(i.valor_total_del_inventario())

print("----------------")

i.eliminar_producto("leche")
i.ver_productos()

print("----------------")

i.actualizar_precio("cafe",20)
i.ver_productos()

