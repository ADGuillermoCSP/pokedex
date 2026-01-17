import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.funciones import cargar_favoritos, guardar_favorito

RUTA_TEST = "data/favoritos.json"


# ----------------------------
# Helpers para limpiar y restaurar
# ----------------------------
def reset_favoritos():
    """Borra el contenido de favoritos.json"""
    with open(RUTA_TEST, "w", encoding="utf-8") as f:
        json.dump([], f)

# ----------------------------
# Test cargar_favoritos
# ----------------------------
def test_cargar_favoritos_devuelve_lista():
    reset_favoritos()
    resultado = cargar_favoritos()
    assert isinstance(resultado, list)
    assert resultado == []

# ----------------------------
# Test guardar_favorito
# ----------------------------
def test_guardar_favorito_anade_pokemon():
    reset_favoritos()
    pokemon_prueba = {
        "id": 999,
        "nombre": "testmon",
        "altura": 1.0,
        "peso": 10.0,
        "tipos": ["normal"],
        "stats": {"hp": 50, "attack": 50, "defense": 50}
    }

    # Guardamos el Pokémon
    guardar_favorito(pokemon_prueba)

    # Comprobamos que está en favoritos
    favoritos = cargar_favoritos()
    assert len(favoritos) == 1
    assert favoritos[0]["id"] == 999
    assert favoritos[0]["nombre"] == "testmon"