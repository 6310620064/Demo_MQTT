import paho.mqtt.client as mqtt
from store_data import sensor_Data_Handler

# Settings 
MQTT_Broker = "mqtt.eclipseprojects.io"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Data/#"

#Subscribe to all Sensors at Base Topic
def on_connect(client, userdata, flags, rc):
    mqttc.subscribe(MQTT_Topic, 0)

#Save Data into DB Table
def on_message(mosq, obj, msg):
	print ("MQTT Data Received")
	print ("Topic: " + msg.topic)
	print("Data: " + msg.payload.decode('utf-8'))
	sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()
