import io
import pytesseract

input_file = r'filepath'
output_file = 'filepath'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(input_file, lang="rus+eng")

with io.open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)