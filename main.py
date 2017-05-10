import time
import machine
import network
import urequests
import ubinascii

CONST_WIFISSID = "Freifunk"
CONST_WIFIPW = ""
CONST_APITOKEN = ""
CONST_SERVERURI = "http://philhil.de/openWaterer/index.php"
CONST_API_KEY = ''
CONST_ZIP = '70825'
CONST_COUNTRY = 'DE'


CONST_WATER_INTERVALL_MS = 15000 # 15 sec

CONST_SENSORREAD_PIN = 0 #A0
CONST_PUMPPIN = 5 #D1
CONST_HUMIDITY_PIN = 4 #D2

CONST_HYDROMAX = 400.0
CONST_RAINTHRESHOLD = 0.5 #mm ^3 

pin_PUMPPIN = machine.Pin(CONST_PUMPPIN, machine.Pin.OUT)
pin_HUMIDITY = machine.Pin(CONST_HUMIDITY_PIN, machine.Pin.OUT)
pin_SENSORREAD = machine.Pin(CONST_SENSORREAD_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
#pin_SENSORREAD = machine.Pin(CONST_SENSORREAD_PIN, machine.Pin.IN)
adc = machine.ADC(CONST_SENSORREAD_PIN)

wlan = network.WLAN(network.STA_IF)

def do_connect():
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(CONST_WIFISSID, CONST_WIFIPW)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def send_data(sensor_type, sensor_data):
    mac =  str(ubinascii.hexlify(wlan.config('mac')), 'ascii')
    params = '?token='+CONST_APITOKEN+'&command=send_data&device_id='+mac+'&name='+sensor_type+'&data='+str(sensor_data)
    resp = urequests.get(CONST_SERVERURI + params)
    print(resp.json())

def rainforecast():
    precipitation = 0.0
    
    if wlan.isconnected():
        r = urequests.get(CONST_SERVERURI+'?token='+CONST_APITOKEN+'&command=get_json&hours=6&zip='+CONST_ZIP+','+CONST_COUNTRY+'&lang=de&units=metric&appid='+CONST_API_KEY)
        forecast = r.json()    
        if "rain" in forecast:
            precipitation = float(forecast["rain"])
        
    print('TOTAL ' + str(precipitation) + ' (Rain volume for next 6 hours per mm)')
    return precipitation

#read Humidity Sensor Data
def getHumidityValue():
    pin_HUMIDITY.value(1)
    time.sleep_ms(500)
    wet = adc.read()
    time.sleep_ms(500)
    wet = wet + adc.read()
    time.sleep_ms(500)
    wet = wet + adc.read()
    pin_HUMIDITY.value(0)
    print(wet / 3)
#push to database
    send_data("humidity", wet/3)
    return wet / 3

#check if humidity and rainforecast threshold is reached -> Watering
def check_watering():
    humidityVal = getHumidityValue()
    rain = rainforecast()

    print(float(humidityVal))
    print(float(rain))
    print(float(CONST_HYDROMAX))
    print(float(CONST_RAINTHRESHOLD))

    if float(humidityVal) > float(CONST_HYDROMAX)  and float(rain) < float(CONST_RAINTHRESHOLD):
        pin_PUMPPIN.value(1)
        time.sleep_ms(CONST_WATER_INTERVALL_MS)
        pin_PUMPPIN.value(0)


time.sleep_ms(5000) #5 sec
do_connect()

while True:

    check_watering()

    time.sleep_ms(63000) #1,05 min

