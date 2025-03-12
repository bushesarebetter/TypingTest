from cv2 import invert
import pyautogui
from imagereader import preprocess, extract, init, invert_colors
from screenshot import take_region_screenshot
import time
import keyboard

init() # Initialize pytesseract if needed


image_path = 'test.png'
image_path_stripped = 'test'

with open('coordinates.txt', 'r') as f:
    coords = [tuple(map(int, line.strip().split(','))) for line in f]

play = True
time.sleep(1) # give time to get to the screenshot site


while play:
    
    take_region_screenshot(*coords[0], *coords[1], image_path_stripped)

    preprocessed_image = preprocess(image_path)
    text = extract(preprocessed_image)
    text = text.replace('|', "I")
    text = text.replace('\n\n', ' ')
    text = text.replace('\n', ' ')
    text = text[:-1]
    print(f'text: {text}')
    

    pyautogui.typewrite(text) # after writing the text, take another screenshot and keep writing
    pyautogui.typewrite(' ')

    for _ in range(5):
        if keyboard.is_pressed('q'):
            play = False
        time.sleep(0.1) # give time for scrolling to finish
    if text.__contains__('wpm') and text.__contains__('Save your score to see how you compare'):
        play = False
