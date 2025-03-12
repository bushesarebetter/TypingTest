import pytesseract
import cv2
from PIL import Image
import numpy as np
import platform

def init():
    if platform.system() == "Windows":
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # Edit to your own tesseract path

def preprocess(image, output_path=None):
    try:
        img = cv2.imread(image)
        
        # Check if image was loaded properly
        if img is None:
            print(f"ERROR: Could not load image {image}")
            return image
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
        
        if output_path:
            cv2.imwrite(output_path, opening)
            return output_path
            
        # Save to temporary file since PIL needs a file path
        temp_path = "temp_processed.png"
        cv2.imwrite(temp_path, opening)
        return temp_path
    except Exception as e:
        print(f"ERROR in preprocessing: {e}")
        return image

def extract(image):
    try:
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"ERROR in extraction: {e}")
        return ""
from PIL import Image, ImageOps

def invert_colors(image_path):
    try:
        image = Image.open(image_path)
        inverted_image = ImageOps.invert(image)
        temp_path = "temp_processed.png"
        cv2.imwrite(temp_path, inverted_image)
        return temp_path
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
