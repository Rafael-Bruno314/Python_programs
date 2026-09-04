import yt_dlp

url = "https://www.youtube.com/watch?v=Bpfw47x5a90"  # substitua pela URL

ydl_opts = {
    'format': 'bestaudio',          # baixa o melhor áudio disponível (qualquer formato)
    'outtmpl': './downloads/%(title)s.%(ext)s',  # salva com título e extensão original
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
