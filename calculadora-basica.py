
# Calculadora basica

# pide al usuario dos numeros y muestra la suma, resta, multiplicacion y divsion de esos numeros


a = float(input("ingrese un numero: "))
b = float(input("ingrese otro numero: "))


def operacion(a,b):
  def suma(a,b):
    return a + b
  def resta(a,b):
    return a - b
  def multiplicacion(a,b):
    return a * b
  def division(a,b):
    if b == 0:
      print("la division no se pudo realizar porque b es cero")
    elif b > 0:
      return a / b
    elif b < 0:
      return a / b
    else:
      print("ingresa un numero entero")
  return suma(a,b),resta(a,b),multiplicacion(a,b),division(a,b)





resultado = operacion(a,b)
print(f"la suma es:{resultado[0]}",
      f"la resta es:{resultado[1]}",
      f"la multiplicacion es:{resultado[2]}",
      f"la division es:{resultado[3]}")




