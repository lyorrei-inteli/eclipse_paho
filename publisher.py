import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "python_publisher")

client.connect("localhost", 1891, 60)

try:
    while True:
        message = str(random.randint(0, 1280)) + " W/m2"
        client.publish("solar_sensor", message)
        print(f"Publicado: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")

client.disconnect()