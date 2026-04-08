import yt_dlp
import re


def clean_title(title):
    title = re.sub(r'\|.*', '', title)                        # Remove everything after |
    title = re.sub(r'\(Full Video\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\(Official Video\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\(Lyrical?\s*Song?\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\(Audio\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'#\w+', '', title)                        # Remove hashtags
    title = re.sub(r'\s+:\s+', ': ', title)                   # Fix spaced colons
    title = re.sub(r' {2,}', ' ', title)                      # Collapse MULTIPLE spaces only
    return title.strip()


def search_tracks(query, max_results=5):
    search_query = f"ytsearch{max_results}:{query}"

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(search_query, download=False)

    tracks = []
    for entry in results["entries"]:
        tracks.append({
            "title": clean_title(entry.get("title")),
            "raw_title": entry.get("title"),
            "url": entry.get("url"),
            "duration": entry.get("duration"),
        })

    return tracks


if __name__ == "__main__":
    results = search_tracks("AR Rahman song", max_results=3)
    for track in results:
        print(f"Clean: {track['title']}")
        print(f"Raw:   {track['raw_title']}")
        print()