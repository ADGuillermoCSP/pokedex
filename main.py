from app.funciones import buscar_pokemon, cargar_favoritos, guardar_favorito, eliminar_favorito
from app.io import mostrar_menu, pedir_opcion


def main():
    """
    Punto de entrada al programa. Ejecuta un menú interactivo en bucle.
    """
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            nombre = input("Introduce nombre o ID del Pokémon: ").strip()
            pokemon = buscar_pokemon(nombre)
            if pokemon:
                guardar = input("\n¿Quieres guardar este Pokémon en favoritos? (s/n): ").strip().lower()
                if guardar == "s":
                    guardar_favorito(pokemon)

        elif opcion == "2":
            cargar_favoritos()  # Aún sin implementar

        elif opcion == "3":
            id_poke = input("Introduce el ID a eliminar: ")
            eliminar_favorito(id_poke)  # Aún sin implementar

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no válida.")

        input("\nPulsa ENTER para continuar...")


if __name__ == '__main__':
    main()