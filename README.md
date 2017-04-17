# !!
# THIS IS STILL IN DEV! NOT READY TO USE!
# !!


# openWaterer
ESP8266 plant water automation

## Description
tbd

## Part list

| Part | Supplyer
| ------ | ------ |
| ESP8266 |[Aliexpress](https://de.aliexpress.com/item/D1-mini-Mini-NodeMcu-4M-bytes-Lua-WIFI-Internet-of-Things-development-board-based-ESP8266-by/32662942091.html) [Amazon](https://www.amazon.de/dp/B01ELFAF1S/ref=cm_sw_em_r_mt_dp_3qn9ybM4RJ55X)|
| Hygrometer Sensor | [Aliexpress ](https://de.aliexpress.com/item/Smart-Electronics-Soil-Moisture-Hygrometer-Detection-Humidity-Sensor-Module-For-arduino-Development-Board-DIY-Robot-Smart/32328189936.html?) [Amazon](https://www.amazon.de/dp/B00ZR3B60I/ref=cm_sw_em_r_mt_dp_wsn9ybG37N97V) |
| DHT 22 | [Aliexpress](https://de.aliexpress.com/item/DHT22-AM2302-Digital-Temperature-And-Humidity-Sensor-Module-Replace-SHT11-SHT15/1859157389.html) [Amazon](https://www.amazon.de/dp/B06XF4TNT9/ref=cm_sw_em_r_mt_dp_4sn9ybG0256WJ) |
| 5V Relay | [Aliexpress](https://de.aliexpress.com/item/Free-Shipping-1PCS-5V-low-level-trigger-One-1-Channel-Relay-Module-interface-Board-Shield-For/32480128984.html) [Amazon](https://www.amazon.de/dp/B01CQ10YXI/ref=cm_sw_em_r_mt_dp_Ftn9ybW2B3HHT) |
| Pump | []() |


## Setup
tbd

prerequire: python pip picocom
latest micropython stable: http://micropython.org/download#esp8266
```sh
$ pip install esptool
$ esptool.py --port /dev/ttyUSB0 erase_flash
$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin
$ picocom --b 115200 /dev/ttyUSB0
>>> import webrepl_setup
```
