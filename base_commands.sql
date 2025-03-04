-- SELECT *
--   FROM demo
--   	WHERE name = 'Kirill N.";
-- SELECT name FROM demo;
-- page = 2
-- limit = 5
-- offset = page * limitdemo
-- SELECT * FROM demo LIMIT 10, 5;

-- SELECT * FROM demo ORDER BY name, id ASC;

-- SELECT * FROM demo ORDER BY name ASC LIMIT 5, 5;
-- SELECT * FROM demo WHERE id > 11;
-- SELECT * FROM demo WHERE id <> 1;
-- SELECT * FROM demo WHERE id < 3;
-- SELECT * FROM demo WHERE id <= 3;
SELECT name FROM demo WHERE id <= 3;