import threading
import time
import random
import pyautogui
import keyboard
from PIL import Image
from ultralytics import YOLO
import pydirectinput
import pygetwindow
import math
import win32gui
import win32con
import ctypes

last_metin_detection_time = 0

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def force_window_focus(window_title):
    try:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.1)  # Brief pause to ensure window is active
    except Exception as e:
        print(f"Error forcing window focus: {e}")

def run_bot(decision, player_position):
    global last_metin_detection_time

    if "metin_location" in decision:
        if time.time() - last_metin_detection_time > 3:
            closest_metin_distance = float('inf')
            closest_metin_location = None

            for metin_location in decision["metin_location"]:
                distance = calculate_distance(player_position, metin_location)
                if distance < closest_metin_distance:
                    closest_metin_distance = distance
                    closest_metin_location = metin_location

            if closest_metin_location:
                try:
                    force_window_focus('Velor2 | Power Of The Elements')  # Force focus on the window
                    print(f"Moving to Metin location: {closest_metin_location}")
                    pydirectinput.keyDown('shift')
                    duration = random.uniform(0.3, 0.7)
                    pydirectinput.moveTo(int(closest_metin_location[0]), int(closest_metin_location[1]), duration=duration)
                    pydirectinput.click(button='right')
                    pydirectinput.keyUp('shift')
                    print(f"Shift + Right Clicked on Metin at: {closest_metin_location}")
                    last_metin_detection_time = time.time()
                except Exception as e:
                    print(f"Error during bot action: {e}")
        else:
            print("Detected Metin within 10 seconds of the last one. Waiting before proceeding.")
            time.sleep(random.uniform(0.3, 2))

def spam_z_key(stop_event):
    while not stop_event.is_set():
        pydirectinput.press('z')
        time.sleep(random.uniform(0.05, 0.2))  # Adjust the zzzzspam speed here

def take_screenshot(stop_event, model):
    try:
        game_window = pygetwindow.getWindowsWithTitle('Velor2 | Power Of The Elements')[0]

        while not stop_event.is_set():
            decision = {"metin_location": []}

            screenshot = pyautogui.screenshot(
                region=(game_window.left, game_window.top, game_window.width, game_window.height))

            results = model([screenshot], conf=.80)
            boxes = results[0].boxes.xyxy.tolist()
            classes = results[0].boxes.cls.tolist()
            names = results[0].names
            confidences = results[0].boxes.conf.tolist()

            print(f"Detected boxes: {boxes}")
            print(f"Detected classes: {classes}")
            print(f"Detected confidences: {confidences}")

            for box, cls, conf in zip(boxes, classes, confidences):
                x1, y1, x2, y2 = box
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                name = names[int(cls)]

                print(f"Detected object: {name} at {center_x}, {center_y} with confidence {conf}")

                if name == "metin":
                    decision["metin_location"].append((center_x, center_y))

            run_bot(decision, (game_window.left + game_window.width / 2, game_window.top + game_window.height / 2))
    except Exception as e:
        print(f"Error in take_screenshot: {e}")

def main():
    model = YOLO('best.pt')
    stop_event = threading.Event()
    
    # Start the screenshot and bot logic in a separate thread
    screenshot_thread = threading.Thread(target=take_screenshot, args=(stop_event, model))
    screenshot_thread.start()
    
    # Start the "z" key spamming in another thread
    spam_thread = threading.Thread(target=spam_z_key, args=(stop_event,))
    spam_thread.start()
    
    # Wait for the "q" key to stop the bot
    keyboard.wait("q")
    stop_event.set()
    screenshot_thread.join()
    spam_thread.join()
    print("Program ended.")

if __name__ == "__main__":
    main()
