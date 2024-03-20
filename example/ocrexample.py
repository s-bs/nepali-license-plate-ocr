import sys
sys.path.append(r'D:\Python\nepali-licence-plate\services\ocr')
import ocr_easyocr
import cv2
# resize image
from PIL import Image
import pandas as pd
import os


if __name__ == '__main__':
    # Open the image
    object_ocr = ocr_easyocr.EasyOCR()

    # Create an empty DataFrame to store the OCR results
    results_df = pd.DataFrame(columns=["Image", "OCR Result"])

    # dir path
    directory = "D:/Python/nepali-licence-plate/resources/images/dataset"


    for filename in os.listdir(directory):
      if filename.endswith(".jpg"):
        # image path
        image_path = os.path.join(directory, filename)

        # original_image = Image.open(image_path)
        # original_image_path = Image.open(image_path)
        
        image_normal = object_ocr.normalize_image(image_path)

        normalize_image_path = Image.open("D:/Python/nepali-licence-plate/resources/output/normalized_image.jpg")
        resize = object_ocr.resize_image(normalize_image_path)

        resize_image_path = Image.open("D:/Python/nepali-licence-plate/resources/output/resized_image.jpg")
        contrast = object_ocr.image_contrast(resize_image_path)

        contrast_image_path =cv2.imread('D:/Python/nepali-licence-plate/resources/output/increased_contrast_image.jpg')
        binary_image = object_ocr.image_binary(contrast_image_path)

        image_path =cv2.imread('D:/Python/nepali-licence-plate/resources/output/binary_image.jpg')
        result = object_ocr.extract_text(image_path)


        # append image and ocr result
        results_df = results_df.append({"Image": filename, "OCR Result": result}, ignore_index=True)
    # Save the DataFrame to an Excel file
    results_df.to_excel("ocr_results.xlsx", index=False)