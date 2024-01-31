def on_touch_fwd_button_down():
    fwdMotors.middle_servo.fwd_set_speed(0)
    fwdSensors.led_ring.fwd_set_all_pixels_colour(0x000000)
fwdSensors.touch.fwd_on_touch(jacdac.ButtonEvent.DOWN, on_touch_fwd_button_down)

def on_dial1_fwd_dial_turned_direction_ccw(difference):
    global turbinespeed
    turbinespeed = fwdSensors.dial1.fwd_position()
    fwdMotors.middle_servo.fwd_set_speed(turbinespeed)
    if turbinespeed <= -40:
        fwdSensors.led_ring.fwd_set_all_pixels_colour(0x00ff00)
    else:
        fwdSensors.led_ring.fwd_set_all_pixels_colour(0xff0080)
fwdSensors.dial1.fwd_on_dial_turned(fwdSensors.DialDirection.CCW,
    on_dial1_fwd_dial_turned_direction_ccw)

def on_dial1_fwd_dial_turned_direction_cw(difference2):
    global turbinespeed
    turbinespeed = fwdSensors.dial1.fwd_position()
    fwdMotors.middle_servo.fwd_set_speed(turbinespeed)
    if turbinespeed >= 40:
        fwdSensors.led_ring.fwd_set_all_pixels_colour(0x00ff00)
    else:
        fwdSensors.led_ring.fwd_set_all_pixels_colour(0xff0080)
fwdSensors.dial1.fwd_on_dial_turned(fwdSensors.DialDirection.CW,
    on_dial1_fwd_dial_turned_direction_cw)

turbinespeed = 0
turbinespeed = 0