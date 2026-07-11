#!/usr/bin/env python3
"""
Corta todos os vídeos da pasta do script em segmentos de duração fixa (padrão 30s).
Cada vídeo gera uma pasta com seu prefixo (3 primeiras palavras) contendo as partes.
"""

import subprocess
import sys
from pathlib import Path
import re

# ========== CONFIGURAÇÕES ==========
DURATION = 30                        # duração de cada parte em segundos
RESET_TIMESTAMPS = True              # reinicia os timestamps em cada segmento
EXTENSOES_VIDEO = ('.mp4', '.mkv', '.avi', '.mov', '.webm', '.flv', '.wmv')
# ===================================

def extrair_prefixo(nome_base, max_palavras=3):
    """
    Extrai as primeiras `max_palavras` palavras do nome base.
    Considera como separadores: espaço, sublinhado, hífen.
    Retorna o prefixo em minúsculas e sem espaços (substitui espaços por '_').
    """
    # Substitui sublinhados e hífens por espaços para unificar
    nome_limpo = re.sub(r'[_\-]+', ' ', nome_base)
    # Divide por espaços e filtra palavras vazias
    palavras = [p for p in nome_limpo.split(' ') if p]
    # Pega as primeiras palavras
    prefixo_palavras = palavras[:max_palavras]
    # Junta com sublinhado e retorna em minúsculas
    prefixo = '_'.join(prefixo_palavras).lower()
    return prefixo

# Pasta onde o script está localizado
script_dir = Path(__file__).parent

# Lista todos os arquivos de vídeo na pasta do script
video_files = [f for f in script_dir.iterdir() if f.suffix.lower() in EXTENSOES_VIDEO]

if not video_files:
    print("Nenhum vídeo encontrado na pasta do script.")
    sys.exit(0)

for video_path in video_files:
    base_name = video_path.stem
    prefix = extrair_prefixo(base_name, max_palavras=3)
    
    # Se o prefixo ficar vazio (nome só com caracteres especiais), use "video"
    if not prefix:
        prefix = "video"
    
    output_dir = script_dir / prefix
    output_dir.mkdir(exist_ok=True)
    
    output_pattern = output_dir / f"{prefix}_%03d.mp4"
    
    cmd = [
        "ffmpeg",
        "-i", str(video_path),
        "-c", "copy",
        "-map", "0",
        "-segment_time", str(DURATION),
        "-f", "segment",
    ]
    
    if RESET_TIMESTAMPS:
        cmd.extend(["-reset_timestamps", "1"])
    
    cmd.append(str(output_pattern))
    
    print(f"\nProcessando: {video_path.name}")
    print(" ".join(cmd))
    
    try:
        # Captura a saída de erro para diagnóstico
        resultado = subprocess.run(cmd, capture_output=True, text=True)
        if resultado.returncode != 0:
            print(f"❌ Erro ao processar {video_path.name}:")
            print(resultado.stderr)
        else:
            # Verifica se pelo menos um arquivo foi gerado
            partes = list(output_dir.glob(f"{prefix}_*.mp4"))
            if partes:
                print(f"✔️ Concluído! {len(partes)} parte(s) salva(s) em: {output_dir}")
            else:
                print(f"⚠️ Nenhum segmento foi gerado para {video_path.name} (possível erro silencioso).")
    except Exception as e:
        print(f"❌ Falha inesperada com {video_path.name}: {e}")

print("\nTodos os vídeos foram processados.")