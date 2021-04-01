# Ejercicio 2
def suma_R(numero):
    if (numero == 0):
        return 0
    else:
        return (numero + (numero-1))

print (suma_R(3))

# Ejercicio 3

def multi_R(numero1, numero2):
    if (numero2 == 0 or numero1 == 0):
        return 0
    else:
        return (numero1 +(numero2-1))

print (multi_R(2, 4))