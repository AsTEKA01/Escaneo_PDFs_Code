# Escaneo_PDFs_Code

Este proyecto permite procesar documentos PDF escaneados, extrayendo texto con OCR y separando cada documento en archivos individuales según un código detectado en una zona específica de la página.

## 📌 Características
- **Conversión de PDF a imágenes** utilizando PyMuPDF.
- **Extracción de texto** con Tesseract OCR.
- **Detección de códigos** en una zona específica de la página.
- **Agrupación de páginas** en un solo archivo PDF hasta que se detecte un nuevo código.
- **Generación automática de PDFs** con nombres basados en los códigos detectados.

---

## 🛠 Instalación

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/AsTEKA01/Escaneo_PDFs_Code.git
cd Escaneo_PDFs_Code
```

### 2️⃣ Crear un entorno virtual

Se recomienda usar un entorno virtual para aislar las dependencias:

**En Windows:**
```bash
python -m venv mi_entorno
mi_entorno\Scripts\activate
```

**En Linux/macOS:**
```bash
python3 -m venv mi_entorno
source mi_entorno/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

Asegúrate de que el archivo `requirements.txt` contenga:
```txt
PyMuPDF
pytesseract
Pillow
```

### 4️⃣ Instalar Tesseract OCR

#### En Windows
1. Descarga [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) e instálalo.
2. Si no se agrega al PATH automáticamente, edita `script_pdf.py` y añade la ruta:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

#### En Linux
```bash
sudo apt update && sudo apt install tesseract-ocr
```

#### En macOS
```bash
brew install tesseract
```

---

## 🚀 Uso del script

1️⃣ Coloca el PDF a procesar en la carpeta `documentos/`.

2️⃣ Ejecuta el script:
```bash
python script_pdf.py
```

3️⃣ Los PDFs separados se guardarán en `documentos_separados/` con nombres basados en los códigos detectados.

---

## 📂 Estructura del Proyecto
```
Escaneo_PDFs_Code/
├── documentos/
│   └── documento_escaneado.pdf  # PDF original
├── documentos_separados/         # Carpeta de PDFs generados
├── script_pdf.py                 # Script principal
├── requirements.txt              # Dependencias
└── README.md                     # Documentación
```

---

## 🔍 Cómo funciona

1️⃣ **Conversión de PDF a imágenes:** Se usa PyMuPDF para transformar cada página en una imagen.
```python
pix = page.get_pixmap()
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
```

2️⃣ **Extracción de texto con OCR:** Se usa Tesseract OCR para extraer el texto de la imagen.
```python
text = pytesseract.image_to_string(img, config="--psm 6").strip()
```

3️⃣ **Detección de códigos:** Se busca un código con formato `2023XXXXXX` y se agrupan páginas hasta que aparezca un nuevo código.
```python
match = re.search(r"2023\d{6}", text)
if match:
    current_code = match.group()
```

4️⃣ **Generación de PDFs:** Se guardan las páginas acumuladas como un nuevo archivo PDF cuando se detecta un cambio de código.
```python
pdf_writer.add_page(page)
pdf_writer.save(f"documentos_separados/{current_code}.pdf")
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para colaborar:
1. Realiza un fork del repositorio.
2. Crea una nueva rama con tu mejora.
3. Envía un Pull Request con una descripción detallada de los cambios.

---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
