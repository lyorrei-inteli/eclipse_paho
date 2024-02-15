from sensor_simulator import SolarRadiationSensorSimulator
import paho.mqtt.client as mqtt
import time 

# Configurações do MQTT
broker_address = "localhost"
port = 1891  # Porta padrão do MQTT
topic = "solar_sensor"

# Inicialização do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")
client.connect(broker_address, port, 60)

solar_sensor = SolarRadiationSensorSimulator(topic)

try:
    while True:
        solar_sensor.publish_data(client)
        time.sleep(2)  # Esperar 2 segundos antes da próxima publicação
except KeyboardInterrupt:
    print("Publicação encerrada")
    client.disconnect()
