#this
#include <ESP32Servo.h>

Servo myServo;

const int servoPin = 18;

void setup() {
  Serial.begin(9600);

  myServo.setPeriodHertz(50);
  myServo.attach(servoPin, 500, 2400);

  myServo.write(90);
  Serial.println("ESP32 Servo Ready");
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    int angle = command.toInt();

    if (angle >= 0 && angle <= 180) {
      myServo.write(angle);
      Serial.println(angle);
    }
  }
}
