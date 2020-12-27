import pyautogui,time
width, height=pyautogui.size()
mouseX, mouseY=pyautogui.position()
pyautogui.hotkey('win', 'r')

pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("You are Hacked.\n")

pyautogui.write("Contact ADMIN\n")
