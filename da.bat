@echo off
chcp 65001
set /p url="請輸入 YouTube 影片的 URL: "
python download_audio.py %url% 