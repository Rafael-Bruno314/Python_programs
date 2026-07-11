import yt_dlp
import os
import subprocess
import time

inicio = time.time()

url = "https://www.youtube.com/watch?v=gsht-oo3YM8"
download_path = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = None

cut_video = False
start_time = "00:00:00"
end_time = "00:00:00"

def download_video_with_audio(url, download_path, ffmpeg_path, cut_video, start_time, end_time):
    try:
        ydl_opts = {
            'format': (
                'bestvideo[height<=720]+bestaudio[language=pt]/'
                'bestvideo[height<=720]+bestaudio/'
                'best[height<=720]'
            ),
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'cookiefile': os.path.join(download_path, 'cookies.txt'),
            'js_runtimes': {'node': {'path': r'C:\Program Files\nodejs\node.exe'}},  # CORRIGIDO
            'remote_components': 'ejs:github',
            'verbose': True,
        }
        if ffmpeg_path and os.path.isfile(ffmpeg_path):
            ydl_opts['ffmpeg_location'] = ffmpeg_path

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloads = info.get('requested_downloads', [])
            if not downloads:
                raise RuntimeError("Nenhum download foi registrado.")
            video_file = downloads[0]['filepath']

        if not os.path.exists(video_file):
            raise FileNotFoundError(f"Arquivo não encontrado após download: {video_file}")

        print(f"[SUCESSO] Vídeo salvo: {video_file}")

        if cut_video:
            clipped_file = os.path.join(
                download_path,
                f"{os.path.splitext(os.path.basename(video_file))[0]}_clipped.mp4"
            )
            clip_cmd = [
                ffmpeg_path if ffmpeg_path else 'ffmpeg',
                '-i', video_file,
                '-ss', start_time,
                '-to', end_time,
                '-c', 'copy',
                clipped_file
            ]
            subprocess.run(clip_cmd, check=True)
            if os.path.exists(clipped_file):
                os.remove(video_file)
                print(f"[CORTE FINALIZADO] Arquivo cortado: {clipped_file}")
        else:
            print("[INFO] Vídeo mantido integralmente.")

    except Exception as e:
        print(f"[ERRO CRÍTICO] {e}")

download_video_with_audio(url, download_path, ffmpeg_path, cut_video, start_time, end_time)

fim = time.time()
print(f"[STATS] Tempo total: {fim - inicio:.2f} segundos")