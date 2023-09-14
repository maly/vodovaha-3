input.onButtonPressed(Button.A, function () {
    oprava = zrychleni
})
let naklon = 0
let zrychleni = 0
let oprava = 0
oprava = 0
basic.forever(function () {
    zrychleni = input.acceleration(Dimension.X)
    naklon = zrychleni - oprava
    basic.clearScreen()
    if (naklon > 100) {
        led.plot(0, 2)
    } else if (naklon > 15) {
        led.plot(1, 2)
    } else if (naklon < -100) {
        led.plot(4, 2)
    } else if (naklon < -15) {
        led.plot(3, 2)
    } else {
        led.plot(2, 2)
    }
})
