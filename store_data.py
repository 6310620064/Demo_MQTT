import json
import sqlite3

# SQLite DB Name
DB_Name =  "data.db"


class DatabaseManager():
	def __init__(self):
		self.conn = sqlite3.connect(DB_Name)
		self.conn.execute('pragma foreign_keys = on')
		self.conn.commit()
		self.cur = self.conn.cursor()
		
	def add_del_update_db_record(self, sql_query, args=()):
		self.cur.execute(sql_query, args)
		self.conn.commit()
		return
	
	def get_temperature_data(self):
		self.cur.execute("SELECT * FROM Temperature_Data")
		data = self.cur.fetchall()
		temperature_data = []
		for row in data:
			temperature_data.append({
				'id': row[0],
				'sensor_name': row[1],
				'date_time': row[2],
				'Temperature': row[3]
			})
		return temperature_data

	def get_humidity_data(self):
		self.cur.execute("SELECT * FROM Humidity_Data")
		data = self.cur.fetchall()
		humidity_data = []
		for row in data:
			humidity_data.append({
				'id': row[0],
				'sensor_name': row[1],
				'date_time': row[2],
				'Humidity': row[3]
			})
		return humidity_data

	def __del__(self):
		self.cur.close()
		self.conn.close()

# Functions to push Sensor Data into Database

# Function to save Temperature to DB Table
def Temp_Data_Handler(jsonData):
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['sensor_name']
	Data_and_Time = json_Dict['Date']
	Temperature = json_Dict['Temperature']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("INSERT INTO Temperature_Data (sensor_name, date_time, Temperature) values (?,?,?)",[SensorID, Data_and_Time, Temperature])
	del dbObj
	print("Inserted Temperature Data into Database.")

# Function to save Humidity to DB Table
def Humidity_Data_Handler(jsonData):
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['sensor_name']
	Data_and_Time = json_Dict['Date']
	Humidity = json_Dict['Humidity']
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("INSERT INTO Humidity_Data (sensor_name, date_time, Humidity) values (?,?,?)",[SensorID, Data_and_Time, Humidity])
	del dbObj
	print("Inserted Humidity Data into Database.")


def sensor_Data_Handler(Topic, jsonData):
	if Topic == "Data/Temperature":
		Temp_Data_Handler(jsonData)
	elif Topic == "Data/Humidity":
		Humidity_Data_Handler(jsonData)	

