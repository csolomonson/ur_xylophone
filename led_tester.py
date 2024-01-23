from machine import Pin
import time

led_pins = range(18,22)
leds = []

for pin in led_pins:
    leds.append(Pin(pin, Pin.OUT))

def led_encode(n):
    #n from 0 to 15
    p = 4
    ans = [0]*p
    
    for i in range(p):
        if n >= 2**(p-i-1):
            ans[i] = 1
            n -= 2**(p-i-1)
    return ans

led_raw = 0
while True:
    #led_raw = (led_raw + 1) % 16
    led_raw = int(input('> '))
    led_states = led_encode(led_raw)
    print(led_states)
    for i in range(len(led_states)):
        leds[i].value(led_states[i])
    time.sleep(0.2)