# 부모님을 위한 유튜브 음원추출 딸깍기

### 패키지 설치
```
pip install yt-dlp
```

ffmpeg 설치
- url : https://www.gyan.dev/ffmpeg/builds/
- release build에서 `ffmpeg-release-essentials.zip` 다운로드
- `C:\`에 `ffmpeg7.1`라는 이름으로 압축 해제
- 환경변수 Path에 C:\ffmpeg7.1\bin 등록 


### .exe로 배포

.exe파일 만들기
```
pyinstaller --onefile new.py
```

프로젝트 구조
```
MyMP3Downloader/
├── new.exe 
├── ffmpeg/
│   └── bin/
│       ├── ffmpeg.exe
│       └── ffprobe.exe
├── downloads/
└── README.txt
```



### 최종 결과물
- .exe파일을 만들어 ffmpeg와 압축한 다음, 음악다운.zip으로 압축하여 부모님 컴퓨터에 보내드림
- 아빠의 리액션이 상당히 좋아 뿌듯했음