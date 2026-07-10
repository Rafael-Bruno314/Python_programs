import os
from pypdf import PdfWriter

# Cria um objeto PdfWriter para mesclar os PDFs
merger = PdfWriter()

# Percorre todos os diretórios e subdiretórios a partir do diretório atual
for raiz, diretorios, arquivos in os.walk("."):
    for arquivo in arquivos:
        # Verifica se o arquivo tem extensão .pdf (case insensitive)
        if arquivo.lower().endswith('.pdf'):
            try:
                # Obtém o caminho completo do arquivo
                caminho_completo_origem = os.path.join(raiz, arquivo)
                print(f"Processando arquivo: {caminho_completo_origem}")
                
                # Adiciona o PDF ao merger
                merger.append(fileobj=caminho_completo_origem)
                
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")
                continue  # Continua para o próximo arquivo mesmo em caso de erro

# Gera o arquivo de saída com todos os PDFs mesclados
output_path = "pdf_mesclado_output.pdf"
try:
    merger.write(output_path)
    print(f"Arquivo mesclado gerado com sucesso: {output_path}")
except Exception as e:
    print(f"Erro ao gerar arquivo de saída: {e}")
finally:
    # Garante que o merger seja fechado mesmo em caso de erro
    merger.close()