class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """

    def invertir_lista(self, lista):
        resultado = []
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        vistos = set()
        for elem in lista:
            clave = (elem, type(elem))
            if clave not in vistos:
                resultado.append(elem)
                vistos.add(clave)
        return resultado


    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado

    def rotar_lista(self, lista, k):
        n = len(lista)
        if n == 0:
            return lista
        k %= n
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1  # debería haber n números
        suma_total = n * (n + 1) // 2
        return suma_total - sum(lista)

    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            encontrado = False
            for x in conjunto2:
                if elem == x:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True

    def implementar_pila(self):
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            return pila.pop() if pila else None

        def peek():
            return pila[-1] if pila else None

        def is_empty():
            return len(pila) == 0

        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}

    def implementar_cola(self):
        cola = []
        def enqueue(x):
            cola.append(x)

        def dequeue():
            return cola.pop(0) if cola else None

        def peek():
            return cola[0] if cola else None

        def is_empty():
            return len(cola) == 0

        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}

    def matriz_transpuesta(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        transpuesta = []
        for j in range(columnas):
            fila = []
            for i in range(filas):
                fila.append(matriz[i][j])
            transpuesta.append(fila)
        return transpuesta
