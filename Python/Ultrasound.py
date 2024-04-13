from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340
TRIG_PULSE_DURATION_US=10

trigger = Pin("GP7", Pin.OUT) # pin 10 in Pico
echo = Pin("GP6", Pin.IN)  # pin 9 in Pico

while True:
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trigger.value(0)

    ultrason_duration = time_pulse_us(echo, 1, 30000)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    print(f"Distance : {distance_cm} cm")
    time.sleep_ms(500)