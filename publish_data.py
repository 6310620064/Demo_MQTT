import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime

# Settings 
MQTT_Broker = "mqtt.eclipseprojects.io"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_Humidity = "Data/Humidity"
MQTT_Topic_Temperature = "Data/Temperature"


def on_connect(client, userdata,flags, rc):
	if rc != 0:
		pass
		print("Unable to connect to MQTT Broker")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		pass
		
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		

		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print ("Published: " + str(message) + " " + "Topic: " + str(topic))


# FAKE SENSOR RANDOM VALUES TO MQTT BROKER

toggle = 0

def publish_Fake_Sensor_Values_to_MQTT():
	threading.Timer(3.0, publish_Fake_Sensor_Values_to_MQTT).start()
	global toggle
	if toggle == 0:
		Humidity_Fake_Value = float("{0:.2f}".format(random.uniform(50, 100)))

		Humidity_Data = {}
		Humidity_Data['sensor_name'] = "SensorNo.1"
		Humidity_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S")
		Humidity_Data['Humidity'] = Humidity_Fake_Value
		humidity_json_data = json.dumps(Humidity_Data)

		print("Fake Humidity Value: " + str(Humidity_Fake_Value))
		publish_To_Topic (MQTT_Topic_Humidity, humidity_json_data)
		toggle = 1

	else:
		Temperature_Fake_Value = float("{0:.2f}".format(random.uniform(25, 40)))

		Temperature_Data = {}
		Temperature_Data['sensor_name'] = "SensorNo.2"
		Temperature_Data['Date'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S")
		Temperature_Data['Temperature'] = Temperature_Fake_Value
		temperature_json_data = json.dumps(Temperature_Data)

		print("Fake Temperature Value: " + str(Temperature_Fake_Value))
		publish_To_Topic (MQTT_Topic_Temperature, temperature_json_data)
		toggle = 0


publish_Fake_Sensor_Values_to_MQTT()

