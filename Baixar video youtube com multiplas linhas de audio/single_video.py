import yt_dlp
import os
import subprocess
import time

inicio = time.time()

"""
Objetivo do código:
    - Buscar a faixa de áudio em português (se disponível) em vídeos do YouTube.
    - Baixar o vídeo em resolução 720p com a melhor trilha de áudio disponível.
    - Mesclar vídeo e áudio usando ffmpeg.
    - Opcionalmente cortar um trecho específico do vídeo conforme definido pelo usuário.
"""

url = "https://www.youtube.com/watch?v=GnZ3dogED7w" # Adicionar a url desejada
download_path = '.'  # Diretório atual para salvar os arquivos
ffmpeg_path = 'C:\\Users\\Rafael Bruno\\AppData\\Roaming\\Python\\Python311\\site-packages\\ffmpeg\\bin\\ffmpeg.exe'

# Configurações de corte (modificáveis pelo usuário)
cut_video = True  # True para ativar o corte, False para download completo
start_time = "00:00:00"  # Formato HH:MM:SS (início do corte)
end_time = "00:00:30"    # Formato HH:MM:SS (fim do corte)

def download_video_with_audio(url, download_path, ffmpeg_path, cut_video, start_time, end_time):
    """
    Baixa vídeos do YouTube com controle de qualidade e opção de corte.

    Parâmetros:
        url (str): URL do vídeo no YouTube
        download_path (str): Diretório de destino
        ffmpeg_path (str): Caminho do executável ffmpeg
        cut_video (bool): Ativa/desativa o corte
        start_time (str): Tempo inicial para corte
        end_time (str): Tempo final para corte
    """
    try:
        # Configuração base para o yt-dlp
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Prioriza 720p
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Padrão de nome do arquivo
            'ffmpeg_location': ffmpeg_path,  # Localização do ffmpeg
        }

        # Fase 1: Análise do vídeo para identificar trilhas de áudio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict['title']
            audio_track_id = None
            all_audio_tracks = []

            # Verifica cada formato disponível
            for fmt in info_dict['formats']:
                if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none':  # Filtra apenas áudio
                    language = fmt.get('language')
                    if language in ('pt', 'pt-BR'):  # Preferência por português
                        print(f"[DEBUG] Trilha PT encontrada: ID {fmt['format_id']}")
                        audio_track_id = fmt['format_id']
                        break
                    all_audio_tracks.append(fmt['format_id'])

            # Fallback: Usa primeira trilha disponível se não encontrar PT
            if audio_track_id is None and all_audio_tracks:
                print("[AVISO] Usando trilha de áudio alternativa (PT não disponível)")
                audio_track_id = all_audio_tracks[0]

            # Atualiza o formato com a trilha de áudio selecionada
            ydl_opts['format'] = f'bestvideo[height<=720]+{audio_track_id}'

            # Fase 2: Download efetivo
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                video_file = os.path.join(download_path, f"{video_title}.mp4")

            # Pós-processamento
            if os.path.exists(video_file):
                print(f"[SUCESSO] Arquivo salvo em: {video_file}")

                if cut_video:
                    clipped_file = os.path.join(download_path, f"{video_title}_clipped.mp4")
                    print(f"[PROCESSO] Cortando vídeo ({start_time} → {end_time})...")
                    
                    # Comando FFmpeg para corte sem re-encode (rápido)
                    clip_command = [
                        ffmpeg_path, '-i', video_file,
                        '-ss', start_time, '-to', end_time,
                        '-c', 'copy',  # Método de cópia direta (sem perda de qualidade)
                        clipped_file
                    ]
                    
                    subprocess.run(clip_command, check=True)

                    # Limpeza: Remove original se o corte for bem-sucedido
                    if os.path.exists(clipped_file):
                        os.remove(video_file)
                        print(f"[CORTE FINALIZADO] Arquivo cortado: {clipped_file}")
                else:
                    print("[INFO] Vídeo mantido integralmente")

            else:
                print("[ERRO] Arquivo de vídeo não foi gerado")

    except Exception as e:
        print(f"[ERRO CRÍTICO] Falha no processo: {str(e)}")

# Execução principal
download_video_with_audio(url, download_path, ffmpeg_path, cut_video, start_time, end_time)

# Benchmarking
fim = time.time()
print(f"[STATS] Tempo total de execução: {fim - inicio:.2f} segundos")