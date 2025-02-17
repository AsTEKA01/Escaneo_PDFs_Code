# Escaneo_PDFs_Code

Este proyecto procesa un PDF escaneado, extrae el texto de cada página usando OCR y, mediante la detección de un código específico (por ejemplo, `2023XXXXXX`), separa el PDF en múltiples archivos. Cada archivo contiene las páginas agrupadas hasta que se detecta un nuevo código.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [Clonar el Repositorio](#clonar-el-repositorio)
  - [Crear un Entorno Virtual](#crear-un-entorno-virtual)
  - [Instalar las Dependencias](#instalar-las-dependencias)
  - [Instalar Tesseract OCR](#instalar-tesseract-ocr)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Cómo Funciona](#cómo-funciona)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

El script `script_pdf.py` convierte cada página de un PDF escaneado en imagen, extrae el texto completo usando Tesseract OCR, detecta códigos con el formato `2023XXXXXX` (aplicando un filtro para códigos mayores o iguales a `202300045`) y, en base a ello, separa el documento en varios PDFs. Cada PDF generado se guarda en la carpeta `documentos_separados` y lleva el nombre del código detectado.

## Características

- **Conversión de PDF a Imágenes:** Utiliza PyMuPDF para convertir cada página del PDF en imagen.
- **OCR Completo:** Emplea Tesseract OCR (a través de `pytesseract`) para extraer el texto de toda la página.
- **Detección de Código:** Busca un código con el formato `2023XXXXXX` usando expresiones regulares.
- **Separación de Documentos:** Agrupa las páginas en nuevos PDFs hasta que se detecta un nuevo código.

## Requisitos

- **Python 3.13** (o superior)
- **Tesseract OCR**
- Las siguientes librerías de Python:
  - [PyMuPDF](https://pymupdf.readthedocs.io/) (se importa como `fitz`)
  - [pytesseract](https://pypi.org/project/pytesseract/)
  - [Pillow](https://pillow.readthedocs.io/)

## Instalación

### Clonar el Repositorio

Clona el repositorio en tu máquina local:

bash

git clone https://github.com/AsTEKA01/Escaneo_PDFs_Code.git
cd Escaneo_PDFs_Code

Crear un Entorno Virtual
Se recomienda crear un entorno virtual para aislar las dependencias del proyecto.

En Windows:

python -m venv mi_entorno
mi_entorno\Scripts\activate

Instalar las Dependencias
Con el entorno virtual activado, instala las dependencias ejecutando:

pip install -r requirements.txt
Asegúrate de que el archivo requirements.txt contenga lo siguiente:

PyMuPDF
pytesseract
Pillow

En Windows
Descarga e instala Tesseract OCR desde Tesseract at UB Mannheim.
Durante la instalación, marca la opción para agregar Tesseract al PATH.
Si Tesseract no se agrega al PATH, edita el script script_pdf.py para establecer la ruta correcta, por ejemplo:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
