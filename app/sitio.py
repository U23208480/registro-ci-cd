from app.validacion import LARGO_MIN_CLAVE, LARGO_MIN_NOMBRE

ESTILO = (
    "body{font-family:Arial,sans-serif;max-width:420px;margin:40px auto;padding:0 16px}"
    "label{display:block;margin-top:12px}input{width:100%;padding:8px;box-sizing:border-box}"
    "button{margin-top:16px;padding:10px 16px}#mensaje{margin-top:16px;font-weight:bold}"
)

SCRIPT = """
document.getElementById('form-registro').addEventListener('submit', function (e) {
  e.preventDefault();
  document.getElementById('mensaje').textContent = 'Registro enviado correctamente.';
});
"""


def pagina_inicio():
    return (
        "<!doctype html><html lang='es'><head><meta charset='utf-8'>"
        "<title>Inicio</title><style>" + ESTILO + "</style></head><body>"
        "<h1>Aplicación de registro</h1>"
        "<p><a href='registro/'>Ir al formulario de registro</a></p>"
        "</body></html>"
    )


def pagina_registro():
    return (
        "<!doctype html><html lang='es'><head><meta charset='utf-8'>"
        f"<title>Registro</title><style>{ESTILO}</style></head><body>"
        "<h1>Registro</h1>"
        "<form id='form-registro'>"
        f"<label>Nombre<input name='nombre' required minlength='{LARGO_MIN_NOMBRE}'></label>"
        "<label>Correo<input name='correo' type='email' required></label>"
        f"<label>Contraseña<input name='clave' type='password' required minlength='{LARGO_MIN_CLAVE}'></label>"
        "<button type='submit'>Registrarme</button>"
        f"</form><p id='mensaje'></p><script>{SCRIPT}</script></body></html>"
    )
