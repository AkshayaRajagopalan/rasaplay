from config import load_config
from search import search_tracks
from downloader import download_track
from library import init_db, track_exists, save_track
import os


def run():
    print("🎵 RasaPlay starting up...")
    init_db()

    config = load_config()
    download_dir = config["download_dir"]
    max_results = config["max_results_per_search"]
    max_duration = config["max_duration_seconds"]

    seeds = []
    for artist in config["seed_artists"]:
        seeds.append({"query": f"{artist} song", "artist": artist, "genre": None})
    for genre in config["seed_genres"]:
        seeds.append({"query": f"{genre} music", "artist": None, "genre": genre})

    for seed in seeds:
        print(f"\n🔍 Searching: {seed['query']}")
        results = search_tracks(seed["query"], max_results=max_results)

        for track in results:
            title = track["title"]
            url = track["url"]
            duration = track["duration"]

            if duration and duration > max_duration:
                print(f"⏭️  Skipping (too long): {title}")
                continue

            if track_exists(title):
                print(f"⏭️  Already in library: {title}")
                continue

            print(f"⬇️  Downloading: {title}")
            success = download_track(url, title, download_dir)

            if success:
                file_path = os.path.join(download_dir, f"{title}.mp3")
                save_track(
                    title=title,
                    artist=seed["artist"],
                    genre=seed["genre"],
                    duration=duration,
                    file_path=file_path,
                    source_url=url
                )

    print("\n✅ RasaPlay done!")


if __name__ == "__main__":
    run()
