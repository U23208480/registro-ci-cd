from app.validacion import validar_registro
from build import construir


def test_registro_valido_no_tiene_errores():
    assert validar_registro("Juan Retuerto", "juan@utp.edu.pe", "clave1234") == []


def test_nombre_corto_es_rechazado():
    errores = validar_registro("Jo", "juan@utp.edu.pe", "clave1234")
    assert "El nombre debe tener al menos 3 caracteres." in errores


def test_correo_invalido_es_rechazado():
    errores = validar_registro("Juan Retuerto", "correo-sin-arroba", "clave1234")
    assert "El correo no es válido." in errores


def test_clave_de_8_caracteres_es_aceptada_y_de_7_rechazada():
    assert validar_registro("Juan Retuerto", "juan@utp.edu.pe", "12345678") == []
    errores = validar_registro("Juan Retuerto", "juan@utp.edu.pe", "1234567")
    assert "La contraseña debe tener al menos 8 caracteres." in errores


def test_build_publica_la_ruta_registro_con_formulario(tmp_path):
    raiz = construir(str(tmp_path / "dist"))
    html = (raiz / "registro" / "index.html").read_text(encoding="utf-8")
    assert "<form id='form-registro'>" in html
    assert "name='correo' type='email'" in html
    assert (raiz / "version.txt").exists()
