import os
import shutil
from pathlib import Path

def mover_pdfs(origem: str, destino: str):
    """
    Move todos os arquivos PDF da pasta 'origem' e subpastas para a pasta 'destino'.
    """
    pasta_origem = Path(origem)
    pasta_destino = Path(destino)

    # Verifica se a pasta de origem existe
    if not pasta_origem.exists() or not pasta_origem.is_dir():
        print(f"ERRO: A pasta de origem '{origem}' não existe ou não é um diretório.")
        return

    # Cria a pasta de destino se não existir
    pasta_destino.mkdir(parents=True, exist_ok=True)

    # Percorre toda a árvore de diretórios a partir da origem
    for raiz, dirs, arquivos in os.walk(pasta_origem):
        for nome_arquivo in arquivos:
            # Verifica se é um arquivo PDF (case insensitive)
            if nome_arquivo.lower().endswith('.pdf'):
                caminho_completo = Path(raiz) / nome_arquivo
                destino_base = pasta_destino / nome_arquivo

                # Se o arquivo já existir no destino, gera um novo nome
                if destino_base.exists():
                    base, ext = os.path.splitext(nome_arquivo)
                    contador = 1
                    while True:
                        novo_nome = f"{base} ({contador}){ext}"
                        destino_novo = pasta_destino / novo_nome
                        if not destino_novo.exists():
                            destino_base = destino_novo
                            break
                        contador += 1

                # Move o arquivo
                try:
                    shutil.move(str(caminho_completo), str(destino_base))
                    print(f"Movido: {caminho_completo} -> {destino_base}")
                except Exception as e:
                    print(f"ERRO ao mover {caminho_completo}: {e}")

if __name__ == "__main__":
    # Defina os caminhos conforme sua necessidade
    ORIGEM = r"C:\Users\Rafa\Downloads\Itens exportados\files"
    DESTINO = r"C:\Users\Rafa\Downloads\Itens exportados\arquivos_extraídos"

    mover_pdfs(ORIGEM, DESTINO)
    print("Processo concluído.")
