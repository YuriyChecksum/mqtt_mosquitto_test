import time
import paho.mqtt.client as mqtt
from mqtt_config import broker, topic
import logging

topic = "#"
# topic = "10974/#"


logging.basicConfig(
    datefmt='%H:%M:%S',
    # format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s: %(message)s',
    format='%(message)s',
)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.info("Starting listener on topic %s", topic)


# Create a new MQTT client instance with a client name
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="SubscriberClient")
mqttc.enable_logger()

resive_unic_topics = set()

@mqttc.connect_callback()
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code} {flags=}")
    if flags.session_present:
        pass

@mqttc.disconnect_callback()
def on_disconnect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        log.info("%s", reason_code) # success disconnect
    if reason_code > 0:
        log.info("%s", reason_code) # success disconnect

@mqttc.message_callback()
def on_message(client, userdata, message):
    resive_unic_topics.add(message.topic)
    try:
        log.info("topic: '%s' Message: '%s'", message.topic, message.payload.decode())
        # print("topic: '{}' Message: {}".format(message.topic, message.payload.decode()))
    except Exception as e:
        log.error("Error processing message: %s", e)

# постаринке, но лучше декоратором
# client.on_message = on_message

# Connect to the broker
mqttc.connect(broker, port=1883, keepalive=60)

# Subscribe to the topic
mqttc.subscribe(topic)

# Start the MQTT client loop to process messages
mqttc.loop_start()
# mqttc.loop_forever()

time.sleep(1)
# Keep the script running
# input("Press Enter to exit...\n")

# Stop the MQTT client loop and disconnect
mqttc.loop_stop()
mqttc.disconnect()

sorted_topics = sorted(resive_unic_topics)
print("Received topics:")
for t in sorted_topics:
    print(t)

print("Total topics:", len(sorted_topics))
