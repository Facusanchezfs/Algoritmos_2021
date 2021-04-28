Valores = {"": 0, "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

def romano_a_decimal(numero_romano):
 
    if numero_romano in Valores:
         return Valores[numero_romano]
 
    primero, segundo = map(romano_a_decimal, numero_romano[:2])
    if primero < segundo:
        return segundo - primero + romano_a_decimal(numero_romano[2:])
    else:
        return primero + romano_a_decimal(numero_romano[1:])

print(romano_a_decimal("XXI"))




