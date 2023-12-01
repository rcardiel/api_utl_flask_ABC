# Valida el código (si es numérico y de longitud 6).
def validar_matricula(matricula: str) -> bool:
    return (matricula.isnumeric() and len(matricula) == 6)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_nombre(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 30)

# Valida que los créditos estén entre 1 y 9.
def validar_apaterno(apaterno: str) -> bool:
    apaterno_texto = str(apaterno)
    if apaterno_texto.isnumeric():
        return (apaterno >= 1 and apaterno <= 9)
    else:
        return False