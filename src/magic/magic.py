class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """

    def fibonacci(self, n):
        """Calcula el n-ésimo número de la secuencia de Fibonacci."""
        if n < 0:
            raise ValueError("n debe ser un entero no negativo")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def secuencia_fibonacci(self, n):
        """Genera los primeros n números de la secuencia de Fibonacci."""
        if n < 0:
            raise ValueError("n debe ser un entero no negativo")
        secuencia = []
        a, b = 0, 1
        for _ in range(n):
            secuencia.append(a)
            a, b = b, a + b
        return secuencia

    def es_primo(self, n):
        """Verifica si un número es primo."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        """Genera una lista de números primos hasta n."""
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        """Verifica si un número es perfecto."""
        if n < 2:
            return False
        suma = sum(i for i in range(1, n) if n % i == 0)
        return suma == n

    def triangulo_pascal(self, filas):
        """Genera las primeras filas del triángulo de Pascal."""
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        """Calcula el factorial de un número."""
        if n < 0:
            raise ValueError("El factorial no está definido para negativos")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        """Calcula el máximo común divisor (Euclides)."""
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        """Calcula el mínimo común múltiplo."""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        """Calcula la suma de los dígitos de un número."""
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        """Verifica si un número es de Armstrong."""
        digitos = str(n)
        potencia = len(digitos)
        return sum(int(d) ** potencia for d in digitos) == n

    def es_cuadrado_magico(self, matriz):
        """Verifica si una matriz es un cuadrado mágico."""
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False  # No es cuadrada

        suma_objetivo = sum(matriz[0])

        # Filas y columnas
        for i in range(n):
            if sum(matriz[i]) != suma_objetivo or sum(matriz[j][i] for j in range(n)) != suma_objetivo:
                return False

        # Diagonales
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False

        return True
