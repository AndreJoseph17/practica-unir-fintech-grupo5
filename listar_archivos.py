import argparse
from pathlib import Path


def obtener_argumentos():
    parser = argparse.ArgumentParser(
        description="Lista archivos de una ruta en orden ascendente o descendente."
    )
    parser.add_argument("ruta", help="Ruta de la carpeta a listar")
    parser.add_argument(
        "--orden",
        choices=["asc", "desc"],
        default="asc",
        help="Orden de listado: asc o desc",
    )
    return parser.parse_args()


def listar_archivos(ruta, orden):
    carpeta = Path(ruta)

    if not carpeta.exists():
        print(f"La ruta no existe: {carpeta}")
        return

    if not carpeta.is_dir():
        print(f"La ruta no es una carpeta valida: {carpeta}")
        return

    archivos = sorted(
        [elemento.name for elemento in carpeta.iterdir() if elemento.is_file()],
        reverse=(orden == "desc"),
    )

    if not archivos:
        print("No se encontraron archivos en la ruta indicada.")
        return

    print(f"Archivos en {carpeta} ({'descendente' if orden == 'desc' else 'ascendente'}):")
    for archivo in archivos:
        print(archivo)


if __name__ == "__main__":
    argumentos = obtener_argumentos()
    listar_archivos(argumentos.ruta, argumentos.orden)
