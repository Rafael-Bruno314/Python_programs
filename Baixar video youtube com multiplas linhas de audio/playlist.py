import yt_dlp
import os
import subprocess
import time

inicio = time.time()

"""
O código vai:

    Função download_playlist_with_audio: Baixa a playlist de vídeos com a melhor qualidade disponível (720p) e tenta selecionar a trilha em português. Ela não realiza a conversão para .mp4, salvando os arquivos nos formatos originais.
    Função convert_all_to_mp4: Converte todos os arquivos de vídeo baixados (em qualquer formato) para .mp4 e remove os arquivos originais após a conversão.
"""

url = "https://www.youtube.com/watch?v=Ql-aT6sgbzY&list=PLOJyC_ALjKYH8YP0sOBmWqpRG4yQmNNvT"

download_path = '.'

ffmpeg_path = 'C:\\Users\\Rafael Bruno\\AppData\\Roaming\\Python\\Python311\\site-packages\\ffmpeg\\bin\\ffmpeg.exe'


# Função para baixar a playlist com a trilha em português, se disponível
def download_playlist_with_audio(url, download_path, ffmpeg_path):
    try:
        # Opções para download de vídeo e áudio com limitação de qualidade em 720p
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Limita a qualidade máxima a 720p
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'ffmpeg_location': ffmpeg_path,
            'extract_flat': 'in_playlist',  # Para obter a lista de vídeos da playlist sem baixar imediatamente
        }

        # Extrai as informações da playlist
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            playlist_info = ydl.extract_info(url, download=False)
            if 'entries' not in playlist_info:
                print("A URL fornecida não é uma playlist.")
                return

            # Itera sobre cada vídeo na playlist
            for index, entry in enumerate(playlist_info['entries'], start=1):
                video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                print(f"\nProcessando vídeo: {entry['title']} ({video_url})\n")
                
                video_title = entry['title']
                audio_track_id = None
                all_audio_tracks = []

                # Verifica trilhas de áudio para encontrar a trilha em português
                video_info = ydl.extract_info(video_url, download=False)
                for fmt in video_info['formats']:
                    if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none':  # Apenas trilhas de áudio
                        language = fmt.get('language')
                        if language == 'pt' or language == 'pt-BR':  # Procura trilhas em português
                            print(f"Encontrada trilha de áudio em português: {fmt['format_id']}")
                            audio_track_id = fmt['format_id']
                            break
                        else:
                            all_audio_tracks.append(fmt['format_id'])

                # Caso não tenha encontrado trilha em português, usa a primeira trilha disponível
                if audio_track_id is None:
                    print("Trilha em português não encontrada; usando a primeira trilha de áudio disponível.")
                    audio_track_id = all_audio_tracks[0] if all_audio_tracks else None

                # Ajusta o formato específico para baixar o vídeo com a trilha de áudio selecionada
                video_ydl_opts = ydl_opts.copy()
                video_ydl_opts['format'] = f'bestvideo[height<=720]+{audio_track_id}'
                video_ydl_opts['outtmpl'] = f"{download_path}/{index:02d}_{video_title}.%(ext)s"

                # Faz o download do vídeo e áudio selecionados
                with yt_dlp.YoutubeDL(video_ydl_opts) as ydl_video:
                    ydl_video.download([video_url])

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para converter todos os vídeos baixados para .mp4 e remover os arquivos originais
def convert_all_to_mp4(directory, ffmpeg_path):
    for filename in os.listdir(directory):
        if filename.endswith(('.mkv', '.webm', '.avi', '.mov', '.flv')):  # Adicione mais extensões conforme necessário
            original_file = os.path.join(directory, filename)
            mp4_file = os.path.join(directory, os.path.splitext(filename)[0] + '.mp4')

            print(f"Convertendo {original_file} para {mp4_file}...")
            conversion_command = [
                ffmpeg_path, '-i', original_file,
                '-c:v', 'copy', '-c:a', 'copy', mp4_file
            ]
            subprocess.run(conversion_command, check=True)

            # Remove o arquivo original após a conversão
            if os.path.exists(mp4_file):
                os.remove(original_file)
                print(f"Arquivo {original_file} excluído após conversão para .mp4.")

# Executa o download da playlist com áudio em português ou outra trilha disponível
download_playlist_with_audio(url, download_path, ffmpeg_path)

# Execute a função para converter todos os arquivos de vídeo na pasta de download
convert_all_to_mp4(download_path, ffmpeg_path)

fim = time.time()
print("O tempo de execução foi de: ", fim - inicio, " segundos")