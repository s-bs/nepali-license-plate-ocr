import easyocr
from PIL import Image
from PIL import Image
from PIL import ImageEnhance
import cv2
from baseocr import BaseOCR

class EasyOCR(BaseOCR):
    def resize_image(self,image_path):
        # Calculate the desired size
        original_width, original_height = image_path.size
        desired_width = original_width // 1
        desired_height = original_height // 1
        # Resize the image
        resized_image = image_path.resize((desired_width, desired_height))
        # Save the resized image
        resized_image.save("D:/Python/nepali-licence-plate/resources/output/resized_image.jpg")
    
    def image_contrast(self,image_path):
        # Increase the contrast
        enhancer = ImageEnhance.Contrast(image_path)
        increased_image = enhancer.enhance(-1.0)  # Increase contrast factor (adjust as needed)
        # Save the increased contrast image
        increased_image.save("D:/Python/nepali-licence-plate/resources/output/increased_contrast_image.jpg")
        
    def image_binary(self,image_path):
        gray = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 20)
        # Save the binary image
        cv2.imwrite("D:/Python/nepali-licence-plate/resources/output/binary_image.jpg", thresh)
             
        
    def extract_text(self,image_path):
        detected =[]
        reader = easyocr.Reader(['ne'])
        result = reader.readtext(image_path)
        for detect in result:
            # print(detect[1])
            detected.append(detect[1])
        return detected
    