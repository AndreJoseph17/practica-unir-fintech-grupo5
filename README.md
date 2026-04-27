# practica-unir-fintech-grupo5

Proyecto de práctica grupal para la asignatura **Entornos de Integración y Entrega Continua** – UNIR.

Aplicación Python con menú interactivo de opciones, desarrollada como caso práctico de **FinTech Solutions S.A.**

---

## Tabla de contenidos

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Funcionalidades implementadas](#funcionalidades-implementadas)
- [Flujo de trabajo GitHub](#flujo-de-trabajo-github)
- [Integrantes del grupo](#integrantes-del-grupo)

---

## Descripción

Este proyecto forma parte de la práctica grupal de la asignatura **Entornos de Integración y Entrega Continua** de UNIR.

Simula el entorno de desarrollo de **FinTech Solutions S.A.**, una empresa enfocada en el desarrollo de software personalizado para instituciones financieras. El objetivo principal de la práctica es aplicar el **GitHub Flow** trabajando en paralelo sobre el mismo repositorio mediante forks y pull requests.

La aplicación consiste en un menú interactivo en Python que permite al usuario seleccionar entre distintas opciones funcionales. Cada opción ejecuta un script independiente.

---

## Requisitos

- Python 3.x
- Git

---

## Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/AndreJoseph17/practica-unir-fintech-grupo5.git
cd practica-unir-fintech-grupo5
```

### 2. Verifica que tienes Python instalado

```bash
python --version
```

No se requieren dependencias externas. La aplicación usa únicamente módulos estándar de Python (`os`, `subprocess`, `sys`).

---

## Uso

Ejecuta el script principal desde la raíz del proyecto:

```bash
python main.py
```

### Menú principal

Al arrancar la aplicación, verás el siguiente menú interactivo:

```
MENU PRINCIPAL
1. Opcion 1
2. Opcion 2
3. Opcion 3
4. Opcion 4
5. Opcion 5
6. Opcion 6
0. Salir

Selecciona una opcion:
```

- Escribe el número de la opción deseada y pulsa **Enter**.
- Si el archivo correspondiente existe, se ejecutará automáticamente.
- Al finalizar, pulsa **Enter** para volver al menú principal.
- Para salir del programa, selecciona la opción **0**.

### Ejemplo de ejecución — Opción 1

```
Selecciona una opcion: 1

[Salida del script opcion1.py]

Presiona Enter para volver al menu...
```

### Ejemplo de ejecución — Opción no válida

```
Selecciona una opcion: 9

Opcion no valida.

Presiona Enter para intentarlo de nuevo...
```

### Ejemplo de ejecución — Archivo no encontrado

```
Selecciona una opcion: 3

No se encontro el archivo: opcion3.py

Presiona Enter para volver al menu...
```

### Ejemplo de ejecución — Salir

```
Selecciona una opcion: 0

Saliendo del programa...
```

---

## Estructura del proyecto

```
practica-unir-fintech-grupo5/
├── main.py        # Menú principal e inicializador
└── README.md      # Documentación del proyecto
```

---

## Funcionalidades implementadas

Cada integrante del grupo implementó una funcionalidad distinta mediante su propia rama y pull request:

| Opción | Funcionalidad | Desarrollador | Rama |
|--------|--------------|---------------|------|
| 1 | Andre Joseph | carga inicial | `origin/main` |
| 2 | Kevin Peña | README | ` feature/actualizar-readme` |
| 3 | *(descripción)* | *(nombre)* | `feature/opcion3` |
| 4 | *(descripción)* | *(nombre)* | `feature/opcion4` |
| 5 | *(descripción)* | *(nombre)* | `feature/opcion5` |
| 6 | *(descripción)* | *(nombre)* | `feature/opcion6` |

---

## Flujo de trabajo GitHub

Este proyecto sigue el **GitHub Flow**. A continuación se describen los pasos que siguió cada integrante:

### Administrador del repositorio

1. Creó el repositorio principal en GitHub (público).
2. Clonó el repositorio en local e inicializó el código base.
3. Realizó el primer commit y push a `main`.
4. Compartió la URL del repositorio con el resto del grupo **sin dar acceso de escritura**.
5. Implementó una funcionalidad en una rama separada y abrió su propia pull request.
6. Revisó y fusionó las pull requests del resto del equipo.

### Desarrolladores

1. Hicieron un **fork** del repositorio del administrador.
2. Clonaron su fork en local:

```bash
git clone https://github.com/<tu-usuario>/practica-unir-fintech-grupo5.git
cd practica-unir-fintech-grupo5
```

3. Crearon una rama nueva para su funcionalidad:

```bash
git checkout -b feature/opcionX
```

4. Implementaron los cambios y realizaron el commit:

```bash
git add .
git commit -m "Agrega funcionalidad opcionX"
```

5. Subieron la rama a su fork:

```bash
git push origin feature/opcionX
```

6. Abrieron una **pull request** desde su fork hacia el repositorio principal del administrador.

---

## Integrantes del grupo

| Nombre completo | GitHub | Rol |
|-----------------|--------|-----|
| Andre Joseph | [@AndreJoseph17](https://github.com/AndreJoseph17) | Administrador |
| Kevin Peña | [@kevin-pena-unir](https://github.com/kevin-pena-unir)| Desarrollador |
| *(Nombre Apellido)* | *(usuario)* | Desarrollador |
| *(Nombre Apellido)* | *(usuario)* | Desarrollador |
| *(Nombre Apellido)* | *(usuario)* | Desarrollador |

---

## Licencia

Proyecto académico – UNIR, 2025. Solo para uso educativo.
