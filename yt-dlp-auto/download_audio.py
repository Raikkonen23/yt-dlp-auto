import os
import subprocess

def download_audio(url):
    try:
        # 構建 yt-dlp 的命令
        command = ['yt-dlp', '-x', url, '--audio-format', 'mp3']
        
        # 使用 subprocess 執行命令
        subprocess.run(command, check=True)
        print(f"音頻已成功下載並轉換為 MP3 格式: {url}")
    except subprocess.CalledProcessError as e:
        print(f"下載過程中發生錯誤: {e}")

if __name__ == "__main__":
    youtube_url = input("請輸入 YouTube 視頻的 URL: ")
    download_audio(youtube_url)
