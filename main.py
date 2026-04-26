import os
import subprocess
import sys
import argparse


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OPCIONES = {
    "1": "opcion1.py",
    "2": "opcion2.py",
    "3": "listar_archivos.py",
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

def tarea_opcion_2_traduccion():
    """Muestra mensajes traducidos al inglés."""
    os.system("cls" if os.name == "nt" else "clear")
    print("--- OPTION 2: TRANSLATION TASK ---")
    print("Status: System is running correctly.")
    print("Message: All interface elements have been translated to English.")
    print("Action: Returning to main menu...")
    input("\nPress Enter to continue...")

def tarea_opcion_3_ordenamiento(orden_param=None):
    """Ordena una lista basada en un parámetro."""
    os.system("cls" if os.name == "nt" else "clear")
    words = ["banana", "apple", "cherry", "date"]
    print("Listado Inicial: {word}")    

    # Si no se pasa parámetro por comando, lo pedimos por teclado
    if not orden_param:
        print("--- OPTION 3: SORTING TASK ---")
        orden_param = input("Select order (asc/desc): ").strip().lower()

    is_reverse = True if orden_param == "desc" else False
    result = sorted(words, reverse=is_reverse)

    print(f"\nOrder selected: {'Descending' if is_reverse else 'Ascending'}")
    print(f"Sorted list: {result}")
    input("\nPress Enter to return to menu...")

def mostrar_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("MENU PRINCIPAL")
        print("1. Op. Traducir los mensajes que se imprimen por pantalla al inglés")
        print("2. Op. Aceptar un nuevo parámetro de línea de comandos que indique si el orden debe ser asc o desc.")
        print("3. Op. Aceptar un nueva ruta y un param. que indique si el orden debe ser asc o desc.")
        print("4. Op. Añadir una directiva en el Makefile que ejecute el comando en local, sin arrancar un contenedor de Docker")
        print("5. Op. Añadir un fichero de ejemplo, palabras.txt, que incluya varias palabras desordenadas, una por línea, y modificar el Makefile para que use el nombre del fichero como parámetro de línea de comandos.")
        print("0. Salir")

        opcion = input("\nSelecciona una opcion: ").strip()

        archivo = OPCIONES.get(opcion)

        if opcion == "0":
            print("\nSaliendo del programa...")
            break
        
        if opcion == "1":
            tarea_opcion_2_traduccion()

        if opcion == "2":
            tarea_opcion_3_ordenamiento()
            
        if opcion == "3":
            ruta = input("\nIngresa la ruta a listar: ").strip()
            orden = input("Ingresa el orden (asc/desc): ").strip().lower()

            if orden not in ("asc", "desc"):
                print("\nOrden no valido. Usa 'asc' o 'desc'.")
                input("\nPresiona Enter para intentarlo de nuevo...")
                continue
            
            ejecutar_archivo(archivo, [ruta, "--orden", orden])
        
if __name__ == "__main__":
         if len(sys.argv) > 1 and sys.argv[1] == "--desc":
            tarea_opcion_3_ordenamiento("desc")
         else:
             mostrar_menu()