import sys
import yt_dlp
import os
import time

# 실행 위치 기준으로 ffmpeg 경로 설정 (어디서 실행해도 작동)
# base_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
# ffmpeg_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "ffmpeg", "bin")

# base_dir = os.path.abspath(os.path.dirname(__file__))
# ffmpeg_path = os.path.join(base_dir, "ffmpeg", "bin")


# 실행 위치 기준으로 ffmpeg 경로 설정 (PyInstaller 대응 완벽)
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.abspath(os.path.dirname(__file__))

ffmpeg_path = os.path.join(base_dir, "ffmpeg", "bin")


def download_youtube_audio_as_mp3(url, output_path="./받은 음악들"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
        'quiet': False,
        'noplaylist': True,
        'ffmpeg_location': ffmpeg_path
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"\n다운로드 성공: {url}")
    except Exception as e:
        print(f"\n다운로드 실패: {url}\n이유: {e}")

if __name__ == "__main__":
    # print(f"🔍 현재 ffmpeg 경로: {ffmpeg_path}")
    # print(f"🔍 ffmpeg.exe 있음? {os.path.isfile(os.path.join(ffmpeg_path, 'ffmpeg.exe'))}")
    # print(f"🔍 ffprobe.exe 있음? {os.path.isfile(os.path.join(ffmpeg_path, 'ffprobe.exe'))}")

    print("가현의 뮤직타임! 유튜브 URL을 한 줄씩 입력하세요.")
    print("여러 개 다운받고 싶으면 엔터로 한줄씩 적고, 마지막 줄에 'y' 입력하면 다운로드 시작!\n")

    urls = []
    while True:
        line = input()
        if line.strip().lower() == "y":
            break
        if line.strip():
            urls.append(line.strip())

    print("\n가현이가 음악 가져오는 중...\n")
    for url in urls:
        download_youtube_audio_as_mp3(url)

    print("\n가현이가 음악을 저장 했어요! [받은 음악들] 폴더를 확인하세요.")
    print("아빠 힘내세요~!! 노래 재밌게 들으시길 ^_^")
    time.sleep(3)
