import random, string

def generar_numero_guia():
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    numeros = ''.join(random.choices(string.digits, k=8))
    return letras + numeros