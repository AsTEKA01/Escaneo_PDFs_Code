import fitz  # PyMuPDF
from PIL import Image

pdf_path = "documentos/prueba_pdf.pdf"
doc = fitz.open(pdf_path)
page = doc[0]  # Tomar la primera página

pix = page.get_pixmap()
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
img.save("pagina1.png")
