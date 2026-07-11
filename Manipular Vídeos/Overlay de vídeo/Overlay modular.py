import subprocess
import math
import random
import os
import glob
import sys

# ========== CONFIGURAÇÃO ==========
pasta_overlays = "overlay_videos"         # Pasta com os vídeos de overlay
pasta_saida = "video_pronto"              # Pasta de saída para o vídeo final

aceleracao = 3.0                          # Fator de aceleração (1.5 = 1,5x)
altura_relativa = 0.25                    # Proporção da altura do principal (0.5 = metade)

# Lista de posições dos overlays (expressões ffmpeg).
# Cada entrada gera um overlay independente.
posicoes = [
    "0:0",                                          # overlay 1: canto superior esquerdo
    "main_w-overlay_w-0:main_h-overlay_h-0",        # overlay 2: canto inferior direito
    "main_w-overlay_w-0:0",                         # overlay 3: canto superior direito
    "0:main_h-overlay_h-0"                          # overlay 4: canto inferior esquerdo
]
# ===================================

script_dir = os.path.dirname(os.path.abspath(__file__))

# --- 0. Criar pasta de saída se não existir ---
os.makedirs(pasta_saida, exist_ok=True)

# --- 1. Detectar automaticamente o vídeo principal ---
extensoes = ("*.mp4", "*.mov", "*.avi", "*.mkv", "*.webm")
videos_no_diretorio = []
for ext in extensoes:
    for caminho in glob.glob(os.path.join(script_dir, ext)):
        if not os.path.relpath(caminho, script_dir).startswith(pasta_overlays + os.sep):
            videos_no_diretorio.append(caminho)

if len(videos_no_diretorio) == 0:
    raise RuntimeError("Nenhum vídeo principal encontrado no diretório do script.")
elif len(videos_no_diretorio) > 1:
    raise RuntimeError("Mais de um vídeo principal encontrado. Deixe apenas um arquivo de vídeo junto ao script.")
video_principal = videos_no_diretorio[0]
print(f"Vídeo principal detectado: {os.path.basename(video_principal)}")

# --- 2. Verificar/coletar overlays ---
if not os.path.isdir(pasta_overlays):
    raise FileNotFoundError(f"A pasta '{pasta_overlays}' não foi encontrada.")

overlay_videos = []
for ext in extensoes:
    overlay_videos.extend(glob.glob(os.path.join(pasta_overlays, ext)))
if not overlay_videos:
    raise RuntimeError(f"Nenhum vídeo de overlay encontrado na pasta '{pasta_overlays}'.")
print(f"Encontrados {len(overlay_videos)} vídeos de overlay.")

# --- 3. Funções auxiliares com ffprobe ---
def get_video_info(path):
    cmd = [
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height,duration:format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', path
    ]
    out = subprocess.check_output(cmd, text=True).strip().split('\n')
    width = int(out[0])
    height = int(out[1])
    dur = out[2] if out[2] != 'N/A' else out[3]
    duration = float(dur) if dur != 'N/A' else 0.0
    return width, height, duration

largura_principal, altura_principal, duracao_principal = get_video_info(video_principal)
print(f"Principal: {largura_principal}x{altura_principal}, duração {duracao_principal:.2f}s")

altura_final = max(100, math.floor(altura_principal * altura_relativa))
if altura_final % 2: altura_final += 1
largura_final = math.floor(altura_final * 9/16)
if largura_final % 2: largura_final += 1
print(f"Tamanho de cada overlay redimensionado: {largura_final}x{altura_final}")

# --- 4. Analisar overlays ---
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
    raise RuntimeError("Nenhum overlay válido.")

# --- 5. Gerar sequências aleatórias garantindo primeiros segmentos distintos ---
num_overlays = len(posicoes)
total_videos = len(overlays_info)

# Criamos uma lista de índices disponível e embaralhamos
indices_disponiveis = list(range(total_videos))
random.shuffle(indices_disponiveis)

# Para cada overlay, vamos gerar sua sequência
sequencias = []

for ov in range(num_overlays):
    seq = []
    tempo = 0.0
    # Se ainda houver índices disponíveis, pega o próximo para começar diferente
    if indices_disponiveis:
        primeiro_idx = indices_disponiveis.pop(0)
    else:
        # Já usamos todos os índices como primeiro, escolhe qualquer um aleatório
        primeiro_idx = random.randrange(total_videos)
    
    # Adiciona o primeiro segmento
    seq.append(primeiro_idx)
    tempo += overlays_info[primeiro_idx]['eff_duration']
    
    # Agora cria uma permutação dos índices, começando com primeiro_idx e depois o resto embaralhado
    restante = [i for i in range(total_videos) if i != primeiro_idx]
    random.shuffle(restante)
    ordem = [primeiro_idx] + restante
    ptr = 1  # já usamos o primeiro
    
    while tempo < duracao_principal:
        idx = ordem[ptr]
        seq.append(idx)
        tempo += overlays_info[idx]['eff_duration']
        ptr += 1
        if ptr >= len(ordem):
            # Reembaralha para o próximo ciclo, mas mantendo o último para não repetir imediatamente?
            # Vamos apenas gerar nova permutação completa
            random.shuffle(ordem)
            ptr = 0
    
    sequencias.append(seq)

for i, seq in enumerate(sequencias):
    print(f"Sequência overlay {i+1}: {len(seq)} segmentos. Primeiro: {os.path.basename(overlays_info[seq[0]]['path'])}")

# --- 6. Montar comando ffmpeg (inalterado a partir daqui) ---
cmd = ['ffmpeg']
cmd.extend(['-i', video_principal])

total_overlay_inputs = sum(len(seq) for seq in sequencias)
for seq in sequencias:
    for idx in seq:
        cmd.extend(['-i', overlays_info[idx]['path']])

filter_parts = []
concat_labels = []
current_input_idx = 1

for ov_idx, seq in enumerate(sequencias):
    labels = []
    for i, idx in enumerate(seq):
        info = overlays_info[idx]
        w_orig = info['width']
        h_orig = info['height']

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

        label_out = f'ov{ov_idx}_{i}'
        labels.append(label_out)

        filter_parts.append(
            f"[{current_input_idx}:v]"
            f"crop={new_w}:{new_h}:{x_crop}:{y_crop},"
            f"setpts={1/aceleracao}*PTS,"
            f"scale={largura_final}:{altura_final}"
            f"[{label_out}]"
        )
        current_input_idx += 1

    concat_label = f'concat{ov_idx}'
    concat_labels.append(concat_label)
    concat_inputs = ''.join(f'[{l}]' for l in labels)
    filter_parts.append(f"{concat_inputs}concat=n={len(seq)}:v=1:a=0[{concat_label}]")

last_output = "0:v"
for ov_idx, (pos, concat_label) in enumerate(zip(posicoes, concat_labels)):
    x, y = pos.split(':')
    if ov_idx == num_overlays - 1:
        final_output = "outv"
        filter_parts.append(
            f"[{last_output}][{concat_label}]overlay={x}:{y}:shortest=1[{final_output}]"
        )
    else:
        temp_output = f"tmp{ov_idx}"
        filter_parts.append(
            f"[{last_output}][{concat_label}]overlay={x}:{y}[{temp_output}]"
        )
        last_output = temp_output

filter_complex = ';'.join(filter_parts)
cmd.extend(['-filter_complex', filter_complex])
cmd.extend(['-map', f'[{final_output}]'])
cmd.extend(['-map', '0:a?'])
cmd.extend(['-c:v', 'libx264', '-c:a', 'aac', '-preset', 'fast'])
cmd.extend(['-shortest', '-y'])

nome_saida = os.path.join(pasta_saida, "video_final_pip.mp4")
cmd.append(nome_saida)

print("\nComando ffmpeg gerado:")
print(' '.join(cmd))

print(f"\nRenderizando '{nome_saida}'...")
subprocess.run(cmd, check=True)
print("Concluído!")