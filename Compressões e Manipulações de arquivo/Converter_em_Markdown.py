import os
from pathlib import Path
from markitdown import MarkItDown

# Pasta com os arquivos de entrada
pasta_entrada = r"C:\Users\Rafa\Documents\Programas Python\Converter em Markdown"

# Pasta onde salvar os .md (opcional, pode ser a mesma)
pasta_saida = r"C:\Users\Rafa\Documents\Programas Python\Converter em Markdown\Convertido"



# Criar a pasta de saída se não existir
Path(pasta_saida).mkdir(parents=True, exist_ok=True)

# Inicializar o conversor (com suporte a plugins, se quiser)
md = MarkItDown(enable_plugins=True)  # mude para True se instalar plugins

# Extensões suportadas (ajuste conforme necessário)
extensoes_suportadas = ('.pdf', '.pptx', '.docx', '.xlsx', '.xls', '.html', '.csv', '.json', '.xml', '.zip', '.epub', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.mp3', '.wav', '.mp4', '.txt')

# Percorre todos os arquivos e subpastas (recursivo)
for raiz, _, arquivos in os.walk(pasta_entrada):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        # Verifica extensão (case insensitive)
        if not caminho_completo.lower().endswith(extensoes_suportadas):
            continue
        
        try:
            print(f"Convertendo: {caminho_completo}")
            resultado = md.convert(caminho_completo)
            
            # Define nome do arquivo de saída: mesmo nome, com .md
            nome_base = Path(arquivo).stem
            # Mantém estrutura de subpastas na saída
            caminho_relativo = os.path.relpath(raiz, pasta_entrada)
            pasta_destino = os.path.join(pasta_saida, caminho_relativo)
            Path(pasta_destino).mkdir(parents=True, exist_ok=True)
            
            arquivo_saida = os.path.join(pasta_destino, f"{nome_base}.md")
            with open(arquivo_saida, "w", encoding="utf-8") as f:
                f.write(resultado.text_content)
            print(f"  -> Salvo em: {arquivo_saida}")
        except Exception as e:
            print(f"  Erro ao converter {caminho_completo}: {e}")

print("Conversão concluída!")
