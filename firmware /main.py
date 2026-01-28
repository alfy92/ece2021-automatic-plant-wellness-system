temp = 0
PLANT_MOISTURE_PIN = AnalogPin.P1
RESERVOIR_MOISTURE_PIN = AnalogPin.P2
PUMP_PIN = DigitalPin.P8


def on_forever():
    global temp
    BLiXel.set_brightness(1)
    # #Light Sensor
    if input.light_level() >= 95:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.ONE), 0x00ff00)
    else:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.ONE), 0xff0000)
    # #Temperature Sensor
    temp = input.temperature()
    if 15 <= temp and temp <= 29:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.TWO), 0x00ff00)
    else:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.TWO), 0xff0000)
    reservoir_value = pins.analog_read_pin(RESERVOIR_MOISTURE_PIN)
    if reservoir_value <= 500:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.FOUR), 0x00ff00)
        reservoir_ok = True
    elif reservoir_value >= 750:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.FOUR), 0xff0000)
        music.set_built_in_speaker_enabled(True)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        reservoir_ok = False
    else:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.FOUR), 0xff0000)
        reservoir_ok = False
    plant_value = pins.analog_read_pin(PLANT_MOISTURE_PIN)
    if plant_value < 600:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.THREE), 0x00ff00)
        needs_water = False
    elif plant_value < 790:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.THREE), 0x00ff00)
        needs_water = False
    else:
        BLiXel.set_pixel_colour(BLiXel.blixel_index(BLiXelIndex.THREE), 0xff0000)
        needs_water = True
    # #Water Pump Conditions
    if needs_water and reservoir_ok:
        bBoard_Motor.motor_left_duty(0)
        pins.digital_write_pin(PUMP_PIN, 1)
    else:
        pins.digital_write_pin(PUMP_PIN, 0)
        bBoard_Motor.motor_left_duty(50)
basic.forever(on_forever)


