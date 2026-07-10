from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Caminho do chromedriver que você acabou de baixar
CAMINHO_DRIVER = r"D:\1234\Documents\Python_programs\Bot wpp\chromedriver.exe"

print("Iniciando...")
service = Service(executable_path=CAMINHO_DRIVER)
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
print("Título da página:", driver.title)
driver.quit()