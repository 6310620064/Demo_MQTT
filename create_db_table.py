import sqlite3

# Create DB Name For SQLite
DB_Name =  "data.db"

# SQLite DB Table Schema
TableSchema="""
drop table if exists Temperature_Data ;
create table Temperature_Data (
  id integer primary key autoincrement,
  sensor_name text,
  date_time text,
  Temperature text
);


drop table if exists Humidity_Data ;
create table Humidity_Data (
  id integer primary key autoincrement,
  sensor_name text,
  date_time text,
  Humidity text
);
"""

#Connect or Create DB File
conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

#Create Tables
sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

#Close DB
curs.close()
conn.close()
