def decimal_a_binario(numero):
 
    if numero == 0:
        return ""
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)


print(decimal_a_binario(25))
