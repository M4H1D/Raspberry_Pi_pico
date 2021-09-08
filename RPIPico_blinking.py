# Raspberry Pi Pico led blinking by your command.
# it’s only held on terminal. Not interpreter. 
from machine import Pin
led=Pin(25,Pin.OUT)
led.value(1)  #when you type 1 and press Enter the led will be blinking
led.value(0)  #when you type 0 and press Enter the led will stop blinking. 