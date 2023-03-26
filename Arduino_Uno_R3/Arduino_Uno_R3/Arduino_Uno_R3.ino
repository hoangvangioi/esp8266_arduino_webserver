#include<SoftwareSerial.h> //Included SoftwareSerial Library

// Started SoftwareSerial at RX and TX pin of ESP8266/NodeMCU
SoftwareSerial waterSerial(5, 6); // (Rx, Tx)

SoftwareSerial soundSerial(0, 1); // (Rx, Tx)

void setup() {
	//Serial mySerial Begin at 115200 Baud
	waterSerial.begin(115200);
	soundSerial.begin(115200);
}

void loop() {
	int waterSensorValue = analogRead(A2);

  	int soundSensorValue = analogRead(A0);

	if (waterSerial.available() > 0) {
		// Water Level Sensor
		waterSerial.write(waterSensorValue);
		Serial.println(waterSensorValue);
	}

	if (soundSerial.available() > 0) {
		// print out the value you read:
		soundSerial.write(soundSensorValue);
		Serial.println(soundSensorValue);
	}
}