#include <Servo.h>

Servo myservo;

void setup() {
  // Начинаем работу с Serial портом на скорости 9600 бит/с
  Serial.begin(9600);
  myservo.attach(7);

  //получаем значение сервопривода в градусах
  int pos = myservo.read();
  Serial.println(pos);
  delay(300);
  

  for (int i = pos; i <= 100; i++) {   
    myservo.write(i);
    delay(150);
  }

}

void loop() {
  
  // myservo.write(100);

  // Проверяем, есть ли данные из Serial порта
  if (Serial.available() > 0) {
    // Читаем полученные данные и сохраняем их в переменной
    String receivedData = Serial.readString();

    for (int i = 100; i <= 170; i++) {   
      myservo.write(i);
      delay(15);
    }
    //delay(5000); 
    // Отправляем ответ обратно в Serial порт
    //Serial.println(receivedData);
    
    // for (int i = 170; i <= 100; i++) {   
    //   myservo.write(i);
    //   delay(15);
    // }
    myservo.detach();
    delay(1000);
  
    // int pos = myservo.read();
    // Serial.println(pos);
    //delay(1000);
  }
  // delay(10000);
}