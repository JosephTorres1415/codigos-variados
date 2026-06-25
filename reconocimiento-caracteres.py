### RECONOCIMIENTO DE CARACTERES

texto = input("Ingrese un texto: ")

caracteres = 0
espacios = 0

for caracter in texto:
    caracteres += 1

    if caracter == " ":
        espacios += 1

palabras = espacios + 1

print("Caracteres:", caracteres)
print("Palabras:", palabras)
print("Espacios:", espacios)