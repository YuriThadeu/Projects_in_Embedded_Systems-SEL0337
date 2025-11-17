#include <Wire.h> 

const int potPin = A0; 
const int ledPin = LED_BUILTIN; 

void setup() {
  Serial.begin(9600); 
  Wire.begin(0x8); 

  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  
  pinMode(potPin, INPUT);
}

void receiveEvent(int howMany) {
  while (Wire.available()) { 
  char c = Wire.read(); 
    digitalWrite(ledPin, c); 
    
    Serial.print("Recebido via I2C: ");
    Serial.println(c);
  }
}

void requestEvent() {
  int potValue = analogRead(potPin); 
  Serial.println(potValue);
  
  Wire.write(highByte(potValue)); 
  Wire.write(lowByte(potValue)); 
}

void loop() { 
  delay(100); 
}