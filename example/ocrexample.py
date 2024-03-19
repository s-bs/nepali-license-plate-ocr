import sys
sys.path.append(r'D:\Python\nepali-licence-plate\services\ocr')
import ocr_easyocr
import cv2
# resize image
from PIL import Image



# if __name__ == '__main__':
#     image_path =cv2.imread('D:/Python/nepali-licence-plate/resources/images/dataset/5.png')
#     object_ocr = ocr_easyocr.EasyOCR()
#     result = object_ocr.extract_text(image_path)
    
# if __name__ == '__main__':
#     # Open the image
#     image_path = Image.open("D:/Python/nepali-licence-plate/resources/images/dataset/2.jpg")
#     object_ocr = ocr_easyocr.EasyOCR()
#     result = object_ocr.resize_image(image_path)


# if __name__ == '__main__':
#     # Open the image
#     image_path = Image.open("D:/Python/nepali-licence-plate/resources/images/dataset/2.jpg")
#     object_ocr = ocr_easyocr.EasyOCR()
#     result = object_ocr.image_contrast(image_path)
    
# if __name__ == '__main__':
#     # Open the image
#     image_path =cv2.imread('D:/Python/nepali-licence-plate/resources/images/dataset/5.png')
#     object_ocr = ocr_easyocr.EasyOCR()
#     result = object_ocr.image_binary(image_path)

if __name__ == '__main__':
    # Open the image
    object_ocr = ocr_easyocr.EasyOCR()
    
    original_image_path = Image.open("D:/Python/nepali-licence-plate/resources/images/dataset/1.jpg")    
    resize = object_ocr.resize_image(original_image_path)
    
    resize_image_path = Image.open("D:/Python/nepali-licence-plate/resources/output/resized_image.jpg")
    contrast = object_ocr.image_contrast(resize_image_path)
    
    contrast_image_path =cv2.imread('D:/Python/nepali-licence-plate/resources/output/increased_contrast_image.jpg')
    binary_image = object_ocr.image_binary(contrast_image_path)
    
    image_path =cv2.imread('D:/Python/nepali-licence-plate/resources/output/binary_image.jpg')
    result = object_ocr.extract_text(image_path)
    