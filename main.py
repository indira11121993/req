CREATE TABLE IF NOT EXISTS Singer (
		singer_id SERIAL PRIMARY KEY,
		singer_name VARCHAR(35) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre (
		genre_id SERIAL PRIMARY KEY,
		genre_name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre_Singer (
		genre_id SERIAL REFERENCES Genre (genre_id),
		singer_id SERIAL REFERENCES Singer(singer_id)
);

CREATE 	TABLE IF NOT EXISTS Album (
		album_id SERIAL PRIMARY KEY,
		album_name VARCHAR(40) NOT NULL,
		release_album DATE
);

CREATE TABLE IF NOT EXISTS Album_Singer (
		album_id SERIAL REFERENCES Album (album_id),
		singer_id SERIAL REFERENCES Singer(singer_id)
);

CREATE TABLE IF NOT EXISTS Track (
		track_id SERIAL PRIMARY KEY,
		track_name VARCHAR(30) NOT NULL,
		duration TIME NOT NULL,
		album_id SERIAL REFERENCES Album (album_id)
);

CREATE TABLE IF NOT EXISTS Collection (
		collection_id SERIAL PRIMARY KEY,
		collection_name VARCHAR(35) NOT NULL,
		release_collection DATE,
		track_id SERIAL REFERENCES Track (track_id)
);
