import yt_dlp


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
            "title": entry.get("title"),
            "url": entry.get("url"),
            "duration": entry.get("duration"),
        })

    return tracks


if __name__ == "__main__":
    results = search_tracks("AR Rahman instrumental", max_results=3)
    for track in results:
        print(track)