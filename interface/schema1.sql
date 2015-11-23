DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS rower;
DROP TABLE IF EXISTS league;

CREATE TABLE user (
	id INTEGER PRIMARY KEY,
	username TEXT,
	hash INTEGER,
	team TEXT,
	league INTEGER
);

CREATE TABLE rower (
	id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	club TEXT,
	age INTEGER,
	height REAL,
	weight REAL
);


CREATE TABLE league (
	id INTEGER PRIMARY KEY,
	name TEXT,
	users TEXT
);


INSERT INTO user values(0, "user", 1118194314, "1;2", 0);
INSERT INTO user values(1, "phil", -1937116876, "0;3", 0);
INSERT INTO rower values(0, "Aaron", "Marcovy", "Case", 30, 76, 220);
INSERT INTO rower values(1, "Eric", "Murray", "NZ", 29, 74, 200);
INSERT INTO rower values(2, "Hamish", "Bond", "NZ", 33, 77, 210);
INSERT INTO rower values(3, "Philip", "Smith", "Case", 19, 75.5, 180);
INSERT INTO league Values(0, "Goon Squad", "0;1");