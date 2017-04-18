import time
import machine
import network
import urequests
import ubinascii


CONST_WIFISSID = "Freifunk"
CONST_WIFIPW = ""
CONST_APITOKEN = ""
CONST_SERVERURI = "http://philhil.de/openWaterer/index.php"

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(CONST_WIFISSID, CONST_WIFIPW)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def send_data(sensor_data):
    wlan = network.WLAN(network.STA_IF)
    mac =  str(ubinascii.hexlify(wlan.config('mac')), 'ascii')
    params = '?token=9FyuFQ5Puil9qhF&device_id='+mac+'&name=humidity&data='+str(sensor_data)
    resp = urequests.get(CONST_SERVERURI + params)
    print(resp.json())


adc = machine.ADC(0)

time.sleep_ms(10000)
do_connect()

while True:

#read sensor data
    #set power to sensor
    #red 3 times and mittelwert
    time.sleep_ms(500)
    wet = adc.read()
    time.sleep_ms(500)
    wet = wet + adc.read()
    time.sleep_ms(500)
    wet = wet + adc.read()
    print(wet / 3)
    send_data(wet/3)
    #cut power of sensor


#push to database


    time.sleep_ms(630000) #10,5 min

