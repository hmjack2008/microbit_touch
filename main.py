def on_pin_pressed_p0():
    basic.show_number(0)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_released_p0():
    basic.show_icon(IconNames.NO)
input.on_pin_released(TouchPin.P0, on_pin_released_p0)

def on_logo_released():
    basic.show_icon(IconNames.NO)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

def on_pin_pressed_p1():
    basic.show_number(1)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_logo_touched():
    basic.show_icon(IconNames.YES)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_pin_released_p1():
    basic.show_icon(IconNames.NO)
input.on_pin_released(TouchPin.P1, on_pin_released_p1)

basic.show_leds("""
    . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
""")
pins.set_events(DigitalPin.P0, PinEventType.TOUCH)
pins.set_events(DigitalPin.P1, PinEventType.TOUCH)

def on_forever():
    pass
basic.forever(on_forever)
