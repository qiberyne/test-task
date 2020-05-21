
import io
import pytesseract

output_file = 'C:/Users/qiber/Desktop/image_parsing_result.txt'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
test = pytesseract.image_to_string(r'C:/Users/qiber/Desktop/t.png', lang="rus+eng")

with io.open(output_file, 'w', encoding='utf-8') as file:
    file.write(test)