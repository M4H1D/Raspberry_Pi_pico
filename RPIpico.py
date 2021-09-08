import machine as m
import utime as t
led=m.Pin(25,m.Pin.OUT)
while True:
	led.value(1)
	t.sleep(1)
	led.value(0)
	t.sleep(1)