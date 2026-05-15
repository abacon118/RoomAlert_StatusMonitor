# Room Alert Status Monitor
ESP32 based status monitor for RoomAlert Temperature monitors and HTTP/HTTPS based web services

## ESP32 Setup
1. [Install MicroPython](https://micropython.org/download/ESP32_GENERIC_C3/)
2. Copy libaries
3. Save RA_StatusMonitor.py as boot.py on the ESP32 using Thonny or another similar IDE.

## Room Alert Setup
You must create a public URL for your Room Alert device.  Paste the URL(s) in line 10 of the code.

## Parts
- 3x [TM1637 4 bit 7 segment display](https://www.aliexpress.us/item/3256805913248771.html?spm=a2g0o.order_list.order_list_main.53.21d81802YQizun&gatewayAdapt=glo2usa)
- 1x [ESP 32 C3 Super Mini](https://www.aliexpress.us/item/3256807754944428.html?spm=a2g0o.order_list.order_list_main.58.21d81802YQizun&gatewayAdapt=glo2usa&_randl_shipto=US)
- 7x Red LEDs
- 7x Green LEDs
- 14x 220 Ohm 0603 Resistors


## Schematic
[Schematic PDF](/Gerber_RoomAlert_Generic_PCB_1-copy_2026-05-15.pdf)
![Schematic](/Photos/Schematic_RoomAlert_Generic_2026-05-15.png)

## PCB
[Gerber ZIP](/Gerber_RoomAlert_Generic_PCB_1-copy_2026-05-15.zip)
[EasyEDA Files](/RoomAlert_EasyEDA.zip)
![PCB](/Photos/RA_PCB.png)
