import json
import random
import time
import paho.mqtt.client as mqtt

# MQTT server information
mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_topic = "TelemetriaVB"

# Number of times to send data
num_messages = 5000000000

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code:", rc)

# Create an MQTT client instance
client = mqtt.Client()

# Set the on_connect callback
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(mqtt_broker, mqtt_port)

# Start the MQTT loop to handle communication
client.loop_start()

# Send random data num_messages times
vi = 0
ti = 900
ri = 0
for _ in range(num_messages):
    v = vi ** (1/2)
    vi += 50
    t = ti ** (1/2)
    ti += 120
    r = ri ** (1/2)
    ri += 100000
    data = {
        "coleta": "RG23",
        "velocidade": v,
        "rpm": r,
        "temperatura": t,
        "acelerometroX": round(random.uniform(-1, 1), 2),
        "acelerometroY": round(random.uniform(-1, 1), 2),
        "acelerometroZ": round(random.uniform(-1, 1), 2),
    }

    json_data = json.dumps(data)
    client.publish(mqtt_topic, json_data)
    print("Sent:", json_data)

    time.sleep(0.5)  # Delay between messages

# Disconnect and stop the MQTT loop
client.disconnect()
client.loop_stop()
print("Finished sending messages.")