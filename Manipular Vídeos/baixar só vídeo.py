import yt_dlp

url = "https://www.youtube.com/watch?v=3JiMr-HgHJ8"  # troque pela sua URL

ydl_opts = {
    'format': 'bestvideo[height<=720]',  # vídeo em até 720p (sem áudio)
    'outtmpl': './downloads/%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
