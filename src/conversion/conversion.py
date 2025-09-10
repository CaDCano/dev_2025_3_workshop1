class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        return ((celsius * 9/5) + 32)
    
    def fahrenheit_a_celsius(self, fahrenheit):
        return ((fahrenheit - 32) * 5/9)
    
    def metros_a_pies(self, metros):
        return (metros*3.28084)
    
    def pies_a_metros(self, pies):
        return (pies/3.28084)
    
    def decimal_a_binario(self, decimal):
        return bin(decimal).replace("0b", "")

    def binario_a_decimal(self, binario):        
        decimal = int(binario, 2)
        return decimal

    def decimal_a_romano(self, numero):
        
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
    
    
    def romano_a_decimal(self, romano):
        
        romano = romano.upper()
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

    
    def texto_a_morse(self, texto):
        texto = texto.upper()
        morse_dict = {
            ".-": "A", "-...": "B", "-..": "D","-.-.": "C", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I",
            ".---": "J", "-.-": "K", ".-..": "L", "--": "M",
            "-.": "N", "---": "O", ".--.": "P", "--.-": "Q",
            ".-.": "R", "...": "S", "-": "T", "..-": "U",
            "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z", "/": " "
        }
        morse_code = []
        for char in texto:
            if char in morse_dict.values():
                morse_code.append([k for k, v in morse_dict.items() if v == char][0])
            elif char.isdigit():
                morse_code.append(char)
            else:
                morse_code.append("?")
        return " ".join(morse_code)
        

    
    def morse_a_texto(self, morse):
        morse_dict = {
            ".-": "A", "-...": "B", "-..": "D", "-.-.": "C",".": "E",
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
        return texto_decodificado
    