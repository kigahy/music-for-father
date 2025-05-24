import yt_dlp
import os

def download_youtube_audio_as_mp3(url, output_path="./downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ffmpeg_location': r'C:\ffmpeg7.1\bin',  # 절대경로: 부모님 PC에 동일하게 세팅
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
        'quiet': False,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"\n✅ 다운로드 성공: {url}")
    except Exception as e:
        print(f"\n❌ 실패: {url}\n이유: {e}")

if __name__ == "__main__":
    print("🎵 유튜브 URL을 한 줄씩 입력하세요.")
    print("🎵 여러 개 입력하려면 엔터로 구분하고, 마지막 줄에 'y' 입력하면 다운로드 시작!\n")

    urls = []
    while True:
        line = input()
        if line.strip().lower() == "y":
            break
        if line.strip():
            urls.append(line.strip())

    print("\n🚀 다운로드 시작...\n")
    for url in urls:
        download_youtube_audio_as_mp3(url)

    print("\n🎉 모든 다운로드가 완료되었습니다! 'downloads' 폴더를 확인하세요.")
