# MQTT Mosquitto

## Подключаемся к публичному серверу
Подключаемся к публичному MQTT серверу и тестируем приём/отправку/снифинг

[test.mosquitto.org](https://test.mosquitto.org/)

Подключиться можно к конкретному топику, или используя фильтр.
Например "top/#" прослушивает все дочерние топики начиная с "top/"
На test.mosquitto.org можно подключиться неаутонтифицированному пользователю ко всем топикам на 20 секунд, затем разорвётся соединение.
(в секунду прилетает до нескольких тысяч сообщений)

Тут примеры от разрабов:
[Examples: https://github.com/eclipse-paho/paho.mqtt.python](https://github.com/eclipse-paho/paho.mqtt.python/tree/master/examples)


## Данные для подключения:
The server listens on the following ports:
1883 : MQTT, unencrypted, unauthenticated
1884 : MQTT, unencrypted, authenticated
8883 : MQTT, encrypted, unauthenticated
8884 : MQTT, encrypted, client certificate required
8885 : MQTT, encrypted, authenticated
8886 : MQTT, encrypted, unauthenticated
8887 : MQTT, encrypted, server certificate deliberately expired
8080 : MQTT over WebSockets, unencrypted, unauthenticated
8081 : MQTT over WebSockets, encrypted, unauthenticated
8090 : MQTT over WebSockets, unencrypted, authenticated
8091 : MQTT over WebSockets, encrypted, authenticated
The encrypted ports support TLS v1.3, v1.2 or v1.1 with x509 certificates and require client support to connect. For ports 8883 and 8884 you should use the certificate authority file (mosquitto.org.crt (PEM format), or mosquitto.org.der (DER format)) to verify the server connection. Ports 8081 and 8886 have a Lets Encrypt certificate, so you should use your system CA certificates or the appropriate Lets Encrypt CA certificate for verification.

Port 8884 requires clients to provide a certificate to authenticate their connection. You can generate your own certificate.

The configuration is available to view.

Authentication and topic access
Unauthenticated clients have access to publish all topics. Clients can also subscribe to all topics with the exception of the literal # topic.

Connecting with the username wildcard will allow a subscription to # to succeed for 20 seconds before being automatically removed. This allows discovery of topics of interest.

The authenticated listeners require a username / password:

rw / readwrite : read/write access to the # topic hierarchy
ro / readonly : read only access to the # topic hierarchy
wo / writeonly : write only access to the # topic hierarchy

***

[[text](https://pypi.org/project/paho-mqtt/)](https://pypi.org/project/paho-mqtt/)

pip install paho-mqtt

***
Документация библиотеки paho-mqtt
[https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html)

Eclipse Mosquitto using docker
https://hub.docker.com/_/eclipse-mosquitto
https://github.com/sukesh-ak/setup-mosquitto-with-docker
https://io-home.ru/home-assistant/docker-container/docker-chast-6-mosquitto-mqtt/
