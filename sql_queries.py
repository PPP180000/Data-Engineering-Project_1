# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id varchar PRIMARY KEY, start_time varchar NOT NULL,user_id varchar NOT NULL, level varchar NOT NULL, song_id varchar NOT NULL, artist_id varchar NOT NULL, session_id varchar NOT NULL, location varchar NOT NULL, user_agent varchar NOT NULL);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id varchar PRIMARY KEY, first_name varchar NOT NULL,last_name varchar NOT NULL, gender varchar NOT NULL, level varchar NOT NULL);
""")


song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar PRIMARY KEY, title varchar NOT NULL, artist_id varchar NOT NULL, year int NOT NULL, duration numeric NOT NULL);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar PRIMARY KEY, artist_name varchar NOT NULL, artist_location varchar NOT NULL, artist_latitude numeric NOT NULL, artist_longitude numeric NOT NULL);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time time PRIMARY KEY, hour int NOT NULL,day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday varchar NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT 
	ON CONSTRAINT songplays UPDATE songplays SET 
	songplay_id = EXCLUDED.songplay_id, start_time = EXCLUDED.start_time, user_id = EXCLUDED.user_id,
	level = EXCLUDED.level, song_id = EXCLUDED.song_id, artist_id = EXCLUDED.artist_id,
	session_id = EXCLUDED.session_id, location = EXCLUDED.location, user_agent = EXCLUDED.user_agent;
""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT users UPDATE users SET 
	user_id = EXCLUDED.user_id, level = EXCLUDED.level, first_name = EXCLUDED.first_name,
	last_name = EXCLUDED.last_name, gender = EXCLUDED.gender; 
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT songs UPDATE songs SET 
	song_id = EXCLUDED.song_id, title = EXCLUDED.title, artist_id = EXCLUDED.artist_id, year = EXCLUDED.year, duration = EXCLUDED.duration;
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, artist_name, artist_location, artist_latitude , artist_longitude) VALUES(%s, %s, %s, %s, %s) ON CONFLICT (artist_id, artist_name, artist_location, artist_latitude , artist_longitude) DO NOTHING;
""")

time_table_insert = ("""INSERT INTO time(start_time , hour ,day , week, month , year , weekday ) VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time , hour ,day , week, month , year , weekday) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT artists.artist_id, songs.song_id FROM songs 
JOIN artists ON songs.artist_id=artists.artist_id 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]