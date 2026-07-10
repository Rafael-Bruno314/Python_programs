import os
import sys
import subprocess
import glob
import time

# ============================================================
# CONFIGURAÇÕES (altere aqui)
# ============================================================

PASTA = r"C:\Users\Rafael Bruno\Downloads\VÍDEOS"   # Pasta com os vídeos
CODEC = 'libx265'      # 'libx265' (HEVC) ou 'libx264' (H.264)
CRF = 28               # Qualidade: 18-32 (28 é bom para H.265)
PRESET = 'medium'      # Velocidade: 'fast', 'medium', 'slow'.

# ============================================================


extensoes = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg'}

def verificar_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True,
                       encoding='utf-8', errors='ignore')
        return True
    except:
        return False

def comprimir_video(entrada, saida):
    comando = [
        'ffmpeg', '-i', entrada,
        '-c:v', CODEC,
        '-crf', str(CRF),
        '-preset', PRESET,
        '-c:a', 'aac',
        '-b:a', '128k',
        '-movflags', '+faststart',
        '-y', saida
    ]
    try:
        subprocess.run(comando, check=True, capture_output=True,
                       text=True, encoding='utf-8', errors='ignore')
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro em {entrada}:")
        if e.stderr:
            print(e.stderr.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore'))
        return False

def formatar_tamanho(tamanho_bytes):
    if tamanho_bytes >= 1024**3:
        return f"{tamanho_bytes/(1024**3):.2f} GB"
    elif tamanho_bytes >= 1024**2:
        return f"{tamanho_bytes/(1024**2):.2f} MB"
    elif tamanho_bytes >= 1024:
        return f"{tamanho_bytes/1024:.2f} KB"
    else:
        return f"{tamanho_bytes} bytes"

# Início
T_inicio = time.time()

if not os.path.isdir(PASTA):
    print(f"Pasta não encontrada: {PASTA}")
    sys.exit(1)

if not verificar_ffmpeg():
    print("ffmpeg não encontrado.")
    sys.exit(1)

# Cria pasta de saída "comprimidos"
pasta_saida = os.path.join(PASTA, "comprimidos")
os.makedirs(pasta_saida, exist_ok=True)

# Busca arquivos
arquivos = set()
for ext in extensoes:
    for padrao in (f"*{ext}", f"*{ext.upper()}"):
        arquivos.update(glob.glob(os.path.join(PASTA, padrao)))
arquivos = list(arquivos)

if not arquivos:
    print("Nenhum vídeo encontrado.")
    sys.exit(1)

print(f"Encontrados {len(arquivos)} vídeos.")
print(f"Codec: {CODEC} | CRF: {CRF} | Preset: {PRESET}")
print(f"Saída em: {pasta_saida}\n")

for entrada in arquivos:
    nome = os.path.basename(entrada)
    saida = os.path.join(pasta_saida, nome)   # mesmo nome, na pasta comprimidos

    tamanho_orig = os.path.getsize(entrada)
    print(f"Comprimindo: {nome}")
    print(f"  Tamanho original: {formatar_tamanho(tamanho_orig)}")

    inicio = time.time()
    sucesso = comprimir_video(entrada, saida)
    fim = time.time()

    if sucesso and os.path.exists(saida):
        tamanho_comp = os.path.getsize(saida)
        reducao = ((tamanho_orig - tamanho_comp) / tamanho_orig) * 100
        print(f"  Tamanho comprimido: {formatar_tamanho(tamanho_comp)}")
        print(f"  Redução de: {reducao:.1f}%")
        print("  Concluído.")
    else:
        print("  Falhou.")

    print(f"  Tempo: {fim-inicio:.1f}s ({((fim-inicio)/60):.1f}min)")
    print("-" * 50)

print("\nFinalizado.")
print(f"Tempo total: {time.time()-T_inicio:.1f}s ({((time.time()-T_inicio)/60):.1f}min)")