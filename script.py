import os
import re
import fitz           # PyMuPDF para manipular PDFs
import pytesseract    # Para OCR
from PIL import Image # Para manipulación de imágenes

# Configurar la ruta de Tesseract si no está en el PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Ruta del PDF escaneado (ajusta la ruta según tu carpeta)
pdf_path = "documentos/prueba_pdf.pdf"

# Carpeta donde se guardarán los PDFs separados
output_folder = "documentos_separados"
os.makedirs(output_folder, exist_ok=True)

# Expresión regular para buscar códigos: "2023" seguido de 6 dígitos
code_pattern = re.compile(r"\b(2023\d{6})\b")

def extract_code_from_page(page):
    """
    Extrae el código analizando la página completa con OCR.
    Devuelve el código si se encuentra y es mayor o igual a 202300045.
    """
    # Convertir la página a imagen
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Extraer el texto de la imagen completa
    text = pytesseract.image_to_string(img, config="--psm 6").strip()
    
    # Mensaje de depuración para ver el texto extraído
    print("Texto extraído de la página:", text)
    
    # Buscar el código usando la expresión regular
    match = code_pattern.search(text)
    if match:
        code = match.group(1)
        # Retornar el código solo si es mayor o igual a 202300045
        if int(code) >= 2023000045:
            return code
    return None

# Abrir el PDF original
doc = fitz.open(pdf_path)

current_pdf = None  # Documento PDF en construcción
last_code = None    # Último código válido detectado

# Recorrer cada página del PDF
for i in range(len(doc)):
    page = doc[i]
    
    # Extraer el código de la página completa
    code = extract_code_from_page(page)
    
    # Mensaje de depuración para ver el código detectado en cada página
    print(f"Página {i+1}: Código detectado: {code}")
    
    # Si no se detecta un código, se usa el último código válido
    if code is None:
        code = last_code

    # Si se detecta un código nuevo (diferente al anterior), guardar el PDF en curso
    if code is not None and code != last_code:
        if current_pdf is not None:
            output_path = os.path.join(output_folder, f"{last_code}.pdf")
            current_pdf.save(output_path)
            current_pdf.close()
            print(f"Documento guardado: {output_path}")
        # Iniciar un nuevo documento PDF para el nuevo código
        current_pdf = fitz.open()

    # Si ya hay un documento en construcción, agregar la página actual
    if current_pdf is not None:
        current_pdf.insert_pdf(doc, from_page=i, to_page=i)
    
    # Actualizar el último código detectado
    last_code = code

# Guardar el último documento procesado
if current_pdf is not None:
    output_path = os.path.join(output_folder, f"{last_code}.pdf")
    current_pdf.save(output_path)
    current_pdf.close()
    print(f"Documento guardado: {output_path}")

print("Proceso completado.")
