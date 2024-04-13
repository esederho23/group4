from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin("GP5"))
buzzer.freq(500)
buzzer.duty_u16(1000)
sleep(1)
buzzer.duty_u16(0)