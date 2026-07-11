import os
import sys
import subprocess
import glob
import time

def verificar_ffmpeg():
    """Verifica se o ffmpeg está disponível."""
    try:
        subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            check=True,
            encoding='utf-8',
            errors='ignore'
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def comprimir_video(entrada, saida, codec, crf, preset):
    """
    Comprime vídeo com H.265 (HEVC) usando preset lento para máxima compressão.
    """
    comando = [
        'ffmpeg',
        '-i', entrada,
        '-c:v', codec,
        '-crf', str(crf),
        '-preset', preset,
        '-c:a', 'aac',
        '-b:a', '128k',
        '-movflags', '+faststart',
        '-y',
        saida
    ]
    try:
        subprocess.run(
            comando,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao comprimir {entrada}:")
        if e.stderr:
            print(e.stderr.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore'))
        return False

# Início do programa
T_inicio_total = time.time()




# Pasta com os vídeos que deseja comprimir
pasta = r"C:\Users\Rafael Bruno\Downloads\VÍDEOS"





if not os.path.isdir(pasta):
    print(f"Pasta não encontrada: {pasta}")
    sys.exit(1)

if not verificar_ffmpeg():
    print("ffmpeg não encontrado. Instale-o e certifique-se de que está no PATH.")
    sys.exit(1)

# Extensões suportadas
extensoes = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg'}
arquivos = set()  # conjunto para evitar duplicatas

for ext in extensoes:
    for padrao in (f"*{ext}", f"*{ext.upper()}"):
        encontrados = glob.glob(os.path.join(pasta, padrao))
        arquivos.update(encontrados)

# Converte para lista
arquivos = list(arquivos)

if not arquivos:
    print("Nenhum arquivo de vídeo encontrado na pasta.")
    sys.exit(1)

print(f"Encontrados {len(arquivos)} arquivos de vídeo.")  # útil para depuração

# Cria pasta de saída
pasta_saida = os.path.join(pasta, "comprimidos")
os.makedirs(pasta_saida, exist_ok=True)



# Parâmetros de compressão
codec = 'libx265'
crf = 28
preset = 'medium'
print(f"Usando H.265 (HEVC) com preset '{preset}' e CRF={crf}.")



# Processa cada vídeo
for entrada in arquivos:
    nome_arq = os.path.basename(entrada)
    saida = os.path.join(pasta_saida, nome_arq)
    print(f"Comprimindo: {nome_arq} -> {saida}")
    
    tempo_inicio = time.time()
    sucesso = comprimir_video(entrada, saida, codec, crf, preset)
    if sucesso:
        print("  Concluído.")
    else:
        print("  Falhou.")
    
    tempo_final = time.time()
    duracao_seg = tempo_final - tempo_inicio
    duracao_min = duracao_seg / 60
    print(f"  Tempo de processamento: {duracao_seg:.2f} segundos ({duracao_min:.2f} minutos)")

print("\nTodos os processamentos foram finalizados.")
print(f"Arquivos comprimidos estão em: {pasta_saida}")

duracao_total = time.time() - T_inicio_total
print(f"Tempo total de execução: {duracao_total:.2f} segundos ({duracao_total/60:.2f} minutos)")