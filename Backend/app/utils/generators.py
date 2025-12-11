import random, string

def generar_numero_guia():
    letras = ''.join(random.choices(string.ascii_uppercase, k=2))
    numeros = ''.join(random.choices(string.digits, k=8))
    return letras + numeros

def generar_flota():
    letras_inicio = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=4))
    letra_final = random.choice(string.ascii_uppercase)
    return letras_inicio + numeros + letra_final

def generar_placa():
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=3))
    return letras + numeros