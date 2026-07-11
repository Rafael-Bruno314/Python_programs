import subprocess
import math
import random
import os
import glob

# ========== CONFIGURAÇÃO ==========
video_principal = "Video_principal.mp4"   # Arquivo do vídeo principal
pasta_overlays = "overlay_videos"         # Pasta com os vídeos de overlay
video_saida = "video_final_pip.mp4"       # Arquivo de saída

posicao_x = "main_w-overlay_w-0"         # Margem direita de 10px
posicao_y = "0"                          # Margem superior de 10px
aceleracao = 3                          # Fator de aceleração (1.5 = 1,5x)
altura_relativa = 0.35                     # Proporção da altura do principal (0.5 = metade)
# ===================================

# --- Verifica a pasta de overlays ---
if not os.path.isdir(pasta_overlays):
    raise FileNotFoundError(f"A pasta '{pasta_overlays}' não foi encontrada.")

extensoes = ("*.mp4", "*.mov", "*.avi", "*.mkv", "*.webm")
overlay_videos = []
for ext in extensoes:
    overlay_videos.extend(glob.glob(os.path.join(pasta_overlays, ext)))
if not overlay_videos:
    raise RuntimeError(f"Nenhum vídeo encontrado na pasta '{pasta_overlays}'.")
print(f"Encontrados {len(overlay_videos)} vídeos de overlay.")

# --- 1. Informações do vídeo principal ---
# Usaremos ffprobe via linha de comando para evitar dependências pesadas
def get_video_info(path):
    cmd = [
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height,duration:format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', path
    ]
    try:
        out = subprocess.check_output(cmd, text=True).strip().split('\n')
        # A saída vem: width, height, stream duration, format duration
        width = int(out[0])
        height = int(out[1])
        dur = out[2] if out[2] != 'N/A' else out[3]
        duration = float(dur) if dur != 'N/A' else 0.0
        return width, height, duration
    except Exception as e:
        print(f"Erro ao obter info de {path}: {e}")
        raise

largura_principal, altura_principal, duracao_principal = get_video_info(video_principal)
print(f"Duração do principal: {duracao_principal:.2f}s")

altura_final = max(100, math.floor(altura_principal * altura_relativa))
if altura_final % 2: altura_final += 1
largura_final = math.floor(altura_final * 9/16)
if largura_final % 2: largura_final += 1
print(f"Tamanho do overlay redimensionado: {largura_final}x{altura_final}")

# --- 2. Analisar todos os vídeos overlay ---
overlays_info = []
for video_path in overlay_videos:
    try:
        w, h, dur = get_video_info(video_path)
        eff_duration = dur / aceleracao
        overlays_info.append({
            'path': video_path,
            'width': w,
            'height': h,
            'duration': dur,
            'eff_duration': eff_duration
        })
        print(f"  {os.path.basename(video_path)}: {w}x{h}, {dur:.2f}s -> acelerado {eff_duration:.2f}s")
    except Exception as e:
        print(f"Erro ao processar '{video_path}': {e}. Ignorando.")

if not overlays_info:
    raise RuntimeError("Nenhum vídeo overlay válido foi carregado.")

# --- 3. Criar sequência aleatória sem repetição até esgotar, depois reembaralhar ---
sequence = []               # índices dos overlays na ordem de exibição
tempo_acumulado = 0.0

indices = list(range(len(overlays_info)))
random.shuffle(indices)
ptr = 0

while tempo_acumulado < duracao_principal:
    idx = indices[ptr]
    sequence.append(idx)
    tempo_acumulado += overlays_info[idx]['eff_duration']
    nome = os.path.basename(overlays_info[idx]['path'])
    print(f"  Adicionado '{nome}' (acumulado: {tempo_acumulado:.2f}s)")
    ptr += 1
    if ptr >= len(indices):
        random.shuffle(indices)
        ptr = 0
        print("  >> Ciclo completo. Reembaralhando...")

N = len(sequence)
print(f"Total de segmentos concatenados: {N}")

# --- 4. Montar comando ffmpeg ---
cmd = ['ffmpeg']

# Entrada do vídeo principal (índice 0)
cmd.extend(['-i', video_principal])

# Entradas de overlay (uma para cada segmento, índices 1..N)
for idx in sequence:
    cmd.extend(['-i', overlays_info[idx]['path']])

# Construir filter_complex
filter_parts = []
overlay_labels = []

for i, idx in enumerate(sequence):
    entrada_idx = i + 1
    info = overlays_info[idx]
    w_orig = info['width']
    h_orig = info['height']

    # Crop para 9:16 centralizado
    if w_orig / h_orig > 9/16:
        new_w = math.floor(h_orig * 9/16)
        new_h = h_orig
        if new_w % 2: new_w += 1
        x_crop = (w_orig - new_w) // 2
        y_crop = 0
    else:
        new_h = math.floor(w_orig / 9*16)
        new_w = w_orig
        if new_h % 2: new_h += 1
        x_crop = 0
        y_crop = (h_orig - new_h) // 2

    label_out = f'ov{i}'
    overlay_labels.append(label_out)

    filter_parts.append(
        f"[{entrada_idx}:v]"
        f"crop={new_w}:{new_h}:{x_crop}:{y_crop},"
        f"setpts={1/aceleracao}*PTS,"
        f"scale={largura_final}:{altura_final}"
        f"[{label_out}]"
    )

# Concatenação
concat_inputs = ''.join(f'[{l}]' for l in overlay_labels)
filter_parts.append(f"{concat_inputs}concat=n={N}:v=1:a=0[ov_concat]")

# Overlay sobre o vídeo principal
filter_parts.append(
    f"[0:v][ov_concat]overlay={posicao_x}:{posicao_y}:shortest=1[outv]"
)

filter_complex = ';'.join(filter_parts)

cmd.extend(['-filter_complex', filter_complex])
cmd.extend(['-map', '[outv]'])
cmd.extend(['-map', '0:a?'])  # áudio do principal, se existir
cmd.extend(['-c:v', 'libx264', '-c:a', 'aac', '-preset', 'fast'])
cmd.extend(['-shortest', '-y', video_saida])

print("\nComando ffmpeg gerado:")
print(' '.join(cmd))

# --- 5. Executar ---
print(f"\nRenderizando '{video_saida}'...")
subprocess.run(cmd, check=True)
print("Concluído!")