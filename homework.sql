-- Создание таблицы для авторов
CREATE TABLE IF NOT EXISTS authors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

-- Создание таблицы для связи авторов и песен
CREATE TABLE IF NOT EXISTS song_authors (
  song_id INTEGER,
  author_id INTEGER,
  FOREIGN KEY (song_id) REFERENCES songs(id),
  FOREIGN KEY (author_id) REFERENCES authors(id),
  PRIMARY KEY (song_id, author_id)
);

-- Добавление альбомов
INSERT INTO albums (title, description, year) VALUES
('First Album', 'Description of the first album', 2020),
('Second Album', 'Description of the second album', 2022);

-- Добавление авторов
INSERT INTO authors (name) VALUES
('Author One'),
('Author Two');

-- Добавление песен
INSERT INTO songs (title, duration, album_id) VALUES
('Song 1', 210, 1),
('Song 2', 180, 1),
('Song 3', 200, 1),
('Song 4', 150, 1),
('Song 5', 220, 1),
('Song 6', 190, 2),
('Song 7', 230, 2),
('Song 8', 175, 2),
('Song 9', 205, 2),
('Song 10', 240, 2);

-- Связь песен с авторами
INSERT INTO song_authors (song_id, author_id) VALUES
(1, 1), (2, 1), (3, 1), (4, 2), (5, 2),
(6, 1), (7, 1), (8, 2), (9, 2), (10, 1);
