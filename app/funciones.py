import json
from typing import Optional, Dict, List

import requests

RUTA_FAVORITOS = "data/favoritos.json"


def buscar_pokemon(nombre: str) -> Optional[Dict]:
    """
    Busca un Pokémon en la PokéAPI y devuelve un diccionario con sus datos.
    Args:
        nombre (str): Nombre o ID del Pokémon.
    Returns:
        dict | None: Datos del Pokémon o None si no se encuentra.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"

    try:
        response = requests.get(url, timeout=5)

        # Si no existe el Pokémon
        if response.status_code == 404:
            print("Pokémon no encontrado.")
            return None

        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as e:
        print(f"Error de HTTP: {e}")
        return None

    except requests.exceptions.RequestException:
        print("Error de conexión con la API.")
        return None

    # Convertimos la respuesta en un diccionario
    pokemon = {
        "id": data["id"],
        "nombre": data["name"],
        "altura": data["height"] / 10,
        "peso": data["weight"] / 10,
        "tipos": [t["type"]["name"] for t in data["types"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
    }

    print(f"\nPokémon encontrado: {pokemon['nombre'].capitalize()}")
    print(f"ID: {pokemon['id']}")
    print("Tipos:", ", ".join(pokemon["tipos"]))
    print("Stats:", pokemon["stats"])

    return pokemon

def cargar_favoritos() -> List[Dict]:
    """
    Carga los Pokémon favoritos desde el archivo JSON.
    Returns:
        list: Lista de Pokémon favoritos.
    """
    try:
        with open(RUTA_FAVORITOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_favorito(pokemon: Dict) -> None:
    """
    Guarda un Pokémon en la lista de favoritos.
    Args:
        pokemon (dict): Datos del Pokémon.
    """
    favoritos = cargar_favoritos()

    # Comprobar si ya está guardado por ID
    if any(p["id"] == pokemon["id"] for p in favoritos):
        print("Ese Pokémon ya está en favoritos.")
        return

    favoritos.append(pokemon)

    with open(RUTA_FAVORITOS, "w", encoding="utf-8") as f:
        json.dump(favoritos, f, indent=4, ensure_ascii=False)

    print("Pokémon guardado en favoritos.")

def eliminar_favorito(valor: str) -> None:
    """
    Elimina un Pokémon favorito por ID o por nombre.
    Args:
        valor (str): ID numérico o nombre del Pokémon a eliminar.
    """
    favoritos = cargar_favoritos()

    if not favoritos:
        print("No hay un Pokémon guardados en favoritos.")
        return

    valor_num = None  # Valor por defecto

    try:
        valor_num = int(valor)
        eliminar_por_id = True
    except ValueError:
        eliminar_por_id = False

    if eliminar_por_id:
        nuevos_fav = [p for p in favoritos if p["id"] != valor_num]
    else:
        valor = valor.lower()
        nuevos_fav = [p for p in favoritos if p["nombre"].lower() != valor]

    if len(nuevos_fav) == len(favoritos):
        print("No se encontró un Pokémon con ese ID o nombre.")
        return

    with open(RUTA_FAVORITOS, "w", encoding="utf-8") as f:
        json.dump(nuevos_fav, f, indent=4, ensure_ascii=False)

    print("Pokémon eliminado de favoritos.")