# Pokedex

## Descripción
Pokedex es una aplicación de consola que permite buscar Pokémon usando la PokéAPI, guardar tus Pokémon favoritos, verlos
y eliminarlos.  
Los datos se guardan de forma persistente en un archivo JSON para que no se pierdan al cerrar la aplicación.  
Se incluyen mensajes coloreados para diferenciar información, advertencias y errores.

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/ADGuillermoCSP/pokedex.git
cd pokedex
```
2. Crear un entorno virtual
```bash
python -m venv venv
```

3. Activar el entorno virtual:  

Windows:
```bash
venv\Scripts\activate
```
Linux/macOS:
```bash
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

5. Ejecutar el programa desde la consola:
```
python main.py
```

## Uso
Al ejecutar `python main.py` aparecerá un menú con las siguientes opciones:

1. **Buscar Pokémon**: Introduce el nombre o ID de un Pokémon para obtener sus datos y decidir si guardarlo en favoritos.
2. **Ver favoritos**: Muestra los Pokémon guardados con ID, altura, peso, tipos y estadísticas.
3. **Eliminar favoritos**: Permite eliminar un Pokémon de los favoritos por ID o nombre.
4. **Salir**: Cierra la aplicación.

## Autor
Guillermo Amado Díaz