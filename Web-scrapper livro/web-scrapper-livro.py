import os
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from urllib.parse import urljoin

# Função para baixar as imagens
"""def download_image(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        image_name = os.path.basename(url)
        image_path = os.path.join(folder_path, image_name)
        with open(image_path, 'wb') as file:
            file.write(response.content)"""

# Função para extrair e traduzir o texto
def extract_and_translate_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    translator = Translator()

    # Extrair texto
    text_content = ''
    for paragraph in soup.find_all('p'):
        text_content += paragraph.get_text() + '\n'

    # Traduzir texto
    translated_text = translator.translate(text_content, src='en', dest='pt').text

    return translated_text

# Função principal
def main():
    url = 'https://geo.libretexts.org/Bookshelves/Meteorology_and_Climate_Science/Book%3A_Fundamentals_of_Atmospheric_Science_(Brune)/01%3A_Getting_Started/1.01%3A_The_atmosphere_is_%E2%80%A6'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Criar pasta para armazenar imagens
    #images_folder = 'images'
    #os.makedirs(images_folder, exist_ok=True)

    # Extrair texto e imagens
    book_text = ''
    for section in soup.find_all('section'):
        section_text = extract_and_translate_text(urljoin(url, section.get('id')))
        book_text += section_text + '\n'

        for img in section.find_all('img'):
            pass
            #img_url = urljoin(url, img.get('src'))
            #download_image(img_url, images_folder)

    # Salvar texto traduzido em um arquivo
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(book_text)

    print("Texto e imagens extraídos e traduzidos com sucesso!")

if __name__ == "__main__":
    main()
