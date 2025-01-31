import pyautogui
import time

comments = []
for i in range(1, 101):
    # Convert integer to string before concatenating
    comments.append(str(i) + "Plz try this recipe dippo boss")

time.sleep(5)

for i in range(100):
    pyautogui.typewrite(comments[i % len(comments)])
    pyautogui.typewrite("\n")
    time.sleep(2)
