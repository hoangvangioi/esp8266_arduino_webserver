#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <Ethernet.h>
#include <SimplePgSQL.h>
#include <DHT.h>
#include<SoftwareSerial.h> //Included SoftwareSerial Library


#define D5 14
#define D6 12

#define D3 0
#define D4 2

//Started SoftwareSerial at RX and TX pin of ESP8266/NodeMCU
SoftwareSerial waterSerial(D6, D5); // (Rx, Tx)

SoftwareSerial soundSerial(D4, D3); // (Rx, Tx)


// Uncomment one of the lines below for whatever DHT sensor type you're using!
#define DHTTYPE DHT11   // DHT 11

// DHT Sensor
#define DHTPIN 4 // GPIO4

// Initialize DHT sensor.
DHT dht(DHTPIN, DHTTYPE);

// env variable
float temperature = 0.0;
float humidity = 0.0;


IPAddress PGIP(192,168,0,1);        // your PostgreSQL server IP

const char ssid[] = "YOUR_NETWORK_SSID";      //  your network SSID (name)
const char pass[] = "YOUR_NETWORK_PASSWORD";      // your network password

const char user[] = "YOUR_DATABASE_USER";       // your database user
const char password[] = "YOUR_DATABASE_PASSWORD";   // your database password
const char dbname[] = "YOUR_DATABASE_NAME";         // your database name

static PROGMEM const char query_sound[] = "SET TIMEZONE = 'Asia/Ho_Chi_Minh'; INSERT INTO api_sound (time, intensity) VALUES(current_timestamp, %s);";

static PROGMEM const char query_watersensor[] = "SET TIMEZONE = 'Asia/Ho_Chi_Minh'; INSERT INTO api_watersensor (time, water_level) VALUES(current_timestamp, %s);";

static PROGMEM const char query_light[] = "SET TIMEZONE = 'Asia/Ho_Chi_Minh'; INSERT INTO api_light (time, intensity) VALUES(current_timestamp, %s);";

static PROGMEM const char query_dht[] = "SET TIMEZONE = 'Asia/Ho_Chi_Minh'; INSERT INTO api_dht11 (time, temperature, humidity) VALUES(current_timestamp, %s, %s);";


int WiFiStatus;
WiFiClient client;

char buffer[1024];
PGconnection conn(&client, 0, 1024, buffer);


void checkConnection() {
    int status = WiFi.status();
    if (status != WL_CONNECTED) {
        if (WiFiStatus == WL_CONNECTED) {
            Serial.println("Connection lost");
            WiFiStatus = status;
        }
    }
    else {
        if (WiFiStatus != WL_CONNECTED) {
            Serial.println("Connected");
            WiFiStatus = status;
        }
    }
}

int pg_status = 0;

void doPg(void) {
    char *msg;
    int rc;
    if (!pg_status) {
        conn.setDbLogin(PGIP, user, password, dbname, "utf8");
        pg_status = 1;
        return;
    }

    if (pg_status == 1) {
        rc = conn.status();
        if (rc == CONNECTION_BAD || rc == CONNECTION_NEEDED) {
            char *c=conn.getMessage();
            if (c) Serial.println(c);
            pg_status = -1;
        }
        else if (rc == CONNECTION_OK) {
            pg_status = 2;
        }
        return;
    }
    if (pg_status == 2) {

        String soundSensorValue = String(soundSerial.read());
        Serial.print("Sound Sensor Value: "); 
        Serial.println(soundSensorValue);

        String waterSensorValue = String(waterSerial.read());
        Serial.print("Water Level Sensor Value: ");
        Serial.println(waterSensorValue);

        // Đọc giá trị độ sáng từ cảm biến LDR
        String ldrValue = String(analogRead(A0));
        Serial.print("LDR Value: "); 
        Serial.println(ldrValue);

        temperature = dht.readTemperature();	// Gets the values of the temperature
        humidity = dht.readHumidity();	// Gets the values of the humidity 
        String newTemperature = String(temperature);
        String newHumidity = String(humidity);
        Serial.print("Temperature: "); 
        Serial.println(temperature);
        Serial.print("Humidity: "); 
        Serial.println(humidity);

        if (conn.executeFormat(true, query_sound, soundSensorValue)) goto error;
        if (conn.executeFormat(true, query_watersensor, waterSensorValue)) goto error;
        if (conn.executeFormat(true, query_light, ldrValue)) goto error;
        if ((newTemperature != "nan") && (newHumidity != "nan")) {
            if (conn.executeFormat(true, query_dht, newTemperature, newHumidity)) goto error;
        }

        Serial.println("Working...");
    }
    return;
    error:
        msg = conn.getMessage();
        if (msg) Serial.println(msg);
        else Serial.println("UNKNOWN ERROR");
        if (conn.status() == CONNECTION_BAD) {
            Serial.println("Connection is bad");
            pg_status = -1;
        }
}

void setup(void) {
    // Serial mySerial Begin at 115200 Baud
	waterSerial.begin(115200);
	soundSerial.begin(115200);
    Serial.begin(115200);
    
    WiFi.begin((char *)ssid, pass);
    dht.begin();
}

void loop() {
    Serial.println("- - - - - - - - - - - - - - - - - - - -");

    checkConnection();
    if (WiFiStatus == WL_CONNECTED) {
        doPg();
    }

    delay(5000);
}