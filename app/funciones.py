from typing import Optional, Dict, List


def buscar_pokemon(nombre: str) -> Optional[Dict]:
    """
    Busca un Pokémon en la API.
    Args:
        nombre (str): Nombre o ID del Pokémon.
    Returns:
        dict | None: Datos del Pokémon o None si no se encuentra.
    """
    pass

def cargar_favoritos() -> List[Dict]:
    """
    Carga los Pokémon favoritos desde el archivo JSON.
    Returns:
        list: Lista de Pokémon favoritos.
    """
    pass

def guardar_favorito(pokemon: Dict) -> None:
    """
    Guarda un Pokémon en la lista de favoritos.
    Args:
        pokemon (dict): Datos del Pokémon.
    """
    pass

def eliminar_favorito(id_pokemon: str) -> None:
    """
    Elimina un Pokémon favorito por ID.
    Args:
        id_pokemon (str): ID del Pokémon a eliminar.
    """
    pass