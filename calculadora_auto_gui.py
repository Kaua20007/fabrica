import pyautogui

pyautogui.hotkey('win', 'r')
pyautogui.sleep(1)

pyautogui.write('calc', interval=0.10)
pyautogui.press('enter')
pyautogui.sleep(3)

pyautogui.write('20')
pyautogui.press('+')
pyautogui.write('20')
pyautogui.press('enter')
