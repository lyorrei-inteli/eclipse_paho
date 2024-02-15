import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")

def on_connect(client, userdata, flags, rc, _):
    print("Conectado com o código de retorno: ", rc)
    client.subscribe("solar_sensor")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1891, 60)

client.loop_forever()
