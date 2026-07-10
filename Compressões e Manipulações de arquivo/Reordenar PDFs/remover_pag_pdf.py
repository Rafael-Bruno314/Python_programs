from pypdf import PdfReader, PdfWriter

def remove_pdf_pages(input_pdf_path, output_pdf_path, pages_to_remove):
    """
    Remove páginas específicas de um arquivo PDF e salva o resultado em um novo arquivo.
    
    Parâmetros:
        input_pdf_path (str): Caminho do arquivo PDF original
        output_pdf_path (str): Caminho para salvar o PDF modificado
        pages_to_remove (list): Lista de números de páginas a serem removidas (índice 0)
    """
    # Abre o PDF original em modo leitura
    reader = PdfReader(input_pdf_path)
    
    # Cria um objeto PdfWriter para o novo PDF
    writer = PdfWriter()

    # Percorre todas as páginas do PDF original
    for page_num in range(len(reader.pages)):
        # Adiciona apenas as páginas que NÃO estão na lista de remoção
        if page_num not in pages_to_remove:
            writer.add_page(reader.pages[page_num])

    # Salva o novo PDF no arquivo de saída
    with open(output_pdf_path, 'wb') as output_pdf_file:
        writer.write(output_pdf_file)

if __name__ == "__main__":
    # Configurações dos arquivos (modifique conforme necessário)
    input_pdf_path = "/home/rana/Downloads/wealth-insight-Sep2024.pdf"         # Caminho do PDF original
    output_pdf_path = "/home/rana/Downloads/wealth-insight-Sep2024-refined.pdf" # Caminho do PDF resultante
    
    # Páginas a serem removidas (numeração humana, começando em 1)
    pages_to_remove = [2,3,6,9,15,19,21,23,33,64,75,76]
    
    # Converte para índice 0 (sistema Python)
    pages_to_remove = [x - 1 for x in pages_to_remove]
    
    try:
        remove_pdf_pages(input_pdf_path, output_pdf_path, pages_to_remove)
    except FileNotFoundError:
        print(f"Erro: Arquivo {input_pdf_path} não encontrado!")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
    
    # Mensagem de confirmação
    print(f"Páginas {[x+1 for x in pages_to_remove]} removidas de {input_pdf_path} e salvas em {output_pdf_path}")