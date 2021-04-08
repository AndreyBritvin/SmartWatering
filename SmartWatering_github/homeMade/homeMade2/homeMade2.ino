String topic1 = "home";
String room = "andrey";

String from_MQTT = "";

//for mode 0 watering
int time_relay1 = 10000;//millis
int time_relay2 = 10000;
int time_relay3 = 10000;
int time_relay4 = 10000;
int time_relay5 = 10000;
int time_relay6 = 10000;

// set all moisture sensors PIN ID
int moisture1 = A5;
int moisture2 = A4;
int moisture3 = A3;
int moisture4 = A2;
int moisture5 = A1;
int moisture6 = A0;

// declare moisture values
int moisture1_value = 0 ;
int moisture2_value = 0;
int moisture3_value = 0;
int moisture4_value = 0;
int moisture5_value = 0;
int moisture6_value = 0;

// set water relays
int relay1 = 12;
int relay2 = 8;
int relay3 = 9;
int relay4 = 10;
int relay5 = 5;
int relay6 = 13;
long relay_delay[6][2] = {{relay1, time_relay1}, {relay2, time_relay2}, {relay3, time_relay3}, {relay4, time_relay4},{relay5, time_relay5},{relay6, time_relay6}};

/*int min1 = 597,min2 = 597,min3 = 597,min4 = 597,min5 = 597,min6 = 597;
int max1 = 255, max2 = 255, max3 = 255,max4 = 255,max5 = 255,max6 = 255;

int mC[6][2] = {{min1, max1}, {min2, max2}, {min3, max3}, {min4, max4}, {min5, max5}, {min6, max6}}; //moistureCalibration
*/
int mC[6][2] = {{597, 255}, {597, 255}, {597, 255}, {597, 255}, {597, 255}, {597, 255}}; //moistureCalibration
void setup()
{
  Serial1.begin(9600);
  for(int i = 0; i<6; i++)
  {
    pinMode(relay_delay[i][0], OUTPUT);
  }
  
}

void loop()
{
  char from_MQTT[1000];
  size_t num_read = Serial1.readBytesUntil('\n', from_MQTT, sizeof(from_MQTT) - 1 );
  from_MQTT[num_read] = '\0';
  if (String(from_MQTT) != "")
  { 
    change_value(String(from_MQTT));
  }
}

void change_value(String str)
{
  String constant = getValue(str, ':', 0);
  String value = getValue(str, ':', 1);
  if (constant == "readValue")
  {
    read_value();
  }
  else if (constant == room)
  {
    int relay_num = value.toInt() - 1;
    digitalWrite(relay_delay[relay_num][0], HIGH);
    delay(relay_delay[relay_num][1]);
    digitalWrite(relay_delay[relay_num][0], LOW);
    Serial1.println(topic1+"/watering/"+room+"/flower/"+String(value.toInt())+"/water:off|");

  }
  else if (constant == room + "_duration")
  {
    int relay_num = value.toInt() - 1;
    relay_delay[relay_num][1] = getValue(str, ':', 2).toInt() * 1000;
  }
  else if (constant == room+"_mC")//moistureCallibration
  {
    int numFlower = value.toInt()-1;
    int num = getValue(str, ':', 2).toInt();

    //Serial1.println("test:"+String(numFlower)+","+String(num)+","+String(getValue(str, ':', 3))+"|");
    
    if(String(getValue(str, ':', 3)) == "min")
    {
      mC[numFlower][0] = num;
      //Serial1.println("test1:insdeMin|");
    }
    else if(String(getValue(str, ':', 3)) == "max")
    {
      mC[numFlower][1] = num;
      //Serial1.println("test2:insdeMax|");
      
    }
    
  }
  delay(100);
}

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
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


//Set moisture value
void read_value()
{
  int value1 = analogRead(moisture1);// Serial.println("Value1 = " + String(value1));
  moisture1_value = map(value1, mC[0][0], mC[0][1], 0, 100); delay(20);
  if (moisture1_value < 0) {
    moisture1_value = 0;
  }
  int value2 = analogRead(moisture2);// Serial.println("Value2 = " + String(value2));
  moisture2_value = map(value2, mC[1][0], mC[1][1], 0, 100); delay(20);
  if (moisture2_value < 0) {
    moisture2_value = 0;
  }
  int value3 = analogRead(moisture3);// Serial.println("Value3 = " + String(value3));
  moisture3_value = map(value3, mC[2][0], mC[2][1], 0, 100); delay(20);
  if (moisture3_value < 0) {
    moisture3_value = 0;
  }
  int value4 = analogRead(moisture4); //Serial.println("Value4 = " + String(value4));
  moisture4_value = map(value4, mC[3][0], mC[3][1], 0, 100); delay(20);
  if (moisture4_value < 0) {
    moisture4_value = 0;
  }
  int value5 = analogRead(moisture5); //Serial.println("Value4 = " + String(value4));
  moisture5_value = map(value5, mC[4][0], mC[4][1], 0, 100); delay(20);
  if (moisture5_value < 0) {
    moisture5_value = 0;
  }
  int value6 = analogRead(moisture6); //Serial.println("Value4 = " + String(value4));
  moisture6_value = map(value6, mC[5][0], mC[5][1], 0, 100); delay(20);
  if (moisture6_value < 0) {
    moisture6_value = 0;
  }
  String hum = "";
  String hum2 = "";
  //delay(500);
  int timeDel = 500;
  hum += topic1+"/watering/"+room+"/flower/1/humidity:" + String(moisture1_value) + "|";
  Serial1.println(hum);
  Serial1.flush();
  hum="";
  delay(timeDel);
  hum += topic1+"/watering/"+room+"/flower/2/humidity:" + String(moisture2_value) + "|";
 Serial1.println(hum);
  Serial1.flush();
  hum="";
  delay(timeDel);
  hum += topic1+"/watering/"+room+"/flower/3/humidity:" + String(moisture3_value) + "|";
 Serial1.println(hum);
  Serial1.flush();
  hum="";
  delay(timeDel);
  
  hum += topic1+"/watering/"+room+"/flower/4/humidity:" + String(moisture4_value) + "|";
  Serial1.println(hum);

  Serial1.flush();
  hum="";
  delay(timeDel);
  hum += topic1+"/watering/"+room+"/flower/5/humidity:" + String(moisture5_value) + "|";
  Serial1.println(hum);

  Serial1.flush();
  hum="";
  delay(timeDel);
  hum += topic1+"/watering/"+room+"/flower/6/humidity:" + String(moisture6_value);
Serial1.println(hum);

  Serial1.flush();
  hum="";
  delay(timeDel);

  
  hum2 += topic1+"/watering/"+room+"/flower/1/humidityRaw:" + String(value1) + "|";
  Serial1.println(hum2);
  Serial1.flush();
  hum2="";
  delay(timeDel);
  hum2 += topic1+"/watering/"+room+"/flower/2/humidityRaw:" + String(value2) + "|";
  Serial1.println(hum2);
  Serial1.flush();
  hum2="";
  delay(timeDel);
  hum2 += topic1+"/watering/"+room+"/flower/3/humidityRaw:" + String(value3) + "|";
  Serial1.println(hum2);
  Serial1.flush();
  hum2="";
  delay(timeDel);
  
  hum2 += topic1+"/watering/"+room+"/flower/4/humidityRaw:" + String(value4) + "|";
  Serial1.println(hum2);
  Serial1.flush();
  hum2="";
  delay(timeDel);
  hum2 += topic1+"/watering/"+room+"/flower/5/humidityRaw:" + String(value5) + "|";
  Serial1.println(hum2);
  Serial1.flush();
  hum2="";
  delay(timeDel);
  hum2 += topic1+"/watering/"+room+"/flower/6/humidityRaw:" + String(value6)+"|";
  Serial1.println(hum2);
  Serial1.flush();
  hum2="";
  delay(timeDel);
  /*
hum = "test:";
  hum += topic1+"/watering/"+room+"/flower/1/humidity-" + String(moisture1_value) + "0";
  hum += topic1+"/watering/"+room+"/flower/2/humidity-" + String(moisture2_value) + "0";
  hum += topic1+"/watering/"+room+"/flower/3/humidity-" + String(moisture3_value) + "0";
  hum += topic1+"/watering/"+room+"/flower/4/humidity-" + String(moisture4_value) + "0";
  hum += topic1+"/watering/"+room+"/flower/5/humidity-" + String(moisture5_value) + "0";
  hum += topic1+"/watering/"+room+"/flower/6/humidity-" + String(moisture6_value) + "0";

  hum2 += topic1+"/watering/"+room+"/flower/1/humidityRaw-" + String(value1) + "0";
  hum2 += topic1+"/watering/"+room+"/flower/2/humidityRaw-" + String(value2) + "0";
  hum += topic1+"/watering/"+room+"/flower/3/humidityRaw-" + String(value3) + "0";
  hum += topic1+"/watering/"+room+"/flower/4/humidityRaw-" + String(value4) + "0";
  hum += topic1+"/watering/"+room+"/flower/5/humidityRaw-" + String(value5) + "0";
  hum += topic1+"/watering/"+room+"/flower/6/humidityRaw-" + String(value6)+"|";
  */
  //Serial1.println("test:"+String(hum.length()));
  //Serial1.println(hum);
  //Serial1.flush();
  //delay(100);
  //Serial1.println(hum2);
  //Serial1.flush();
  //delay(500);
}
