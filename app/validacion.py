import re

LARGO_MIN_NOMBRE = 3
LARGO_MIN_CLAVE = 8
PATRON_CORREO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validar_registro(nombre, correo, clave):
    errores = []
    if len(nombre.strip()) < LARGO_MIN_NOMBRE:
        errores.append("El nombre debe tener al menos 3 caracteres.")
    if not PATRON_CORREO.match(correo.strip()):
        errores.append("El correo no es válido.")
    if len(clave) <= LARGO_MIN_CLAVE:
        errores.append("La contraseña debe tener al menos 8 caracteres.")
    return errores
