"""
"""
import time, machine, neopixel
from explorer import button_a, button_b, button_c, button_x, button_y, button_z, display, WHITE, CYAN, MAGENTA, YELLOW, GREEN, BLACK, BLUE, RED, SERVO_1_PIN, button_user

#Number of LEDs
LED_COUNT = const(45)

# A little function to save ourselves some time doing the drop shadows :)
def drop_shadow_text(text, x, y, offset, wrap, size, main_colour):

    # Draw the drop shadow
    display.set_pen(BLACK)
    display.text(text, x + offset, y + offset, wrap, size)

    # Draw the main text
    display.set_pen(main_colour)
    display.text(text, x, y, wrap, size)


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(WHITE)
    display.clear()
    display.update()


# set up
clear()
display.set_font("bitmap8")

# Clear all layers first
display.set_layer(0)
display.set_pen(WHITE)
display.clear()
display.set_layer(1)
display.set_pen(BLACK)
display.clear()

# Set the layer back to the first
display.set_layer(0)
np = neopixel.NeoPixel(machine.Pin(SERVO_1_PIN),LED_COUNT)

while True:
    if button_a.value() == 0:
        clear()
        drop_shadow_text("Red", 65, 75, 2, 240, 4, RED)
        for i in range(45):
            np[i] = (255,0,0)
        display.update()
        np.write()
        time.sleep(1)
        clear()
    elif button_b.value() == 0:
        clear()
        drop_shadow_text("Green", 65, 75, 2, 240, 4, GREEN)
        for i in range(45):
            np[i] = (0,255,0)
        display.update()
        np.write()
        time.sleep(1)
        clear()
    elif button_c.value() == 0:
        clear()
        drop_shadow_text("Blue", 65, 75, 2, 240, 4, BLUE)
        for i in range(45):
            np[i] = (0,0,255)
        display.update()
        np.write()
        time.sleep(1)
        clear()
    elif button_user.value() == 0:
        for i in range(45):
            np[i] = (0,0,0)
        np.write()        
    else:
        display.set_pen(BLACK)
        drop_shadow_text("Press any button! :)", 65, 75, 2, 240, 4, CYAN)
        display.update()
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses

