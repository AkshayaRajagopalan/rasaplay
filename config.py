import json
import os

CONFIG_PATH = "config.json"

DEFAULT_CONFIG = {
    "seed_artists": [],
    "seed_genres": [],
    "download_dir": "downloads",
    "max_results_per_search": 5,
    "max_duration_seconds": 600
}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def add_artist(artist):
    config = load_config()
    if artist not in config["seed_artists"]:
        config["seed_artists"].append(artist)
        save_config(config)
        print(f"✅ Added artist: {artist}")
    else:
        print(f"⚠️  {artist} already in your seeds")


def add_genre(genre):
    config = load_config()
    if genre not in config["seed_genres"]:
        config["seed_genres"].append(genre)
        save_config(config)
        print(f"✅ Added genre: {genre}")
    else:
        print(f"⚠️  {genre} already in your seeds")


if __name__ == "__main__":
    add_artist("AR Rahman")
    add_artist("Ilaiyaraaja")
    add_genre("Carnatic fusion")
    print(load_config())
