import time
import machine

adc = machine.ADC(0)

while True:
     #set power to sensor
     #red 3 times and mittelwert
     time.sleep_ms(500)
     wet = adc.read()
     time.sleep_ms(500)     
     wet = wet + adc.read()
     time.sleep_ms(500)
     wet = wet + adc.read()
     print(wet / 3)
     #cut power of sensor
     #push to database
     time.sleep_ms(10000)


