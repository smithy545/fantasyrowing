CREATE TABLE user (
	id INTEGER PRIMARY KEY,
	username TEXT,
	hash INTEGER,
	teamid INTEGER,
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

CREATE TABLE team (
	id INTEGER PRIMARY KEY,
	rowers TEXT,
	size INTEGER
);

CREATE TABLE league (
	id INTEGER PRIMARY KEY,
	name TEXT,
	users TEXT,
	taken_rowers TEXT
);