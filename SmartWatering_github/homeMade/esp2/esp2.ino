/*******************************************************************
   A universal mqtt subscriber to automatically watering flowers
   GitHub: https://github.com/AndreyBritvin/SmartWatering
   By Andrey Britvin
*******************************************************************/
#include <ESP8266WiFi.h>
#include <SmartHome.h>
#include <PubSubClient.h>

char ssid[] = WIFI_SSID;     // your network SSID (name)
char password[] = WIFI_PASSWORD; // your network key

const char *mqtt_server = MQTT_SERVER; // Имя сервера MQTT
const int mqtt_port = MQTT_PORT; // Порт для подключения к серверу MQTT
const char *mqtt_user = MQTT_USER; // Логи от сервер
const char *mqtt_pass = MQTT_PASSWORD; // Пароль от сервера

WiFiClient wclientMQTT;
PubSubClient client(wclientMQTT, mqtt_server, mqtt_port);
MqttMessage test(&client);
int needMeasure = 0;
String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  //int maxIndex = data.length()-1;
  int maxIndex = data.length();

  for (int i = 0; i <= maxIndex && found <= index; i++) {

    if (data.charAt(i) == separator || i == maxIndex) {
      found++;
      strIndex[0] = strIndex[1] + 1;
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";

}
void callback(const MQTT::Publish& pub)
{
  //  Serial.println("lalal");
  String payload = pub.payload_string();
  String Topic = pub.topic();
  // Serial.print("topic=>"+Topic);
  // Serial.print(" ");
  // Serial.println("payload=>"+payload);
  if (Topic == "home/watering/doMeasurement" and needMeasure!=0)
  {
    Serial.println("readValue:NONE");//NONE means that it should be empty, but there must be ':'
  }
  else if(Topic == "home/watering/doMeasurement" and needMeasure == 0)
  {
      needMeasure = 1;
  }
  else {

    String room = getValue(Topic, '/', 2);
    String numFlower = getValue(Topic, '/', 4);
    String water_or_duration = getValue(Topic, '/', 5);
    if (payload == "on") {
      if (water_or_duration == "water")
      {
        Serial.println(room + ":" + numFlower);
      }
    }
    if (water_or_duration == "waterDuration")
    {
      // Serial.println(room + ":" + numFlower + ":" + String(payload));
      Serial.println(room + "_duration" + ":" + numFlower + ":" + String(payload));
    }
    
    else if (water_or_duration == "maxValue")
    {
      Serial.println(room + "_mC" + ":" + numFlower + ":" + String(payload)+":"+"max"+":"+"end");//moistureCallibration
    }
    else if(water_or_duration == "minValue")
    {
      Serial.println(room + "_mC" + ":" + numFlower + ":" + String(payload)+":"+"min"+":"+"end");//moistureCallibration
    }

  }
  delay(500);
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    WiFi.begin(ssid, password);

    if (WiFi.waitForConnectResult() != WL_CONNECTED)
      return;
  }

  if (WiFi.status() == WL_CONNECTED) {

    if (!client.connected()) {
      if (client.connect(MQTT::Connect(MQTT_CLIENT_ID).set_auth(mqtt_user, mqtt_pass))) {
        client.set_callback(callback);
        client.subscribe("home/watering/+/flower/+/water"); 
        client.subscribe("home/watering/+/flower/+/waterDuration"); 
        client.subscribe("home/watering/+/flower/+/minValue"); 
        client.subscribe("home/watering/+/flower/+/maxValue"); 
        client.subscribe("home/watering/doMeasurement");

      }
    }
    else {
      delay(500);
    }
    if (client.connected()) {
      char name_arr[700];
      size_t num_read = Serial.readBytesUntil('\n', name_arr, sizeof(name_arr) - 1 );
      name_arr[num_read] = '\0';

      if (String(name_arr) != "") {
        test.publishMessages(String(name_arr));
      }
      client.loop();
    }
  }
}
