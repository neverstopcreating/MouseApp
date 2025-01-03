import pyautogui
import time


def scroll_page():
    while True:
        pyautogui.scroll(500)  # Scroll up
        time.sleep(5)
        pyautogui.scroll(-500)  # Scroll down
        time.sleep(5)

if __name__ == "__main__":
    scroll_page()
