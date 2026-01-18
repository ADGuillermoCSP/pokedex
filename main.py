from app.colores import CIAN, RESET, AMARILLO, ROJO, MAGENTA, VERDE
from app.funciones import buscar_pokemon, cargar_favoritos, guardar_favorito, eliminar_favorito
from app.io import mostrar_menu, pedir_opcion


def main():
    """
    Punto de entrada al programa. Ejecuta un menú interactivo en bucle.
    """
    while True:
        # Mostrar menú principal
        mostrar_menu()

        #Leer opción del usuario
        opcion = pedir_opcion()

        # ------------------------------
        # Opción 1: Buscar Pokémon
        # ------------------------------
        if opcion == "1":
            nombre = input(f"{CIAN}Introduce nombre o ID del Pokémon:{RESET} ").strip()

            # Validación de entrada vacía
            if not nombre:
                print(f"{ROJO}Debes escribir un nombre o un ID válido.{RESET}")
                continue

            # Buscar Pokémon usando la API
            pokemon = buscar_pokemon(nombre)

            # Si no encuentra el Pokémon, vuelve al menú
            if not pokemon:
                input(f"{AMARILLO}Pulsa ENTER para volver al menú...{RESET}")
                continue

            # Preguntar si quiere guardarlo como favorito
            while True:
                guardar = input("\n¿Quieres guardar este Pokémon en favoritos? (s/n): ").strip().lower()

                if guardar == "s":
                    guardar_favorito(pokemon)
                    break
                elif guardar == "n":
                    print(f"{AMARILLO}No se guardó el Pokémon en favoritos.{RESET}")
                    break
                else:
                    print(f"{ROJO}Por favor, introduce 's' para sí o 'n' para no.{RESET}")

        # ------------------------------
        # Opción 2: Mostrar favoritos
        # ------------------------------
        elif opcion == "2":
            favoritos = cargar_favoritos()

            if favoritos:
                print(f"\n{MAGENTA}--- Pokémon Favoritos ---{RESET}")
                for p in favoritos:
                    print(f"\n{CIAN}--- {p['nombre'].capitalize()} ---{RESET}")
                    print(f"ID: {p['id']}")
                    print(f"Altura: {p['altura']} m")
                    print(f"Peso: {p['peso']} kg")
                    print("Tipos:", ", ".join(p["tipos"]))
                    print("Stats:", p["stats"])
            else:
                print(f"\n{AMARILLO}No hay Pokémon guardados en favoritos.{RESET}")

        # ------------------------------
        # Opción 3: Eliminar favorito
        # ------------------------------
        elif opcion == "3":
            favoritos = cargar_favoritos()

            if not favoritos:
                print(f"\n{AMARILLO}No hay Pokémon guardados en favoritos.{RESET}")
            else:
                print(f"\n{MAGENTA}--- Pokémon Favoritos ---{RESET}")
                for p in favoritos:
                    print(f"ID: {p['id']} | Nombre: {p['nombre'].capitalize()}")

                print(f"\n{CIAN}Puedes eliminar un Pokémon por ID o por nombre{RESET}")
                valor = input("Introduce el ID o nombre del Pokémon a eliminar: ").strip()

                eliminar_favorito(valor)

        # ------------------------------
        # Opción 4: Salir del programa
        # ------------------------------
        elif opcion == "4":
            print(f"{VERDE}Saliendo del programa...{RESET}")
            break

        # ------------------------------
        # Opción inválida
        # ------------------------------
        else:
            print(f"{ROJO}Opcion no válida.{RESET}")

        input(f"\n{AMARILLO}Pulsa ENTER para continuar...{RESET}")


if __name__ == '__main__':
    main()