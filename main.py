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
            while True:
                if pokemon:
                    guardar = input("\n¿Quieres guardar este Pokémon en favoritos? (s/n): ").strip().lower()

                    if guardar == "s":
                        guardar_favorito(pokemon)
                        break
                    elif guardar == "n":
                        print("No se guardó el Pokémon en favoritos.")
                        break
                    else:
                        print("Por favor, introduce 's' para sí o 'n' para no.")

        elif opcion == "2":
            favoritos = cargar_favoritos()
            if favoritos:
                print("\n--- Pokémon Favoritos ---")
                for p in favoritos:
                    print(f"\n--- {p['nombre'].capitalize()} ---")
                    print(f"ID: {p['id']}")
                    print(f"Altura: {p['altura']} m")
                    print(f"Peso: {p['peso']} kg")
                    print("Tipos:", ", ".join(p["tipos"]))
                    print("Stats:", p["stats"])
            else:
                print("\nNo hay Pokémon guardados en favoritos.")

        elif opcion == "3":
            id_poke = input("Introduce el ID a eliminar: ")
            eliminar_favorito(id_poke)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no válida.")

        input("\nPulsa ENTER para continuar...")


if __name__ == '__main__':
    main()