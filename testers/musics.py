import yt_dlp
import os

def download_youtube_audio_as_mp3(url, output_path="./downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ffmpeg_location': r'C:\ffmpeg7.1\bin',  # ✅ 네가 설치한 경로
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"✅ Success: {url}")
    except Exception as e:
        print(f"❌ Failed: {url}\nReason: {e}")

if __name__ == "__main__":
    urls = [
        "https://youtu.be/54Uq3BH6DwY?si=OCDg98gGZOhijGOQ",
        "https://youtu.be/447yaU_4DF8?si=_vkNiap9KidVhmEh",
        "https://youtu.be/OOO4ROO_sPM?si=IC_uA2WmbcC3b0Ko",
        "https://youtu.be/NBA8AV5ni-4?si=HRl5PakdAe6mUlV9",
        "https://youtu.be/pRLf_bBaiCA?si=-MHFKeQbBkoZCwvQ",
        "https://youtu.be/yQdiUiUTlcQ?si=Die9N3T1WSfsAi-3",
        "https://youtu.be/Gge8y11GNMQ?si=wMhTSz_1WGLDkBi5"
    ]

    for url in urls:
        download_youtube_audio_as_mp3(url)
