import paho.mqtt.client as mqtt
import time
from datetime import datetime
from mqtt_config import broker, topic

# Create a new MQTT client instance with a client name
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="PublisherClient")

# Connect to the broker
client.connect(broker)

try:
    while True:
        # Get the current time without date
        message = datetime.now().strftime("%H:%M:%S")
        
        # Publish a message to the topic
        client.publish(topic, message)
        
        print(f"Published message '{message}' to topic '{topic}'")
        
        # Wait for 2 seconds before sending the next message
        time.sleep(2)
except KeyboardInterrupt:
    print("Publishing stopped by user")

# Disconnect from the broker
client.disconnect()
