import machine
import time
red_led = machine.Pin(15, machine.Pin.OUT)
yellow_led = machine.Pin(14, machine.Pin.OUT)
green_led = machine.Pin(13,machine.Pin.OUT)
print("Traffic Light Simulator Started!")
while True:
    green_led.value(1)
    yellow_led.value(0)
    red_led.value(0)
    time.sleep(5)

    green_led.value(0)
    yellow_led.value(1)
    red_led.value(0)
    time.sleep(5)

    green_led.value(0)
    yellow_led.value(0)
    red_led.value(1)
    time.sleep(5)