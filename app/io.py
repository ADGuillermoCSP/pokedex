from app.colores import MAGENTA, RESET, CIAN


def mostrar_menu() -> None:
    """
    Muestra el menú principal de la aplicación.
    """
    print(f"\n{MAGENTA}====== POKEDEX ======{RESET}")
    print(f"{CIAN}1. Buscar Pokémon")
    print("2. Ver favoritos")
    print("3. Eliminar favoritos")
    print("4. Salir")
    print(f"{MAGENTA}======================={RESET}")

def pedir_opcion() -> str:
    """
    Pide una opción al usuario y la devuelve.
    Returns:
         str: Opción seleccionada.
    """
    return input("Selecciona una opción: ").strip()