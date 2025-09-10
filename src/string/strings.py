class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """

    def es_palindromo(self, texto):
        """Verifica si una cadena es un palíndromo (ignora mayúsculas y espacios)."""
        texto_limpio = "".join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]

    def invertir_cadena(self, texto):
        """Invierte una cadena sin usar slicing ni reversed()."""
        invertida = ""
        for c in texto:
            invertida = c + invertida
        return invertida

    def contar_vocales(self, texto):
        """Cuenta el número de vocales en una cadena."""
        vocales = "aeiouáéíóú"
        return sum(1 for c in texto.lower() if c in vocales)

    def contar_consonantes(self, texto):
        """Cuenta el número de consonantes en una cadena."""
        vocales = "aeiouáéíóú"
        return sum(1 for c in texto.lower() if c.isalpha() and c not in vocales)

    def es_anagrama(self, texto1, texto2):
        """Verifica si dos cadenas son anagramas (ignora mayúsculas y espacios)."""
        t1 = sorted([c.lower() for c in texto1 if c.isalnum()])
        t2 = sorted([c.lower() for c in texto2 if c.isalnum()])
        return t1 == t2

    def contar_palabras(self, texto):
        """Cuenta el número de palabras en una cadena."""
        palabras = [p for p in texto.split(" ") if p.strip() != ""]
        return len(palabras)

    def palabras_mayus(self, texto):
        """Pone en mayúscula la primera letra de cada palabra."""
        palabras = texto.split()
        return " ".join(p[0].upper() + p[1:] if p else "" for p in palabras)

    def eliminar_espacios_duplicados(self, texto):
        """Elimina espacios duplicados dejando solo uno entre palabras."""
        resultado = []
        espacio_anterior = False
        for c in texto:
            if c == " ":
                if not espacio_anterior:
                    resultado.append(c)
                espacio_anterior = True
            else:
                resultado.append(c)
                espacio_anterior = False
        return "".join(resultado).strip()

    def es_numero_entero(self, texto):
        """Verifica si una cadena representa un número entero (con signo opcional)."""
        if not texto:
            return False
        if texto[0] in "+-":
            texto = texto[1:]
        return all(c.isdigit() for c in texto) and texto != ""

    def cifrar_cesar(self, texto, desplazamiento):
        """Aplica el cifrado César a una cadena de texto."""
        resultado = []
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                nuevo = (ord(c) - base + desplazamiento) % 26 + base
                resultado.append(chr(nuevo))
            else:
                resultado.append(c)
        return "".join(resultado)

    def descifrar_cesar(self, texto, desplazamiento):
        """Descifra una cadena con cifrado César."""
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        """Encuentra todas las posiciones de una subcadena sin find() ni index()."""
        posiciones = []
        n, m = len(texto), len(subcadena)
        if m == 0:
            return posiciones
        for i in range(n - m + 1):
            if texto[i:i+m] == subcadena:
                posiciones.append(i)
        return posiciones
