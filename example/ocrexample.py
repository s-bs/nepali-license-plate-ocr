import sys
sys.path.append(r'D:\Python\nepali-licence-plate\services\ocr')
import ocr_easyocr
import cv2

if __name__ == '__main__':
    image_path =cv2.imread('D:/Python/nepali-licence-plate/resources/images/dataset/5.png')
    object_ocr = ocr_easyocr.EasyOCR()
    result = object_ocr.extract_text(image_path)