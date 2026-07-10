"""
FUNCIONAMENTO:
- Abre o WhatsApp Web uma vez, você escaneia o QR Code.
- Após o login, fica enviando mensagens fofas automaticamente.
- Na primeira vez, escaneia o QR; nas próximas, a sessão é recuperada.
- Roda para sempre (loop infinito) até você fechar o terminal.

PRÉ-REQUISITOS:
1. Ter o Google Chrome instalado no computador.
2. Instalar as bibliotecas:
   pip install selenium webdriver-manager

CONFIGURAÇÃO:
- Altere as variáveis abaixo (número da noiva, intervalo, mensagens).
"""

import os
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ========================================
# 🎀 CONFIGURAÇÕES
# ========================================
MEU_NUMERO = "+5531987719298"          # Apenas informativo, não é usado no envio
NUMERO_NOIVA = "+5531996649776"        # Número da noiva com DDI (ex: +5511999998888)
INTERVALO_SEGUNDOS = 15              # 1 hora = 3600 segundos. Mude à vontade.

MENSAGENS = [
    "Meu amorzinho, te amo muito",
    "Seu noivo criou um bot apenas para dizer que te ama",
    "Pq só escrever pra vc não é suficiente",
    "Repito e repito infinitamente (enquanto o pc tiver energia) que eu te amo muito"
]

# Pasta do perfil persistente (não precisa escanear QR toda vez)
PASTA_PERFIL = os.path.join(os.getcwd(), "perfil_whatsapp_bot")
# ========================================


def criar_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={PASTA_PERFIL}")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    
    # Caminho manual (pode estar vazio se não quiser usar)
    caminho_manual = r"D:\1234\Documents\Python_programs\Bot wpp\chromedriver.exe"
    
    try:
        if os.path.exists(caminho_manual):
            service = Service(executable_path=caminho_manual)
        else:
            raise FileNotFoundError("Usando webdriver-manager")
    except Exception:
        print("🔧 Usando webdriver-manager para obter o ChromeDriver...")
        service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def fechar_popup_se_existir(driver):
    """Tenta fechar o pop‑up de notificações (se aparecer)."""
    try:
        # Espera até 5s para o botão "not now" / "cancelar" / "fechar"
        botoes = driver.find_elements(By.XPATH, "//button[contains(.,'Agora não') or contains(.,'Cancel')]")
        if botoes:
            botoes[0].click()
            print("🔔 Pop‑up fechado.")
            time.sleep(1)
    except Exception:
        pass  # não era crítico


def esperar_whatsapp_carregar(driver, timeout=60):
    """Abre o WhatsApp Web e aguarda o login (QR Code)."""
    print("🚀 Abrindo WhatsApp Web...")
    driver.get("https://web.whatsapp.com")
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan this QR code to link a device!']"))
        )
        # Se o QR Code ainda está presente, significa que não logou
        raise Exception("QR Code ainda visível – escaneie antes de continuar.")
    except Exception:
        # Se o QR sumiu ou o canvas desapareceu, a página principal carregou
        pass

    # Agora espera um elemento típico da tela principal (campo de busca ou lista de conversas)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='chat-list']"))
        )
        print("✅ WhatsApp carregado e logado!")
    except Exception:
        print("❌ Tempo esgotado. Verifique se você escaneou o QR Code.")
        driver.quit()
        exit()

    # Garante que pop‑ups de notificação sejam fechados
    time.sleep(3)  # pequena pausa para qualquer animação
    fechar_popup_se_existir(driver)


def enviar_mensagem_por_link(driver, numero, mensagem):
    """
    Abre diretamente a conversa via wa.me, digita e envia a mensagem.
    """
    try:
        # Monta URL sem o texto (vamos digitar manualmente para manter o loop simples)
        url = f"https://web.whatsapp.com/send?phone={numero}"
        driver.get(url)

        # Aguarda a caixa de mensagem ficar pronta (aparece após carregar a conversa)
        input_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            )
        )
        time.sleep(1)  # folga extra

        # Digita a mensagem e envia
        input_box.click()
        input_box.send_keys(mensagem)
        input_box.send_keys(Keys.ENTER)

        print(f"💌 Mensagem enviada: {mensagem}")
        return True

    except Exception as e:
        print(f"⚠️ Falha ao enviar: {e}")
        return False


def main():
    print("=" * 50)
    print("Enviador de mensagens periódicas")
    print("=" * 50)
    print(f"Enviando para: {NUMERO_NOIVA}")
    print(f"A cada: {INTERVALO_SEGUNDOS} segundos")
    print("Pressione Ctrl+C para parar.\n")

    driver = criar_driver()
    esperar_whatsapp_carregar(driver)

    try:
        indice = 0  # começa pela primeira mensagem da lista
        while True:
            
            """Comentar aqui para mensagens aleatórias"""
            # Pega a mensagem da posição atual e avança para a próxima
            msg = MENSAGENS[indice]
            indice = (indice + 1) % len(MENSAGENS)  # volta ao 0 quando chegar ao final
            
            """Comentar aqui para mensagens em sequencia
            msg = random.choice(MENSAGENS)
            """
            
            sucesso = enviar_mensagem_por_link(driver, NUMERO_NOIVA, msg)

            if not sucesso:
                print("⏳ Aguardando um pouco antes de tentar novamente...")
                time.sleep(10)

            print(f"💤 Próximo envio em {INTERVALO_SEGUNDOS} segundos...\n")
            time.sleep(INTERVALO_SEGUNDOS)

    except KeyboardInterrupt:
        print("\n Bot interrompido. Até logo!")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()