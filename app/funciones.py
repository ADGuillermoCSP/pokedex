import json
from typing import Optional, Dict, List

import requests

from app.colores import ROJO, RESET, VERDE, AMARILLO

# Ruta donde se guardan los Pokémon favoritos
RUTA_FAVORITOS = "data/favoritos.json"


def buscar_pokemon(nombre: str) -> Optional[Dict]:
    """
    Busca un Pokémon en la PokéAPI y devuelve un diccionario con sus datos.
    Args:
        nombre (str): Nombre o ID del Pokémon.
    Returns:
        dict | None: Datos del Pokémon o None si no se encuentra.
    """
    # Construimos la URL normalizando el nombre a minúsculas
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"

    try:
        # Solicitud a la API con timeout para evitar bloqueos
        response = requests.get(url, timeout=5)

        # Si no existe el Pokémon
        if response.status_code == 404:
            print(f"{ROJO}Pokémon no encontrado.{RESET}")
            return None

        # Si el código indica error (400–500), se lanzará excepción
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as e:
        print(f"{ROJO}Error de HTTP: {e}{RESET}")
        return None

    except requests.exceptions.RequestException:
        # Error genérico: problemas de red, timeout, DNS, etc.
        print(f"{ROJO}Error de conexión con la API.{RESET}")
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

    # Mostrar información
    print(f"\n{VERDE}Pokémon encontrado: {pokemon['nombre'].capitalize()}{RESET}")
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
        # Si el archivo existe, lo cargamos
        with open(RUTA_FAVORITOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si no existe o está corrupto, devolvemos una lista vacía
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
        print(f"{AMARILLO}Ese Pokémon ya está en favoritos.{RESET}")
        return

    favoritos.append(pokemon)

    # Guardado persistente en JSON
    with open(RUTA_FAVORITOS, "w", encoding="utf-8") as f:
        json.dump(favoritos, f, indent=4, ensure_ascii=False)

    print(f"{VERDE}Pokémon guardado en favoritos.{RESET}")

def eliminar_favorito(valor: str) -> None:
    """
    Elimina un Pokémon favorito por ID o por nombre.
    Args:
        valor (str): ID numérico o nombre del Pokémon a eliminar.
    """
    favoritos = cargar_favoritos()

    if not favoritos:
        print(f"{AMARILLO}No hay un Pokémon guardados en favoritos.{RESET}")
        return

    valor_num = None  # Valor por defecto

    # Intentar interpretar el valor como número (ID)
    try:
        valor_num = int(valor)
        eliminar_por_id = True
    except ValueError:
        # Si falla, eliminaremos por nombre
        eliminar_por_id = False

    # Buscar Pokémon antes de eliminarlo
    if eliminar_por_id:
        # Eliminación por ID
        pokemon_eliminado = next((p for p in favoritos if p["id"] == valor_num), None)
        nuevos_fav = [p for p in favoritos if p["id"] != valor_num]
    else:
        # Eliminación por nombre (ignorando mayúsculas)
        valor = valor.lower()
        pokemon_eliminado = next((p for p in favoritos if p["nombre"].lower() == valor), None)
        nuevos_fav = [p for p in favoritos if p["nombre"].lower() != valor]

    if pokemon_eliminado is None:
        # El Pokémon no está en la lista
        print(f"{ROJO}No se encontró un Pokémon con ese ID o nombre.{RESET}")
        return

    # Escribir la lista actualizada
    with open(RUTA_FAVORITOS, "w", encoding="utf-8") as f:
        json.dump(nuevos_fav, f, indent=4, ensure_ascii=False)

    print(f"{VERDE}Pokémon '{pokemon_eliminado['nombre'].capitalize()}' eliminado de favoritos.{RESET}")