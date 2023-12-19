# Youtube Proximity Controller
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import neopixel
import random
import time
from adafruit_apds9960.apds9960 import APDS9960

apds = APDS9960(board.I2C())  # initializes the I2C bus then the APDS-9960 library
keyboard = Keyboard(usb_hid.devices) #sets up keyboard
pixels = neopixel.NeoPixel(board.NEOPIXEL, 2)  # activates the two LED on the board
pixels.brightness = 0.1
# if gesture is enabled, proximity wont be reliable

apds.enable_proximity = True  # proximity produces value from 0-255 with apds.proximity
apds.enable_gesture = True  # uses gesture function
"""
e.g. gesture = apds.gesture()
the four gestures are up, down, left, and right
with function returning values 1 through 4, in that order
"""

def temp_rainbow_rgb(r, g, b): #default rainbow when no controls in effect, for now its random colors
    new_r = random.randint(0, 255)
    new_g = random.randint(0, 255 - new_r)
    new_b = (255 - new_r - new_g)
    pixels.fill((((new_r + r)/2), ((new_g + g)/2), ((new_b + b)/2)))
    time.sleep(0.5)
    r = random.randint(0, 255)
    g = random.randint(0, 255 - r)
    b = (255 - r - g)

    return r, g, b

r = 0
g = 0
b = 0

while True:
    r, g, b = temp_rainbow_rgb(r, g, b)
    gesture = apds.gesture()

    if gesture == 1: #up -> right
        pixels.fill((25, 200, 25))
        time.sleep(1)
        keyboard.send(Keycode.L)
    elif gesture == 2: #down -> left
        pixels.fill((200, 10, 10))
        time.sleep(1)
        keyboard.send(Keycode.J)
    elif gesture == 3: #left -> up
        pixels.fill((0, 0, 255))
        time.sleep(1)
        keyboard.send(Keycode.K)
    elif gesture == 4: #right -> down
        pixels.fill((128,0,128))
        time.sleep(1)
        keyboard.send(Keycode.SPACE)
