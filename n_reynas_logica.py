from itertools import combinations


class ProblemaReinas:

    def __init__(self, n_reinas, n_tablero):
        self.n_reinas = n_reinas
        self.n_tablero = n_tablero

    def es_seguro(self, posiciones):
        """Verifica si ninguna reina se ataca"""

        for i in range(len(posiciones)):
            f1, c1 = posiciones[i]

            for j in range(i + 1, len(posiciones)):
                f2, c2 = posiciones[j]

                if (
                    f1 == f2 or
                    c1 == c2 or
                    abs(f1 - f2) == abs(c1 - c2)
                ):
                    return False

        return True

    def resolver(self):
        """Genera todas las combinaciones y conserva las válidas"""

        todas_las_posiciones = [
            (fila, columna)
            for fila in range(self.n_tablero)
            for columna in range(self.n_tablero)
        ]

        soluciones = []

        for combinacion in combinations(todas_las_posiciones, self.n_reinas):

            if self.es_seguro(combinacion):
                soluciones.append(combinacion)

        return soluciones

    def mostrar_tablero(self, solucion):
        """Muestra una solución en forma de tablero"""

        print("   ", end="")

        for col in range(self.n_tablero):
            print(col, end=" ")

        print("\n")

        for fila in range(self.n_tablero):

            print(fila, end="  ")

            for columna in range(self.n_tablero):

                if (fila, columna) in solucion:
                    print("♛", end=" ")
                else:
                    print(".", end=" ")

            print()


# ------------------------
# PROGRAMA PRINCIPAL
# ------------------------

print("=" * 50)
print("PROBLEMA DE LAS N REINAS")
print("=" * 50)

n = int(input("Ingrese el tamaño del tablero N (NxN): "))
k = int(input("Ingrese la cantidad de reinas: "))

if k > n:
    print("La cantidad de reinas no puede ser mayor que N.")
else:

    problema = ProblemaReinas(k, n)

    print("\nBuscando soluciones...\n")

    soluciones = problema.resolver()

    print(f"Total de soluciones encontradas: {len(soluciones)}")

    if len(soluciones) > 0:

        for numero_solucion, solucion in enumerate(soluciones, start=1):

            print("\n" + "=" * 40)
            print(f"SOLUCIÓN {numero_solucion}")
            print("=" * 40)

            problema.mostrar_tablero(solucion)

            print("\nCoordenadas de las reinas:")

            for i, reina in enumerate(solucion, start=1):
                print(f"Reina {i}: {reina}")

            print()

    else:
        print("\nNo se encontraron soluciones.")

