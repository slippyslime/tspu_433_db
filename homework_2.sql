SELECT 
    albums.title AS album_title,
    a.name AS author_name,
    COUNT(s.id) AS track_count,
    -- Сумма продолжительности в секундах
    SUM(s.duration) AS total_duration_seconds,
    -- Форматируем как MM:SS
    LPAD(FLOOR(SUM(s.duration) / 60), 2, '0') || ':' || LPAD(SUM(s.duration) % 60, 2, '0') AS total_duration_formatted
FROM albums
LEFT JOIN songs AS s ON s.album_id = albums.id
LEFT JOIN song_authors ON song_authors.song_id = s.id
LEFT JOIN authors AS a ON a.id = song_authors.author_id
GROUP BY albums.title, a.name
ORDER BY albums.title, a.name;
