import pyautogui # implimindo o pyautogui no programa

for i in range(10):
    pyautogui.moveTo(100 +10 * i, 100 +10 * i, duration=0.5)
    pyautogui.moveTo(200 +10 * i, 100+ 10 *i, duration=0.5)
    pyautogui.moveTo(200 +10 * i, 20 + 10 *i, duration=0.5)
    pyautogui.moveTo(100 +10 * i, 100 +10 * i, duration=0.5)



