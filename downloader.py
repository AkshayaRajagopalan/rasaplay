import yt_dlp
import os


def download_track(url, title, download_dir="downloads"):
    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{download_dir}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"✅ Downloaded: {title}")


if __name__ == "__main__":
    test_url = "https://www.youtube.com/watch?v=a1NTKbiA3xg"
    download_track(test_url, "AR Rahman Test")
