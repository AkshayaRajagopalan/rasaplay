import sqlite3
import os
from datetime import datetime


DB_PATH = "data/library.db"


def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT NOT NULL,
            artist      TEXT,
            genre       TEXT,
            duration    INTEGER,
            file_path   TEXT NOT NULL,
            source_url  TEXT,
            date_added  TEXT,
            liked       INTEGER DEFAULT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database ready")


def track_exists(title):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tracks WHERE title = ?", (title,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def save_track(title, artist, genre, duration, file_path, source_url):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tracks (title, artist, genre, duration, file_path, source_url, date_added)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (title, artist, genre, duration, file_path, source_url, datetime.now().isoformat()))

    conn.commit()
    conn.close()
    print(f"✅ Saved to library: {title}")


if __name__ == "__main__":
    init_db()
    save_track(
        title="AR Rahman Test Track",
        artist="AR Rahman",
        genre="instrumental",
        duration=300,
        file_path="downloads/test.mp3",
        source_url="https://www.youtube.com/watch?v=a1NTKbiA3xg"
    )
