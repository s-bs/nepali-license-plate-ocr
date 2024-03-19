import easyocr
from baseocr import BaseOCR

class EasyOCR(BaseOCR):
    def extract_text(self,image_path):
        reader = easyocr.Reader(['ne'])
        result = reader.readtext(image_path)
        for detect in result:
            print(detect[1])