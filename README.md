# 🎵 RasaPlay

> An AI-powered personal DJ that learns your taste and builds your music library — no subscriptions, no algorithms you didn't ask for.

---

## What is RasaPlay?

RasaPlay is a local-first music tool that lets you seed your taste (artists, genres, moods), finds matching tracks on YouTube, downloads them to your machine, and over time learns what you actually like — building an intelligent queue engine that gets smarter the more you use it.

No Spotify Premium. No Apple Music. No monthly fees. Your music, your data, your machine.

---

## Features (Roadmap)

| Phase | Feature | Status |
|-------|---------|--------|
| 1 | Seed artists/genres via CLI | 🔨 In Progress |
| 1 | YouTube search + audio download via yt-dlp | 🔨 In Progress |
| 1 | Local SQLite music library | 🔨 In Progress |
| 2 | Audio analysis (tempo, key, energy) via librosa | 📋 Planned |
| 2 | Rich terminal dashboard | 📋 Planned |
| 3 | AI-powered queue generation | 📋 Planned |
| 3 | Like/skip feedback loop | 📋 Planned |
| 4 | Web UI | 📋 Planned |

---

## Tech Stack

- **Python 3.12**
- **yt-dlp** — YouTube audio downloading
- **SQLite** — local music library
- **librosa** — audio feature extraction *(Phase 2)*
- **rich** — terminal UI *(Phase 2)*

---

## Getting Started

### Prerequisites

- Python 3.12+
- `yt-dlp` installed globally (`pip install yt-dlp`)

### Installation

```bash
git clone https://github.com/yourusername/rasaplay.git
cd rasaplay
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

## Project Structure

```
rasaplay/
├── main.py               # Entry point
├── search.py             # YouTube search logic
├── downloader.py         # yt-dlp wrapper
├── library.py            # SQLite library management
├── config.py             # User preferences & settings
├── downloads/            # Downloaded audio files
├── data/
│   └── library.db        # Local SQLite database
├── requirements.txt
└── .env.example
```

---

## Philosophy

RasaPlay is built on a simple idea: your music taste is personal, and your library should be too. Instead of renting access to a catalogue, RasaPlay helps you build one — track by track, shaped by what you actually love.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — contributions welcome once V1 is stable.

---

## License

MIT
