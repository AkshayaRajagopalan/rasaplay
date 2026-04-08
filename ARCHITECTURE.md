# 🏗️ RasaPlay Architecture

This document describes the technical design of RasaPlay — how the components fit together, what each module is responsible for, and how data flows through the system.

---

## High-Level Overview

```
User Input (CLI)
      │
      ▼
  config.py          ← stores user preferences, seed artists/genres
      │
      ▼
  search.py          ← queries YouTube for matching tracks
      │
      ▼
  downloader.py      ← pulls audio via yt-dlp, saves to /downloads
      │
      ▼
  library.py         ← writes track metadata to SQLite
      │
      ▼
  main.py            ← orchestrates the full flow
```

---

## Module Responsibilities

### `main.py`
The entry point. Coordinates the flow between all modules. Handles CLI interaction in Phase 1.

### `config.py`
Loads and saves user preferences — seed artists, genres, download directory, audio quality settings. Stored in a local `config.json` or `.env`.

### `search.py`
Takes an artist name or genre string and returns a list of candidate YouTube URLs. Uses `yt-dlp`'s search capability (`ytsearch:`) to avoid any external search API dependency.

```python
# Example query format
"ytsearch5:AR Rahman instrumental"
```

### `downloader.py`
Wraps `yt-dlp` to download audio from a given URL. Handles:
- Output format (MP3, 192kbps default)
- Output path (`/downloads`)
- Error handling and retry logic
- Returns metadata (title, duration, file path) on success

### `library.py`
Manages the SQLite database. Responsible for:
- Creating the schema on first run
- Inserting new track records
- Querying tracks (by artist, genre, etc.)
- Duplicate detection (checks by title + artist before downloading)

---

## Database Schema (Phase 1)

```sql
CREATE TABLE tracks (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  title       TEXT NOT NULL,
  artist      TEXT,
  genre       TEXT,
  duration    INTEGER,        -- in seconds
  file_path   TEXT NOT NULL,
  source_url  TEXT,
  date_added  TEXT,
  liked       INTEGER DEFAULT NULL  -- NULL=unrated, 1=liked, 0=skipped (Phase 3)
);
```

### Phase 2 Extension (Audio Analysis)
```sql
ALTER TABLE tracks ADD COLUMN tempo      REAL;
ALTER TABLE tracks ADD COLUMN key        TEXT;
ALTER TABLE tracks ADD COLUMN energy     REAL;
ALTER TABLE tracks ADD COLUMN danceability REAL;
```

---

## Data Flow — Phase 1

```
1. User runs: python main.py
2. main.py reads config (seed artists/genres)
3. search.py queries YouTube → returns list of URLs + titles
4. library.py checks duplicates → filters already-downloaded tracks
5. downloader.py pulls audio → saves MP3 to /downloads/
6. library.py inserts new track record into SQLite
7. Repeat for each seed artist/genre
```

---

## Directory Structure

```
rasaplay/
├── main.py
├── search.py
├── downloader.py
├── library.py
├── config.py
├── requirements.txt
├── .env.example
├── downloads/          ← audio files live here (gitignored)
└── data/
    └── library.db      ← SQLite database (gitignored)
```

> `downloads/` and `data/` are excluded from version control via `.gitignore`. Only code and schema are committed.

---

## Phase 2 Additions

- `analyzer.py` — runs librosa on each track post-download, writes audio features back to SQLite
- `queue.py` — rule-based queue builder using audio features
- `ui.py` — Rich terminal dashboard

## Phase 3 Additions

- `ai_engine.py` — natural language queue generation, taste profile management
- `recommender.py` — suggests new tracks based on like/skip history

---

## Key Design Decisions

**Why SQLite?**
Local, zero-config, file-based. No server to run. Perfectly suited for a personal tool with one user. Can be migrated to Postgres later if RasaPlay ever becomes multi-user.

**Why yt-dlp over other downloaders?**
Actively maintained, handles format selection cleanly, exposes metadata we need (title, duration), and has a Python API in addition to CLI usage.

**Why CLI first?**
Forces clean separation of logic from presentation. The core pipeline (search → download → store) should work independently of whatever UI sits on top. This makes Phase 4 (web UI) a layer added on top, not a rewrite.
