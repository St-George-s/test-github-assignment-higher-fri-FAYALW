# SELECT Statement
# Name: SELECT
# What it does: It retrieves data from one or more columns in a database table.
# How to use it: 
# SELECT column_name 
# FROM table_name;

# Example: 
# SELECT artist_name 
# FROM Artists;

# Spotify Use: Retrieves the names of all artists in the Artists table.

# SELECT * Statement
# Name: SELECT *
# What it does: Selects all columns from a database table.
# How to use it: 
# SELECT * 
# FROM table_name;

# Example: 
# SELECT * FROM Albums;

# Spotify Use: Retrieves all information about all albums in the Albums table.

# WHERE Clause
# Name: WHERE
# What it does: Filters the results set to include only rows that meet certain criteria.
# How to use it: 
# SELECT column_name 
# FROM table_name 
# WHERE condition;

# Example: 
# SELECT * 
# FROM Tracks 
# WHERE duration_ms > 200000;

# Spotify Use: Retrieves all tracks from the Tracks table that are longer than 200,000 milliseconds (or 200 seconds).

# Modifying Queries
# What it does: Adjusting SELECT statements to retrieve different data sets.
# How to use it: Change the column_name or conditions in the SELECT or WHERE clause.
# Example: 

# Different Columns: 
# SELECT artist_id, artist_name 
# FROM Artists;

# Different Years in Albums: 
# SELECT * FROM Albums 
# WHERE release_year = 2017;

# Different Conditions in Tracks: 
# SELECT * FROM Tracks 
# WHERE duration_ms < 180000;