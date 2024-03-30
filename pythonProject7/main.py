import time
import serial.tools.list_ports
from paho.mqtt.subscribe import simple

arduino=serial.Serial('COM3',9600)

message=simple('maker/#',hostname='95.163.230.191',port=1883,auth={'username':'maker','password':'LABmaker123'})

print(message.payload.decode())

# while True:
if message.payload.decode() == '1':
    print("!!!!")
    arduino.write(b'message.payload.encode()')
    time.sleep(1)

    # Считываем строку с Arduino
    data = arduino.readline().decode('utf-8').strip()
    # Выводим текущие показания
    print(data)
# line = arduino.readline().decode()
# print(line)
    print('футболка получена')

    # elif message.payload.decode() == '2':
    #     print('розовая футболка')
    # else:
    #     print('нет нужной футболки')



