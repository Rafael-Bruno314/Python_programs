import os

# Defina o caminho da pasta onde os arquivos estão localizados
caminho_pasta = 'D:\\1234\\Downloads\\EasyRooms\\megadrive'

# Extensão dos arquivos que você quer modificar (nesse caso, .gba)
extensao_alvo = '.bin'

# Lista todos os arquivos na pasta
arquivos = os.listdir(caminho_pasta)

# Percorre cada arquivo na pasta
for arquivo in arquivos:
    # Verifica se é um arquivo e se tem a extensão .gba
    caminho_arquivo_antigo = os.path.join(caminho_pasta, arquivo)
    if os.path.isfile(caminho_arquivo_antigo) and arquivo.endswith(extensao_alvo):
        # Remove os 4 primeiros caracteres do nome do arquivo
        novo_nome = arquivo[4:]
        caminho_arquivo_novo = os.path.join(caminho_pasta, novo_nome)

        # Renomeia o arquivo
        os.rename(caminho_arquivo_antigo, caminho_arquivo_novo)
        print(f'Renomeado: {arquivo} -> {novo_nome}')
