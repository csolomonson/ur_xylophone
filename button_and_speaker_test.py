from machine import Pin, PWM
from time import ticks_ms

button_pins = range(2,17)
buttons = []

speaker = PWM(Pin(16))

for pin in button_pins:
    buttons.append(Pin(pin, Pin.IN, Pin.PULL_DOWN))

def check_buttons():
    n = 0
    for i in range(len(buttons)):
        #Deal with it
        n += buttons[i].value() * 2**i
    return n
button_state = 0
timer = 0
while True:
    new_state = check_buttons()
    if button_state != new_state:
        timer = ticks_ms()
        print(new_state)
        button_state = new_state
        speaker.freq(new_state+100)
        speaker.duty_u16(1000)
    if ticks_ms() - timer > 1000:
        speaker.duty_u16(0)

    