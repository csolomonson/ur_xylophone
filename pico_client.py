from machine import Pin
import network
import socket
from time import ticks_ms

WIFI_SSID = "AgencyRobot"
WIFI_PASSWORD = "theagency3021"

SERVER_IP = '10.30.21.202'
PORT = 8004

led_pins = range(21,25)
leds = []

for pin in led_pins:
    leds.append(Pin(pin, Pin.OUT))

button_pins = range(2,17)
buttons = []

for pin in button_pins:
    buttons.append(Pin(pin, Pin.IN, Pin.PULL_DOWN))
    
state = [0] * 15
    
def check_buttons():
    n = 0
    for i in range(len(buttons)):
        #Deal with it
        val = buttons[i].value()
        if states[i] != val and val == 1:
            n = i
        states[i] = val
        
    return n

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)
print(wlan)
#Maybe assign an ip address?
#Right here, please

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))

def led_encode(n):
    #n from 0 to 15
    p = 4
    ans = [0]*p
    
    for i in range(p):
        if n >= 2**(p-i-1):
            ans[i] = 1
            n -= 2**(p-i-1)
    return ans
        

button_state = 0
while True:
    new_button_pressed = check_buttons()
    led_raw = sock.recv(1024)
    led_states = led_decode(led_raw)
    for i in range(len(led_states)):
        leds[i].value(led_states[i])
    if new_button_pressed != 0:
        print("trying to send")
        sock.send(str(new_buton_pressed) + '\n')
        print("sent")
        print(new_button_pressed)
    
    
    #sock.send("whatever")
    
