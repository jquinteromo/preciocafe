import requests
import io
from PyPDF2 import PdfReader
import re

def obtener_precio_cafe():
    url = "https://www.federaciondecafeteros.org/static/files/precio_cafe.pdf"
    try:
        response = requests.get(url)
        pdf_file = io.BytesIO(response.content)
        reader = PdfReader(pdf_file)

        text = ""
        for page in reader.pages:
            text += page.extract_text()

        print("=== TEXTO EXTRAÍDO ===")
        print(text)
        print("=== FIN DEL TEXTO ===")

        match = re.search(r'\b[2-3],\d{3},\d{3}\b', text)
        if match:
            return match.group(0)
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None
