from gpiozero import LED, Button
from time import sleep

led1 = LED(16)
led2 = LED(17)
button = Button(26)

led_on = False

def button_pressed():
    global led_on
    if not led_on:
        led1.blink(1) 
        sleep(0.5)
        led2.blink(1) 
        led_on = True
    else:
        led1.off() 
        led2.off()  
        led_on = False

button.when_pressed = button_pressed

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    pass

led1.close()
led2.close()
button.close()

