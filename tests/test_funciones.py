import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.funciones import cargar_favoritos, RUTA_FAVORITOS


# ----------------------------
# Test cargar_favoritos
# ----------------------------
def test_cargar_favoritos_devuelve_lista():
    # Limpiamos el archivo antes de probar
    with open(RUTA_FAVORITOS, "w", encoding="utf-8") as f:
        json.dump([], f)

    resultado = cargar_favoritos()
    assert isinstance(resultado, list)
    assert resultado == []