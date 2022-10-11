from turtle import position
import pyautogui


while True:
    input("Press Enter to capture cursor position")
    pos = pyautogui.position()
    print(pos)
    pyautogui.click(pos)

# capture cursor position
