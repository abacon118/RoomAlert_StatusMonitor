# Room Alert ESP32 Monitor
# Andrew Bowman 2026
# https://docs.sunfounder.com/projects/umsk/en/latest/04_pi_pico/pico_lesson26_lcd.html
# https://microcontrollerslab.com/micropython-openweathermap-api-esp32-esp8266-sensorless-weather-station/
# AI assistance from Copilot was used in the creation of this.

ssid = 'YourBillWiTheScienceFi'
password = 'NachoPass*word'
#RA_URLs are the public URL for your Room Alert device
RA_URLs = ["https://account.roomalert.com/public/device/your-device-1","https://account.roomalert.com/public/device/your-device-2","https://account.roomalert.com/public/device/your-device-3"]
Locations = ["Site1","Site2","Site3"] #Update with your site names for RoomAlert
Temps = [None] * len(Locations)
lcd_char = 0


import time
import socket
import tm1637
from machine import Pin
tm = [
    tm1637.TM1637(clk=Pin(1), dio=Pin(0)),
    tm1637.TM1637(clk=Pin(3), dio=Pin(2)),
    tm1637.TM1637(clk=Pin(5), dio=Pin(4))
]

try:
  import urequests as requests
except:
  import requests
  
try:
  import ujson as json
except:
  import json

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

led6 = Pin(6, Pin.OUT)
led7 = Pin(7, Pin.OUT)
led8 = Pin(8, Pin.OUT)
led9 = Pin(9, Pin.OUT)
led10 = Pin(10, Pin.OUT)
led20 = Pin(20, Pin.OUT)
led21 = Pin(21, Pin.OUT)

led6.value(1)
led7.value(1)
led8.value(1)
led9.value(1)
led10.value(1)
led20.value(1)
led21.value(1)


PING_URLs = [ ("google.com", 443, led6),
              ("yahoo.com", 443, led7),
              ("cnn.com", 443, led8),
              ("foxnews.com", 80, led9),
              ("192.168.20.10", 4343, led10),
              ("yourdomain.com", 443, led20),
              ("yourserver.local", 8080, led21)]


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


def print_temp(display, f):

    if f < -9.9:
        display.show('lo')
        return
    if f > 99.9:
        display.show('hi')
        return
    raw = "{:4.2f}".format(f)   # e.g. "67.7"     # Format with one decimal
    dot_pos = raw.index('.')    # e.g. 2     # Find decimal BEFORE removing it
    s = raw.replace('.', '')    # "677"     # Remove the dot
    segs = display.encode_string(s)     # Encode the digits (3 digits + 1 blank)
    segs[dot_pos - 1] |= 0x80     # Add decimal point to the correct digit
    segs[-1] = 0b01110001      # Replace last digit with raw segment pattern for 'F'
    display.write(segs)     # Write raw segments directly

def tcp_ping(host, port=80, timeout=2000):
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.settimeout(timeout / 1000)

    start = time.ticks_ms()
    try:
        s.connect(addr)
        s.close()
        return True, time.ticks_diff(time.ticks_ms(), start)
    except Exception as e:
        return False, str(e)

while(1):
    for i in range(len(RA_URLs)):
        RA_data = requests.get(RA_URLs[i])
        RA_text = RA_data.text

        #print(RA_data.text)

        marker = "                                            <b>" #Find this on line 265 in the Room Alert HTML.  The Temp is right after it.
        start = RA_text.find(marker)

        if start != -1:
            start += len(marker)
            end = RA_text.find("°F", start)
            Temps[i] = float(RA_text[start:end].strip())
            print(Locations[i]," temperature:", Temps[i])
            print_temp(tm[i],Temps[i])
        else:
            print("Temperature not found")
            
    for host, port, led in PING_URLs:
            ok, info = tcp_ping(host, port)
            if ok:
                print(host, "reachable, latency:", info, "ms")
                led.value(0)
            else:
                print(host, "UNREACHABLE:", info)
                led.value(1)
                
    
    time.sleep(60)







