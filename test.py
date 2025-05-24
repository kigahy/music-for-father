# ffmpeg 위치 확인용

import os

ffmpeg_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "ffmpeg", "bin")

print("▶ ffmpeg path:", ffmpeg_path)
print("▶ ffmpeg.exe exists?", os.path.isfile(os.path.join(ffmpeg_path, "ffmpeg.exe")))
print("▶ ffprobe.exe exists?", os.path.isfile(os.path.join(ffmpeg_path, "ffprobe.exe")))
