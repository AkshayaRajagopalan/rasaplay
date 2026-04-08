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

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Downloaded: {title}")
        return True

    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Download failed: {title}")
        print(f"   Reason: {e}")
        return False

    except Exception as e:
        print(f"❌ Unexpected error for: {title}")
        print(f"   Reason: {e}")
        return False
    