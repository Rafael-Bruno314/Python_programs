import os
import subprocess

def comprimir_video(caminho_entrada, percentual, qualidade=28, bitrate='500k'):
    """Compressão inteligente com controle de codec e bitrate"""
    pasta = os.path.dirname(caminho_entrada)
    nome_base = os.path.splitext(os.path.basename(caminho_entrada))[0]
    caminho_saida = os.path.join(pasta, f"{nome_base}_otimizado.mp4")

    # Redimensionar + comprimir diretamente com FFmpeg (mais eficiente)
    comando = [
        'ffmpeg',
        '-y',
        '-i', caminho_entrada,
        '-vf', f"scale=iw*{percentual/100}:ih*{percentual/100}",
        '-c:v', 'libx264',  # Codec H.264
        '-crf', str(qualidade),  # (quanto menor, melhor qualidade)
        '-preset', 'slow',  # Compressão mais eficiente
        '-c:a', 'aac',
        '-b:a', bitrate,
        caminho_saida
    ]
    
    subprocess.run(comando, check=True)
    return caminho_saida


# Configurações (teste com esses valores)
caminho_original = r"C:\Users\Rafael Bruno\Documents\Programacao\Python\Compressão de vídeo\video02.mp4"

# Verificar existência do arquivo original
if not os.path.exists(caminho_original):
    raise FileNotFoundError(f"Arquivo não encontrado: {caminho_original}")


comprimir_video(
    caminho_original,
    percentual=50,  # Redução de resolução (0 - 100) (valores entre 65 a 75 retornam erro, evite)
    qualidade=28,    # Aumente para reduzir tamanho (Melhores valores para compressão estão entre 23 a 32)
    bitrate='96k'   # Reduza conforme necessário (altera a qualidade do áudio)
)
   