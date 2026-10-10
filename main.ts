input.onButtonPressed(Button.A, function () {
    if (escaleras == 0) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        escaleras = 1
    } else if (escaleras == 1) {
        pins.servoWritePin(AnalogPin.P15, 0)
        pins.servoWritePin(AnalogPin.P16, 180)
        escaleras = 0
    }
})
input.onPinPressed(TouchPin.P2, function () {
    direccional = 2
})
input.onButtonPressed(Button.B, function () {
    if (escaleras == 0) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
        escaleras = 1
    } else if (escaleras == 1) {
        pins.servoWritePin(AnalogPin.P16, 0)
        pins.servoWritePin(AnalogPin.P15, 180)
        escaleras = 0
    }
})
let direccional = 0
let escaleras = 0
pins.servoWritePin(AnalogPin.P16, 360)
pins.servoWritePin(AnalogPin.P15, 360)
basic.forever(function () {
    if (input.pinIsPressed(TouchPin.P0)) {
        music.playTone(262, music.beat(BeatFraction.Whole))
    }
    if (direccional == 1) {
        led.plot(1, 3)
        basic.pause(100)
        led.unplot(1, 3)
        basic.pause(100)
    } else if (direccional == 2) {
        led.plot(3, 3)
        basic.pause(100)
        led.unplot(3, 3)
        basic.pause(100)
    } else if (direccional == 3) {
        led.unplot(3, 3)
        led.unplot(1, 3)
    }
})
