def on_button_pressed_a():
    global oprava
    oprava = zrychleni
input.on_button_pressed(Button.A, on_button_pressed_a)

naklon = 0
zrychleni = 0
oprava = 0
oprava = 0

def on_forever():
    global zrychleni, naklon
    zrychleni = input.acceleration(Dimension.X)
    naklon = zrychleni - oprava
    basic.clear_screen()
    if naklon > 100:
        led.plot(0, 2)
    elif naklon > 15:
        led.plot(1, 2)
    elif naklon < -100:
        led.plot(4, 2)
    elif naklon < -15:
        led.plot(3, 2)
    else:
        led.plot(2, 2)
basic.forever(on_forever)
