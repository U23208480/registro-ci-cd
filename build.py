import hashlib
import os
import pathlib
import sys

from app.sitio import pagina_inicio, pagina_registro


def construir(destino="dist"):
    raiz = pathlib.Path(destino)
    (raiz / "registro").mkdir(parents=True, exist_ok=True)
    (raiz / "index.html").write_text(pagina_inicio(), encoding="utf-8")
    (raiz / "registro" / "index.html").write_text(pagina_registro(), encoding="utf-8")
    secreto = os.environ.get("APP_SECRET", "")
    commit = os.environ.get("GITHUB_SHA", "local")
    huella = hashlib.sha256((secreto + commit).encode()).hexdigest()[:12]
    (raiz / "version.txt").write_text("commit=%s\nhuella=%s\n" % (commit[:7], huella))
    return raiz


if __name__ == "__main__":
    print("Sitio generado en", construir(sys.argv[1] if len(sys.argv) > 1 else "dist"))
