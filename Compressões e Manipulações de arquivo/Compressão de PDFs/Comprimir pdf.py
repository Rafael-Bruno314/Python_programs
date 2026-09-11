#!/usr/bin/env python
# coding: utf-8

# pip install apryse-sdk --extra-index-url=https://pypi.apryse.com

# In[1]:


# Import Libraries
import os
import sys
import tempfile
from apryse_sdk import PDFDoc, Optimizer, SDFDoc, PDFNet

#from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet


# In[2]:


def get_size_format(b, factor=1024, suffix="B"):
    """
    Converte um tamanho em bytes para um formato legível (KB, MB, GB, etc.).

    Parâmetros:
        b (int): Tamanho em bytes.
        factor (int, opcional): Fator de conversão (padrão: 1024 para binário).
        suffix (str, opcional): Sufixo da unidade (padrão: "B" para Bytes).

    Retorna:
        str: String formatada com o tamanho ajustado (ex: "1.20MB").

    Exemplo:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


# In[3]:


def compress_file(input_file: str, output_file: str):
    """
    Comprime um arquivo PDF usando a biblioteca PDFNet, reduzindo seu tamanho.

    IMPORTANTE: PDFNet.Initialize() deve ter sido chamado antes desta função.

    Parâmetros:
        input_file (str): Caminho do arquivo PDF de entrada.
        output_file (str): Caminho do arquivo PDF de saída (se vazio, sobrescreve o original).

    Retorna:
        bool: True se a compressão foi bem-sucedida, False caso contrário.
    """
    if not output_file:
        output_file = input_file

    initial_size = os.path.getsize(input_file)  # Tamanho original do arquivo

    doc = None  # <-- define antes do try para evitar NameError no except
    try:
        doc = PDFDoc(input_file)  # Carrega o PDF

        # Configura o manipulador de segurança padrão (necessário para edição)
        doc.InitSecurityHandler()

        # Otimiza o PDF: remove metadados redundantes e compacta fluxos de dados
        Optimizer.Optimize(doc)

        # Salva o arquivo compactado (e_linearized para web)
        doc.Save(output_file, SDFDoc.e_linearized)
        doc.Close()  # Fecha o documento

    except Exception as e:
        print("Error compress_file=", e)
        # Só tenta fechar se o documento chegou a ser aberto
        if doc is not None:
            try:
                doc.Close()
            except Exception:
                pass
        return False

    # Calcula estatísticas pós-compressão
    compressed_size = os.path.getsize(output_file)
    ratio = 1 - (compressed_size / initial_size)  # Taxa de compressão (0-1)

    # Resumo da operação
    summary = {
        "Input File": input_file,
        "Initial Size": get_size_format(initial_size),
        "Output File": output_file,
        "Compressed Size": get_size_format(compressed_size),
        "Compression Ratio": "{0:.3%}.".format(ratio)  # Formata como porcentagem
    }

    # Exibe o resumo formatado
    print("--------------------- Resumo da compressão ------------------------")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("-------------------------------------------------------------------")
    print("")
    return True


# In[4] — NOVAS FUNÇÕES ----------------------------------------------------------


def get_folder_size(folder_path: str) -> int:
    """
    Calcula o tamanho total (em bytes) de todos os arquivos de uma pasta,
    incluindo subpastas.

    Parâmetros:
        folder_path (str): Caminho da pasta.

    Retorna:
        int: Tamanho total em bytes.
    """
    total = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                total += os.path.getsize(full_path)
            except OSError:
                # Ignora arquivos inacessíveis / links quebrados
                pass
    return total


def compress_file_safe(input_file: str):
    """
    Comprime o PDF para um arquivo temporário e mantém apenas a versão de
    menor tamanho (comprimida ou original).

    Regra:
        - Se o comprimido for menor que o original -> substitui o original.
        - Se o comprimido for maior ou igual -> descarta o comprimido e
          mantém o original intacto.

    Parâmetros:
        input_file (str): Caminho do PDF a ser processado (in-place se vencer).

    Retorna:
        tuple: (tamanho_inicial_bytes, tamanho_final_bytes)
    """
    initial_size = os.path.getsize(input_file)

    # Cria o temporário no mesmo diretório (garante os.replace sem copiar entre FS)
    temp_fd, temp_path = tempfile.mkstemp(
        suffix=".pdf", dir=os.path.dirname(input_file) or "."
    )
    os.close(temp_fd)

    try:
        success = compress_file(input_file, temp_path)
    except Exception as e:
        print(f"Falha ao comprimir '{input_file}': {e}\n\n")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return initial_size, initial_size

    if not success or not os.path.exists(temp_path):
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"[Info] Compressão falhou em '{input_file}'. Mantendo original.\n\n")
        return initial_size, initial_size

    compressed_size = os.path.getsize(temp_path)

    if compressed_size < initial_size:
        # O comprimido é de fato menor -> substitui o original
        os.replace(temp_path, input_file)
        return initial_size, compressed_size
    else:
        # O comprimido não é menor -> descarta e mantém o original
        os.remove(temp_path)
        print(f"[Info] Compressão NÃO reduziu '{os.path.basename(input_file)}' "
            f"({get_size_format(initial_size)} -> {get_size_format(compressed_size)}). "
            f"Mantendo original.\n\n"
        )
        return initial_size, initial_size


# In[5] — EXECUÇÃO PRINCIPAL -----------------------------------------------------


# Pasta contendo os PDFs a serem comprimidos (substitua pelo seu caminho)
input_folder = r"G:\Meu Drive\Zotero_Files"


# --- Inicialização única do PDFNet (fora do loop) -----------------------------
PDFNet.Initialize(
    "demo:1652721067096:7b89dd1603000000008ca8f036d3c1112cd0debd5cca3f78321ecf6f88"
)

# --- Medição inicial ----------------------------------------------------------
initial_folder_size = get_folder_size(input_folder)

print("=" * 70)
print(f"Tamanho INICIAL da pasta: {get_size_format(initial_folder_size)} "
      f"({initial_folder_size} bytes)")
print("=" * 70)
print("")

# --- Processamento ------------------------------------------------------------
total_initial = 0
total_final = 0
processed = 0

try:
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)      # Caminho completo do PDF
                ini, fin = compress_file_safe(pdf_path)  # Sempre fica com a versão menor
                total_initial += ini
                total_final += fin
                processed += 1
finally:
    # Libera recursos da biblioteca, mesmo se algo falhar no meio
    try:
        PDFNet.Terminate()
    except Exception:
        pass

# --- Medição final ------------------------------------------------------------
final_folder_size = get_folder_size(input_folder)

# --- Resumo geral -------------------------------------------------------------
print("")
print("=" * 70)
print("RESUMO GERAL")
print("=" * 70)
print(f"PDFs processados:        {processed}")
print(f"Tamanho inicial da pasta: {get_size_format(initial_folder_size)}")
print(f"Tamanho final da pasta:   {get_size_format(final_folder_size)}")

if initial_folder_size > 0:
    reducao = 1 - (final_folder_size / initial_folder_size)
    economia = initial_folder_size - final_folder_size
    print(f"Redução total:            {reducao:.3%}")
    print(f"Espaço economizado:       {get_size_format(economia)}")
else:
    print("Redução total:            N/A (pasta vazia)")

print("=" * 70)
print("Otimização concluída!")
