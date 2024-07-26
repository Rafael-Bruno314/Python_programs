import pyperclip
from pyautogui import *

PAUSE = 2
FAILSAFE = True

# Abrindo o navegador
press("winleft")
write("chrome")
press("enter")


# time.sleep(4)
# hotkey('ctrl', 't')

def cambio(link):
    print(link)
    sleep(3)
    write(f"{link}")
    press("enter")
    hotkey("winleft", "right")

    time.sleep(3)
    print(position())

    # time.sleep(2)
    click(812, 499)
    hotkey('ctrl', 'c')

    spam = pyperclip.paste()
    print(spam)


cambio("https://www.melhorcambio.com/dolar-hoje")
