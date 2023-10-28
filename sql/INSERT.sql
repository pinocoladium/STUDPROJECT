INSERT INTO Genre(name) VALUES
('rock'),
('rock and roll'),
('pop music'),
('industrial rock'),
('jazz'),
('electonic music');

INSERT INTO Performer(name, pseudonym) VALUES
('David Callcott','Dave Gahan'),
('Till','Lindemann'),
('Elvis Aaron Presley','Elvis Presley'),
('Rudolph Heinrich Schenker','Rudolph'),
('Steven Victor Tallarico','Steven Tyler'),
('Francis Albert Sinatra','Frank sinatra'),
('Agnetha','Ose Fältskog'),
('Gordon Matthew Thomas Sumner','Sting'),
('James Douglas Morrison','Jim Morrison');

INSERT INTO Album(name_album, year) VALUES
('The Doors',1967),
('Brand New Day',1944),
('Waterloo',1974),
('Christmas Songs by Sinatra',1948),
('Get a Grip',2020),
('Lovedrive',1979),
('Elvis Presley',1956),
('Mutter',2020),
('Some Great Reward',2018);

INSERT INTO Track(name, duration, album) VALUES
('Mutter',269, 8),
('Ich will',217, 8),
('Master and servant',253, 9),
('Blasphemous rumours',382, 9),
('I m counting on you',145, 7),
('Holiday',576, 6),
('My lovedrive',288, 6),
('Gotta love it',358, 5),
('Crazy',317, 5),
('White christmas',204, 4),
('Sitting in the palmtree',219, 3),
('My honey, honey',177, 3),
('Desert rose',286, 2),
('Big lie small world',306, 2),
('The end',706, 1),
('My alabama song (whisky bar)',201, 1),
('Feuer frei!',189, 8),
('Eat the rich',251, 5);

INSERT INTO Compilation(name, year) VALUES
('Old school', 2017),
('New school', 2022),
('School of rock', 2019),
('For each', 2018),
('Originally from Germany', 2020),
('American classic', 1999),
('20th century', 2005),
('For sports', 2013),
('Under the groovy mood', 2009);

INSERT INTO Genre_performer(genre_id, performer_id) VALUES
(1, 2),
(1, 4),
(1, 5),
(1, 8),
(1, 9),
(2, 3),
(2, 9),
(3, 1),
(3, 7),
(4, 2),
(5, 6),
(6, 1),
(6, 7);

INSERT INTO Performer_album(performer_id, album_id) VALUES
(9, 1),
(8, 2),
(7, 3),
(6, 4),
(5, 5),
(4, 6),
(3, 7),
(2, 8),
(1, 9);

INSERT INTO Track_compilation(track_id, compilation_id) VALUES
(16, 1),
(16, 6),
(15, 3),
(15, 8),
(14, 7),
(13, 4),
(12, 5),
(11, 1),
(10, 9),
(9, 8),
(9, 2),
(8, 5),
(7, 3),
(6, 2),
(5, 9),
(4, 5),
(4, 1),
(3, 6),
(2, 7),
(2, 4),
(1, 6);