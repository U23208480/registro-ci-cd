# registro-ci-cd

Formulario de registro con pruebas automáticas, integración continua (CI) y despliegue continuo (CD) en GitHub Pages.

Autor: Juan César Retuerto Ibañez - U23208480

## Qué contiene
- `app/validacion.py`: reglas del formulario (nombre de 3 o más caracteres, correo válido, contraseña de 8 o más).
- `app/sitio.py` y `build.py`: generan el sitio estático. La ruta `/registro/` es el formulario.
- `tests/test_registro.py`: 5 pruebas automáticas.
- `.github/workflows/ci-cd.yml`: pruebas, build con artifact y publicación.

## Pipeline
1. **Pruebas automáticas** (`pytest`) en cada push y pull request.
2. **Build y artifact**: genera `dist/` y lo sube como artifact `sitio-dist`.
3. **CD**: solo en `main`, publica en GitHub Pages. Exige el secret `APP_SECRET`, que no está en el código.

## Ejecutar en local
```bash
pip install -r requirements.txt
python -m pytest
python build.py dist
```
