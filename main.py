def on_button_pressed_a():
    global escaleras
    if escaleras == 0:
        basic.show_leds("""
            # . . . .
            # # . . .
            . # # . .
            . . # # .
            . . . # #
            """)
        escaleras = 1
    elif escaleras == 1:
        pins.servo_write_pin(AnalogPin.P15, 0)
        pins.servo_write_pin(AnalogPin.P16, 180)
        escaleras = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global direccional
    direccional = 2
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global escaleras
    if escaleras == 0:
        basic.show_leds("""
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        escaleras = 1
    elif escaleras == 1:
        pins.servo_write_pin(AnalogPin.P16, 90)
        pins.servo_write_pin(AnalogPin.P15, 90)
        escaleras = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

direccional = 0
escaleras = 0
pins.servo_write_pin(AnalogPin.P16, 90)
pins.servo_write_pin(AnalogPin.P15, 90)

def on_forever():
    if input.pin_is_pressed(TouchPin.P0):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
    if direccional == 1:
        led.plot(1, 3)
        basic.pause(100)
        led.unplot(1, 3)
        basic.pause(100)
    elif direccional == 2:
        led.plot(3, 3)
        basic.pause(100)
        led.unplot(3, 3)
        basic.pause(100)
    elif direccional == 3:
        led.unplot(3, 3)
        led.unplot(1, 3)
basic.forever(on_forever)
