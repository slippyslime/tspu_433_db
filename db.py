import sqlite3


def get_connection(db_path="music.db"):
    """Создает подключение к базе данных SQLite."""
    return sqlite3.connect(db_path)


def initialize_schema():
    """Создает необходимые таблицы в базе данных, если они еще не существуют."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS albums (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                year INTEGER
            );

            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                duration INTEGER NOT NULL,
                album_id INTEGER,
                FOREIGN KEY (album_id) REFERENCES albums(id)
            );

            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS song_authors (
                song_id INTEGER,
                author_id INTEGER,
                PRIMARY KEY (song_id, author_id),
                FOREIGN KEY (song_id) REFERENCES songs(id),
                FOREIGN KEY (author_id) REFERENCES authors(id)
            );
        """)
        print("✅ Структура базы данных успешно инициализирована.")


def insert_album(title, description, year):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO albums (title, description, year) VALUES (?, ?, ?);",
            (title, description, year)
        )
        print(f"🎵 Добавлен альбом: '{title}' ({year})")


def insert_author(name):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO authors (name) VALUES (?);",
            (name,)
        )
        print(f"✍️ Добавлен автор: {name}")


def insert_song(title, duration, album_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO songs (title, duration, album_id) VALUES (?, ?, ?);",
            (title, duration, album_id)
        )
        song_id = cur.lastrowid
        print(f"🎶 Добавлена песня: '{title}' (длительность: {duration} сек.)")
        return song_id


def link_song_to_author(song_id, author_id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO song_authors (song_id, author_id) VALUES (?, ?);",
            (song_id, author_id)
        )
        print(f"🔗 Связан автор #{author_id} с песней #{song_id}")


if __name__ == "__main__":
    initialize_schema()

    # Примеры добавления данных
    insert_album("Now or Never", "Debut Album", 2019)
    insert_album("Second Chance", "Follow-up album", 2021)

    insert_author("Lana Miles")
    insert_author("John Dee")

    song1_id = insert_song("Echoes", 242, 1)
    song2_id = insert_song("Waves", 205, 1)

    link_song_to_author(song1_id, 1)
    link_song_to_author(song2_id, 2)
