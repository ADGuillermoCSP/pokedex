def mostrar_menu() -> None:
    """
    Muestra el menú principal de la aplicación.
    """
    print("\n====== POKEDEX ======")
    print("1. Busca Pokémon")
    print("2. Ver favoritos")
    print("3. Eliminar favoritos")
    print("4. Salir")
    print("=======================")

def pedir_opcion() -> str:
    """
    Pide una opción al usuario y la devuelve.
    Returns:
         str: Opción seleccionada.
    """
    return input("Selecciona una opción: ").strip()