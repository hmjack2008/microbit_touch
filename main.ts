input.onPinPressed(TouchPin.P0, function () {
    basic.showNumber(0)
})
input.onPinReleased(TouchPin.P0, function () {
    basic.showIcon(IconNames.No)
})
input.onLogoEvent(TouchButtonEvent.Released, function () {
    basic.showIcon(IconNames.No)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showNumber(1)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showIcon(IconNames.Yes)
})
input.onPinReleased(TouchPin.P1, function () {
    basic.showIcon(IconNames.No)
})
basic.showLeds(`
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    `)
pins.setEvents(DigitalPin.P0, PinEventType.Touch)
pins.setEvents(DigitalPin.P1, PinEventType.Touch)
basic.forever(function () {
	
})
