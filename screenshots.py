import os
import time
import threading
import pyautogui
import keyboard


def take_screenshot(interval, stop_event):
    
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    while not stop_event.is_set():
       
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshots/screenshot_{timestamp}.png")

        
        stop_event.wait(interval)


def main():
    
    interval = int(input("Enter the interval between screenshots (in seconds): "))
    
    
    stop_event = threading.Event()
    
    
    screenshot_thread = threading.Thread(target=take_screenshot, args=(interval, stop_event))
    screenshot_thread.start()

    print("Screenshot program started. Press 'q' to quit.")

    
    keyboard.wait("q")

    
    stop_event.set()

    
    screenshot_thread.join()

    print("Program ended.")

if __name__ == "__main__":
    main()