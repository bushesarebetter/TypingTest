import pyautogui
import keyboard
import time
from screenshot import take_region_screenshot


# USE ONLY FOR TESTING

def coordinate_finder():
    print("Move your mouse to the desired position.")
    print("Press 'c' to capture the current coordinates.")
    print("Press 'q' to quit.")
    
    points = []
    
    while True:
        if keyboard.is_pressed('c'):
            x, y = pyautogui.position()
            points.append((x, y))
            print(f"Captured point: ({x}, {y})")
            print(f"Total points: {len(points)}")
            
            time.sleep(0.5)
            
        elif keyboard.is_pressed('q'):
            break
    
    if len(points) >= 2:
        x1, y1 = points[0]
        x2, y2 = points[1]
        print(f"\nRegion coordinates:")
        print(f"Top-left (x1, y1): ({x1}, {y1})")
        print(f"Bottom-right (x2, y2): ({x2}, {y2})")
        print("Saving image to test.png...")
        take_region_screenshot(x1, y1, x2, y2, "test")
        print("Saving coordinates to coords.txt...")
        with open('coordinates.txt', 'w') as f:
            for coord in points[0:2]:
                f.write(",".join(map(str, coord)) + "\n")
    
    return points



coordinate_finder()