SELECT name_album, year FROM Album
WHERE year = 2018;

SELECT name, duration*1.0 / 60 FROM Track
WHERE duration =(SELECT MAX(duration) FROM Track);

SELECT name FROM Track
WHERE duration >= 210;

SELECT name FROM Compilation
WHERE year BETWEEN 2018 AND 2020;

SELECT name FROM Performer
WHERE NOT LIKE '% %'

SELECT name FROM Track
WHERE LOWER(name) LIKE '%my%';

____________________________________________________________________________

SELECT name, COUNT(performer_id) FROM genre_performer gp
JOIN genre g ON gp.genre_id = g.genre_id
GROUP BY g.name
ORDER BY count DESC;

SELECT name, year, COUNT(track_id) FROM Track_compilation tc 
JOIN compilation c ON tc.compilation_id = c.compilation_id
WHERE year BETWEEN 2019 AND 2020
GROUP BY c.year, c.name;

SELECT name_album , AVG(duration*1.0 / 60) FROM Album a
JOIN Track t ON a.album_id = t.album
GROUP BY a.name_album
ORDER BY AVG DESC;

SELECT name FROM Performer p
JOIN Performer_album pa ON p.performer_id = pa.performer_id
JOIN Album a ON a.album_id = pa.album_id
WHERE p.name NOT IN (
		SELECT DISTINCT p.name FROM Performer p 
		LEFT JOIN Performer_album pa ON p.performer_id = pa.performer_id
        JOIN Album a ON a.album_id = pa.album_id 
		WHERE a.year = 2020
		)
ORDER BY p.name;

SELECT c.name FROM Compilation c
JOIN Track_compilation tc ON c.compilation_id = tc.compilation_id
JOIN  Track t ON tc.track_id = t.track_id
JOIN Album a ON t.album = a.album_id  
JOIN Performer_album pa ON a.album_id = pa.album_id
JOIN Performer p ON pa.performer_id = p.performer_id
WHERE pseudonym = 'Lindemann';

SELECT name_album FROM Album a
JOIN Performer_album pa ON a.album_id = pa.album_id
JOIN Performer p ON pa.performer_id = p.performer_id
JOIN Genre_performer gp ON p.performer_id = gp.performer_id
GROUP BY gp.performer_id, name_album 
HAVING count(*) > 1;

SELECT t.name FROM Track t
FULL JOIN Track_compilation tc ON t.track_id = tc.track_id
GROUP BY t.name
HAVING count(tc.compilation_id) < 1;

SELECT p.name FROM Performer p
JOIN Performer_album pa ON p.performer_id = pa.performer_id
JOIN Album a ON pa.album_id = a.album_id
JOIN Track t ON a.album_id = t.album
WHERE duration = (SELECT MIN(duration) FROM Track);

SELECT name_album FROM Album a
JOIN Track t ON a.album_id = t.album
GROUP BY name_album
HAVING count(t.album) < 1;

SELECT name_album FROM Album a
JOIN Track t ON a.album_id = t.album
GROUP BY name_album
HAVING count(t.album) = (
    SELECT count(t.album) FROM Album a
    JOIN Track t ON a.album_id = t.album
    GROUP BY name_album
    order by count(t.album)
    LIMIT 1
);