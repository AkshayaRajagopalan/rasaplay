# 🗺️ RasaPlay Roadmap

This document tracks the phased development of RasaPlay. Each phase builds on the last and represents a shippable, meaningful milestone.

---

## Phase 1 — The Pipeline
**Goal:** A working CLI that takes your music taste as input and builds a local downloaded library.

### Milestones
- [ ] CLI onboarding — user seeds 3–5 artists or genres
- [ ] YouTube search integration — find top tracks per artist/genre
- [ ] yt-dlp downloader — pull audio as MP3 to `/downloads`
- [ ] SQLite library — store track metadata (title, artist, duration, file path, date added)
- [ ] Download logging — track successes, failures, and skips
- [ ] Basic duplicate detection — don't re-download existing tracks

### Definition of Done
User can run `python main.py`, enter some artists they like, and end up with a populated local music library.

---

## Phase 2 — The Brain (Offline Analysis)
**Goal:** Understand the music in the library at an audio level.

### Milestones
- [ ] librosa integration — extract tempo, key, energy, danceability per track
- [ ] Store analysis results in SQLite alongside track metadata
- [ ] Rule-based queue builder — e.g. "give me high energy tracks in a major key"
- [ ] Rich terminal dashboard — browsable library view, now playing, queue display

### Definition of Done
User can launch a terminal dashboard, see their library, and play a rule-based queue with basic audio intelligence.

---

## Phase 3 — The AI Layer
**Goal:** Natural language control and taste learning.

### Milestones
- [ ] Prompt-based queue generation — "something slow and melancholic for late night"
- [ ] Like/skip feedback system — stores user reactions per track
- [ ] Taste profile — builds a preference model from feedback over time
- [ ] Recommendation engine — suggests new tracks based on taste profile
- [ ] Auto-seed — finds new music without user needing to input artists manually

### Definition of Done
User can describe a vibe in plain language and RasaPlay builds an intelligent queue. The more they use it, the better it gets.

---

## Phase 4 — The Face (Web UI)
**Goal:** A proper visual interface for the full experience.

### Milestones
- [ ] Flask or FastAPI backend
- [ ] React or plain HTML/CSS frontend
- [ ] Now Playing view with track metadata
- [ ] Library browser with search and filters
- [ ] Queue management UI
- [ ] Settings panel (download directory, audio quality, etc.)

### Definition of Done
RasaPlay runs in the browser. Someone who has never used a terminal can use it.

---

## Guiding Principles

- **Local first** — all data stays on your machine
- **No subscriptions** — no APIs that require payment to function
- **Progressive complexity** — each phase is usable on its own
- **Clean code over fast code** — this is a portfolio project; readability matters

---

## Version History

| Version | Phase | Notes |
|---------|-------|-------|
| v0.1.0 | Phase 1 | Initial pipeline — search, download, library |
| v0.2.0 | Phase 1 | Duplicate detection + download logging |
| v0.3.0 | Phase 2 | Audio analysis + SQLite expansion |
| v0.4.0 | Phase 2 | Rich terminal dashboard |
| v1.0.0 | Phase 3 | AI queue engine + taste learning |
| v2.0.0 | Phase 4 | Web UI |
