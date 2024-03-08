#include <MQ135.h>
#include "dht.h" 

#define PDHT11 A2

dht DHT;
float humi;
float temp;

int quali;
MQ135 gasSensor = MQ135(A0); 

void setup() {
  Serial.begin(9600);
}

void loop() {
  quali = analogRead(0);
  DHT.read11(PDHT11);
  temp = DHT.temperature;
  humi = DHT.humidity;
  Serial.println(String(quali) + "," + String(temp) + "," + String(humi));
  delay(1800000); //30: 1800000 | 5: 300000
}
