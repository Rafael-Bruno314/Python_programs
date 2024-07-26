import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1

# Abrindo o navegador
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
# pyautogui.alert("Alguma coisa")
pyautogui.hotkey('ctrl', 't')

# Abrindo o drive
link = "https://drive.google.com/drive/folders/1JLa3vHvF_U4J4wTVkjKy0wn6NrrHAkPK"
pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")
time.sleep(10)

"baixar a base de dados atualizada - mais ou menos isso"
# print(pyautogui.position())
pyautogui.click(1350, 378, clicks=3)
time.sleep(10)
pyautogui.click(1030, 300, clicks=3)
time.sleep(10)
pyautogui.rightClick(1200, 350)
time.sleep(5)
pyautogui.press("down", presses=6)
pyautogui.press("enter")
