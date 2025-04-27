#!/usr/bin/env python3
import os
import subprocess
import argparse

def download_audio(url):
    try:
        # 構建 yt-dlp 的命令
        command = ['yt-dlp', '-x', url, '--audio-format', 'mp3']
        
        # 使用 subprocess 執行命令
        subprocess.run(command, check=True)
        print(f"音檔已成功下載並轉換為 MP3 格式: {url}")
    except subprocess.CalledProcessError as e:
        print(f"下載過程中發生錯誤: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='下載 YouTube 音檔並轉換為 MP3 格式')
    parser.add_argument('url', help='YouTube 影片的 URL')
    args = parser.parse_args()
    
    download_audio(args.url)
