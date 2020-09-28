#!/usr/bin/env python3
# read a TMP101 sensor

import smbus, time, Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(2)
address = 0x48
address2 = 0x4a

tmpAlert1 = "P9_14"
tmpAlert2 = "P9_12"

GPIO.setup("P9_12", GPIO.IN)
GPIO.setup("P9_14", GPIO.IN)

GPIO.add_event_detect(tmpAlert2, GPIO.RISING)
GPIO.add_event_detect(tmpAlert1, GPIO.RISING)

bus.write_byte_data(address, 1, 0b10000100)
bus.write_byte_data(address2, 1, 0b10000100)

bus.write_byte_data(address, 3, 0b00011101)
bus.write_byte_data(address2, 3, 0b00011101)

bus.write_byte_data(address, 2, 0b00011011)
bus.write_byte_data(address2, 2, 0b00011011)

bus.write_byte_data(address, 2, 0b00011101)
bus.write_byte_data(address2, 2, 0b00011101)

print('waiting for interrupt now')
while True:
    time.sleep(0.25)
    if GPIO.event_detected(tmpAlert1):
        temp = bus.read_byte_data(address, 0) * 1.8 + 32
        print('1st temp sensor: ' + str(temp))
    if GPIO.event_detected(tmpAlert2):
        #do something else
        temp2 = bus.read_byte_data(address2, 0) * 1.8 + 32
        print('2nd temp sensor: ' + str(temp2))
