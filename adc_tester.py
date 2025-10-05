from explorer import ADC_3_PIN, display, WHITE, CYAN, BLACK
import machine, time

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

display.set_pen(BLACK)
drop_shadow_text("Press any button! :)", 65, 75, 2, 240, 4, CYAN)
display.update()

adc = machine.ADC(ADC_3_PIN)

while True:
    display.clear()
    drop_shadow_text("Current value: " + str(adc.read_u16()), 65, 75, 2, 240, 4, CYAN)
    display.update()
    time.sleep(0.5)