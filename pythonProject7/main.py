import time
import serial.tools.list_ports
from paho.mqtt.subscribe import simple

#Связь с ардуино уно
arduino=serial.Serial('COM3',9600)

#Связь пайтона с управлением
message=simple('maker/#',hostname='95.163.230.191',port=1883,auth={'username':'maker','password':'LABmaker123'})

#Выводим возможное сообщение
print(message.payload.decode())

#Если пришло сообщение, отправляем сигнал к ардуино
if message.payload.decode() == '1':
    print("футболка 1")
    arduino.write(b'message.payload.encode()')
    time.sleep(1)

    # Считываем строку с Arduino
    data = arduino.readline().decode('utf-8').strip()
    # Выводим текущие показания
    print(data)
    print('футболка получена')

#Если пришло сообщение, отправляем сигнал к ардуино
if message.payload.decode() == '2':
    print("футболка 2")
    arduino.write(b'message.payload.encode()')
    time.sleep(1)

    # Считываем строку с Arduino
    data = arduino.readline().decode('utf-8').strip()
    # Выводим текущие показания
    print(data)
    print('футболка получена')



