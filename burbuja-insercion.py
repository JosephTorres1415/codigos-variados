def burbuja(lista):
    arr = lista.copy()
    n = len(arr)
    intercambios = 0

    print("=== ORDENAMIENTO POR BURBUJA ===")
    print("Inicial:", arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1

        print(f"Pasada {i + 1}: {arr}")

    print("Resultado:", arr)
    print("Intercambios realizados:", intercambios)
    print()

    return arr


def insercion(lista):
    arr = lista.copy()
    desplazamientos = 0

    print("=== ORDENAMIENTO POR INSERCIÓN ===")
    print("Inicial:", arr)

    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            desplazamientos += 1
            j -= 1

        arr[j + 1] = clave

        print(f"Inserción {i}: {arr}")

    print("Resultado:", arr)
    print("Desplazamientos realizados:", desplazamientos)
    print()

    return arr


# Programa principal
datos = [85, 42, 97, 23, 61, 15, 74]

burbuja(datos)
insercion(datos)