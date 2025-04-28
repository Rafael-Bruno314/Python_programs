import yt_dlp
import os
import subprocess
import time

inicio = time.time()

"""
Fluxo principal do programa:
1. download_playlist_with_audio:
   - Baixa todos os vídeos de uma playlist YouTube em 720p
   - Prioriza áudio em português quando disponível
   - Mantém os formatos originais dos vídeos
2. convert_all_to_mp4:
   - Converte todos os vídeos baixados para MP4
   - Remove os arquivos originais após conversão
   - Preserva a qualidade original (cópia direta de codecs)
"""

# Configurações globais

# Adicionar a url da playlist desejada
url = "https://www.youtube.com/watch?v=Ql-aT6sgbzY&list=PLOJyC_ALjKYH8YP0sOBmWqpRG4yQmNNvT" 

download_path = '.'  # Diretório atual para salvar os arquivos
download_path = '.'  # Diretório atual para downloads
ffmpeg_path = 'C:\\Users\\Rafael Bruno\\AppData\\Roaming\\Python\\Python311\\site-packages\\ffmpeg\\bin\\ffmpeg.exe'

def download_playlist_with_audio(url, download_path, ffmpeg_path):
    """
    Baixa todos os vídeos de uma playlist do YouTube com as seguintes características:
    - Resolução máxima de 720p
    - Áudio em português (prioritário) ou primeira trilha disponível
    - Mantém formato original do container
    
    Parâmetros:
        url (str): URL da playlist YouTube
        download_path (str): Diretório de destino
        ffmpeg_path (str): Caminho do executável ffmpeg
    """
    try:
        # Configuração base para yt-dlp
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'ffmpeg_location': ffmpeg_path,
            'extract_flat': 'in_playlist',  # Analisa a playlist sem baixar
        }

        # Fase 1: Análise da playlist
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            playlist_info = ydl.extract_info(url, download=False)
            
            if 'entries' not in playlist_info:
                print("[ERRO] URL não contém uma playlist válida")
                return

            # Fase 2: Processamento por vídeo
            for index, entry in enumerate(playlist_info['entries'], start=1):
                video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                print(f"\n[PROCESSANDO] Vídeo {index}: {entry['title']}")
                
                video_title = entry['title']
                audio_track_id = None
                all_audio_tracks = []

                # Análise das trilhas de áudio disponíveis
                video_info = ydl.extract_info(video_url, download=False)
                for fmt in video_info['formats']:
                    if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none':
                        language = fmt.get('language')
                        if language in ('pt', 'pt-BR'):  # Preferência por PT
                            print(f"[ÁUDIO] Trilha PT encontrada (ID: {fmt['format_id']})")
                            audio_track_id = fmt['format_id']
                            break
                        all_audio_tracks.append(fmt['format_id'])

                # Fallback para outras trilhas se PT não existir
                if audio_track_id is None and all_audio_tracks:
                    print("[AVISO] Usando trilha de áudio alternativa")
                    audio_track_id = all_audio_tracks[0]

                # Configuração específica para este vídeo
                video_ydl_opts = {
                    **ydl_opts,
                    'format': f'bestvideo[height<=720]+{audio_track_id}',
                    'outtmpl': f"{download_path}/{index:02d}_{video_title}.%(ext)s"  # Padrão de nome com numeração
                }

                # Download efetivo
                with yt_dlp.YoutubeDL(video_ydl_opts) as ydl_video:
                    print(f"[DOWNLOAD] Iniciando...")
                    ydl_video.download([video_url])
                    print(f"[SUCESSO] Vídeo {index} concluído")

    except Exception as e:
        print(f"[ERRO CRÍTICO] Falha no download: {str(e)}")

def convert_all_to_mp4(directory, ffmpeg_path):
    """
    Converte vídeos para MP4 sem re-encode (stream copy)
    
    Parâmetros:
        directory (str): Pasta contendo os vídeos
        ffmpeg_path (str): Caminho do executável ffmpeg
    """
    print("\n[CONVERSÃO] Iniciando processo de conversão para MP4")
    
    for filename in os.listdir(directory):
        # Lista de formatos suportados para conversão
        if filename.lower().endswith(('.mkv', '.webm', '.avi', '.mov', '.flv')):
            original_file = os.path.join(directory, filename)
            base_name = os.path.splitext(filename)[0]
            mp4_file = os.path.join(directory, f"{base_name}.mp4")

            print(f"[CONVERTENDO] {filename} → MP4")
            
            # Comando FFmpeg para conversão direta (sem perda de qualidade)
            conversion_command = [
                ffmpeg_path, '-i', original_file,
                '-c:v', 'copy',  # Copia o vídeo sem recompressão
                '-c:a', 'copy',  # Copia o áudio sem recompressão
                '-y',  # Sobrescreve se existir
                mp4_file
            ]
            
            try:
                subprocess.run(conversion_command, check=True)
                
                # Verificação e limpeza
                if os.path.exists(mp4_file):
                    os.remove(original_file)
                    print(f"[LIMPEZA] Removido arquivo original: {filename}")
                else:
                    print(f"[AVISO] Arquivo MP4 não foi gerado: {mp4_file}")
                    
            except subprocess.CalledProcessError as e:
                print(f"[ERRO] Falha na conversão de {filename}: {str(e)}")

# Execução principal
print("[INÍCIO] Processamento da playlist")
download_playlist_with_audio(url, download_path, ffmpeg_path)

print("\n[ETAPA 2] Conversão para MP4")
convert_all_to_mp4(download_path, ffmpeg_path)

# Benchmarking
fim = time.time()
print(f"\n[FINALIZADO] Tempo total: {fim - inicio:.2f} segundos")