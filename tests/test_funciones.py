import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.funciones import cargar_favoritos, guardar_favorito, eliminar_favorito

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

def test_guardar_favorito_no_duplicados():
    reset_favoritos()
    pokemon_prueba = {
        "id": 500,
        "nombre": "duplicatemon",
        "altura": 1.2,
        "peso": 12.0,
        "tipos": ["fire"],
        "stats": {"hp": 60, "attack": 60, "defense": 60}
    }

    # Guardamos el Pokémon dos veces
    guardar_favorito(pokemon_prueba)
    guardar_favorito(pokemon_prueba)  #Intento duplicado

    # Comprobamos que solo hay uno
    favoritos = cargar_favoritos()
    assert len(favoritos) == 1
    assert favoritos[0]["id"] == 500

# ----------------------------
# Test eliminar_favorito
# ----------------------------
def test_eliminar_favorito_existente():
    reset_favoritos()
    pokemon_prueba = {
        "id": 777,
        "nombre": "deletemon",
        "altura": 0.7,
        "peso": 13.0,
        "tipos": ["dark"],
        "stats": {"hp": 40, "attack": 40, "defense": 40}
    }

    # Guardamos Pokémon
    guardar_favorito(pokemon_prueba)

    # Eliminamos Pokémon por ID
    eliminar_favorito("777")

    # Comprobamos que favoritos está vacío
    favoritos = cargar_favoritos()
    assert len(favoritos) == 0