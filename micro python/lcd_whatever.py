from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
from time import sleep

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(2), sda = Pin(1), freq=400000)

display = SSD1306_I2C(128, 64, i2c)

# display.invert(1)
#display.contrast(100)




while True:
    display.text('Example 1:',0,0)

    
    display.fill(0)
    display.text('@p1sam',0,0,1)
    display.show()
    sleep(1)

    display.fill(0)
    display.text('George',0,0,1)
    display.show()
    sleep(1)

    display.fill(0)
    display.text('Jewel',0,0,1)
    display.show()
    sleep(1)
    
    display.fill(0)
    display.text('Victor',0,0,1)
    display.show()
    sleep(1)
    

  
    
