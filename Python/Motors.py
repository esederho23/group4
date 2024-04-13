from machine import Pin, PWM
from time import sleep

# Define pin numbers
pwmPIN=("GP16")
cwPin=("GP14") 
acwPin=("GP15")

# Define function to control motor movement
def motorMove(speed,direction,speedGP,cwGP,acwGP):
    # Ensure speed is within 0-100
    if speed > 100:
        speed = 100
    if speed < 0:
        speed = 0
    
    # Initialize Pico for mot speed control
    Speed = PWM(Pin(speedGP))
    Speed.freq(50)
    
    # Initialize colckwise and anti-clockwise pins
    cw = Pin(cwGP, Pin.OUT)
    acw = Pin(acwGP, Pin.OUT)
    
    # Set motor speed using duty cycle
    Speed.duty_u16(int(speed / 100 * 65536))
    
    # Control motor rotation direction
    if direction < 0:
        cw.value(0)
        acw.value(1)
    elif direction == 0:
        cw.value(0)
        acw.value(0)
    elif direction > 0:
        cw.value(1)
        acw.value(0)
# Example usage: Full-speed anti-clockwise rotation for 5 seconds
motorMove(100, -1, pwmPIN, cwPin, acwPin)
sleep(5)

# Turn off the motor
motorMove(0, 0, pwmPIN, cwPin, acwPin)

    