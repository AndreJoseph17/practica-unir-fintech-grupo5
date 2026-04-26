import os
import subprocess
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OPCIONES = {
    "1": "opcion1.py",
    "2": "listar_archivos.py",
    "3": "opcion3.py",
    "4": "opcion4.py",
    "5": "opcion5.py",
    "6": "opcion6.py",
}


def ejecutar_archivo(nombre_archivo, argumentos=None):
    ruta_archivo = os.path.join(BASE_DIR, nombre_archivo)

    if not os.path.exists(ruta_archivo):
        print(f"\nNo se encontro el archivo: {nombre_archivo}")
        input("\nPresiona Enter para volver al menu...")
        return

    comando = [sys.executable, ruta_archivo]
    if argumentos:
        comando.extend(argumentos)

    subprocess.run(comando, check=False)
    input("\nPresiona Enter para volver al menu...")


def mostrar_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("MENU PRINCIPAL")
        print("1. Opcion 1")
        print("2. Opcion 2")
        print("3. Opcion 3")
        print("4. Opcion 4")
        print("5. Opcion 5")
        print("6. Opcion 6")
        print("0. Salir")

        opcion = input("\nSelecciona una opcion: ").strip()

        if opcion == "0":
            print("\nSaliendo del programa...")
            break

        archivo = OPCIONES.get(opcion)

        if archivo:
            if opcion == "2":
                ruta = input("\nIngresa la ruta a listar: ").strip()
                orden = input("Ingresa el orden (asc/desc): ").strip().lower()

                if orden not in ("asc", "desc"):
                    print("\nOrden no valido. Usa 'asc' o 'desc'.")
                    input("\nPresiona Enter para intentarlo de nuevo...")
                    continue

                ejecutar_archivo(archivo, [ruta, "--orden", orden])
            else:
                ejecutar_archivo(archivo)
        else:
            print("\nOpcion no valida.")
            input("\nPresiona Enter para intentarlo de nuevo...")


if __name__ == "__main__":
    mostrar_menu()
