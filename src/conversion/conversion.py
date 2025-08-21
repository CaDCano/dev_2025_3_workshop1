class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        return ((celsius * 9/5) + 32)
        
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        pass
    
    def fahrenheit_a_celsius(self, fahrenheit):
        
        fahrenheit = float(input("Ingrese la temperatura en fahrenheit: "))
        return ((fahrenheit - 32) * 5/9)
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        pass
    
    def metros_a_pies(self, metros):
        
        metros = float(input("Ingrese la distancia en metros: "))
        return (metros*3.28084)
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        pass
    
    def pies_a_metros(self, pies):
        pies = float(input("Ingrese la distancia en metros: "))
        return (pies/3.28084)
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        pass
    
    def decimal_a_binario(self, decimal):
        
        decimal = int(input("Ingrese un número decimal: "))
        return bin(decimal).replace("0b", "")
        
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
        pass
    
    def binario_a_decimal(self, binario):
        
        decimal = int(input("Ingrese un número binario: "), 2)
        return decimal
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """
        pass
    
    def decimal_a_romano(self, numero):
        
        numero = int(input("Ingrese un número decimal entre 1 y 3999: "))
        if numero < 1 or numero > 3999:
            raise ValueError("El número debe estar entre 1 y 3999")
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        resultado = ""
        for valor, simbolo in roman_numerals:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado
    
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        pass
    
    def romano_a_decimal(self, romano):
        
        romano = input("Ingrese un número romano válido: ").upper()
        roman_numerals = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        prev_value = 0
        for char in reversed(romano):
            value = roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
    
        """
        Convierte un número romano a decimal.
        
        Args:
            romano (str): Número romano válido
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            romano_a_decimal("IX") -> 9
            romano_a_decimal("MCMXCIV") -> 1994
        """
        pass
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        pass
    
    def morse_a_texto(self, morse):
        
        morse = input("Ingrese el código Morse separado por espacios: ")
        morse_dict = {
            ".-": "A", "-...": "B", "-..": "D", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I",
            ".---": "J", "-.-": "K", ".-..": "L", "--": "M",
            "-.": "N", "---": "O", ".--.": "P", "--.-": "Q",
            ".-.": "R", "...": "S", "-": "T", "..-": "U",
            "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z", "/": " "
        }
        texto_decodificado = ""
        for codigo in morse.split(" "):
            if codigo in morse_dict:
                texto_decodificado += morse_dict[codigo]
            else:
                texto_decodificado += "?"
        return "El texto decodificado es: ",texto_decodificado
    
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        pass