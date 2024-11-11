import yt_dlp
import os
import subprocess
import time

inicio = time.time()

"""
O código vai:

    Buscar a faixa de áudio em português e usá-la, se estiver disponível.
    Baixar o vídeo em 720p rapidamente com a trilha de áudio correta usando cópia de fluxo.
    Usar ffmpeg para mesclar o vídeo e o áudio selecionado e salvar o resultado final em .mp4.
    Permitir que o usuário escolha um intervalo específico do vídeo.
"""

url = "https://www.youtube.com/watch?v=GnZ3dogED7w"
download_path = '.'
ffmpeg_path = 'C:\\Users\\Rafael Bruno\\AppData\\Roaming\\Python\\Python311\\site-packages\\ffmpeg\\bin\\ffmpeg.exe'

# Defina o intervalo de tempo desejado (em formato "HH:MM:SS")
start_time = "00:00:30"  # Exemplo: começar aos 30 segundos
end_time = "00:01:30"    # Exemplo: terminar em 1 minuto e 30 segundos

#----------------------------------

def download_video_with_audio(url, download_path, ffmpeg_path):
    try:
        # Opções para download de vídeo e áudio com limitação de qualidade em 720p
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Limita a qualidade máxima a 720p
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'ffmpeg_location': ffmpeg_path,
        }

        # Primeira extração de informações para verificar as trilhas de áudio disponíveis
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict['title']
            audio_track_id = None
            all_audio_tracks = []

            # Procura por uma trilha em português
            for fmt in info_dict['formats']:
                if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none':  # Apenas trilhas de áudio
                    language = fmt.get('language')
                    if language == 'pt' or language == 'pt-BR':  # Procura trilhas em português
                        print(f"Encontrada trilha de áudio em português: {fmt['format_id']}")
                        audio_track_id = fmt['format_id']
                        break
                    else:
                        all_audio_tracks.append(fmt['format_id'])

            # Caso não tenha encontrado trilha em português, usa todas as trilhas disponíveis
            if audio_track_id is None:
                print("Trilha em português não encontrada; baixando todas as trilhas de áudio disponíveis.")
                audio_track_id = all_audio_tracks[0]  # Seleciona a primeira trilha disponível se não houver português

            # Ajusta o formato específico para baixar o vídeo com a trilha de áudio selecionada
            ydl_opts['format'] = f'bestvideo[height<=720]+{audio_track_id}'

            # Faz o download do vídeo e áudio selecionados
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                video_file = os.path.join(download_path, f"{video_title}.mp4")

            # Verifica se o vídeo foi baixado com sucesso
            if os.path.exists(video_file):
                print(f"Vídeo baixado com sucesso em: {video_file}")
                
                # Define o nome do arquivo de saída para o trecho
                clipped_file = os.path.join(download_path, f"{video_title}_clipped.mp4")

                # Usa ffmpeg para cortar o vídeo no intervalo desejado
                print(f"Cortando o vídeo para o intervalo de {start_time} até {end_time}...")
                clip_command = [
                    ffmpeg_path, '-i', video_file,
                    '-ss', start_time, '-to', end_time,
                    '-c', 'copy', clipped_file
                ]
                subprocess.run(clip_command, check=True)

                print(f"Trecho do vídeo salvo como: {clipped_file}")

            else:
                print("Falha ao baixar o vídeo.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa o download do vídeo com áudio em português ou todas as trilhas se necessário
download_video_with_audio(url, download_path, ffmpeg_path)

fim = time.time()
print("O tempo de execução foi de: ", fim - inicio, " segundos")