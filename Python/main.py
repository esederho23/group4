from imu import MPU6050
from utime import sleep, sleep_ms
from machine import Pin, I2C, PWM, time_pulse_us
import time

# Initialize I2C and MPU 6050
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

# Initialize Buzzer
buzzer_pin = Pin("GP5")
buzzer = PWM(buzzer_pin)
buzzer.freq(500)

# Initialize ultrasound sensor
SOUND_SPEED = 340
TRIG_PULSE_DURATION_US = 10

trigger = Pin("GP7", Pin.OUT)
echo = Pin("GP6", Pin.IN)

# Function to sound the buzzer
def sound_buzzer():
    buzzer.duty_u16(1000)
    
# Function to stop the buzzer
def stop_buzzer():
    buzzer.duty_u16(0)

# Main loop
while True:
    # Read accelerometer data
    ax = round(imu.accel.x, 2)
    ay = round(imu.accel.y, 2)
    az = round(imu.accel.z, 2)
    gx = round(imu.gyro.x)
    gy = round(imu.gyro.y)
    gz = round(imu.gyro.z)
    tem = round(imu.temperature, 2)
    
    # Read ultrasound data
    trigger.value(0)
    time.sleep_us(5)
    trigger.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trigger.value(0)
    
    # Calculate distance
    ultrasound_duration = time_pulse_us(echo, 1, 30000)
    distance_cm = SOUND_SPEED * ultrasound_duration / 20000
    
    # Check if gyro says stop
    if ay < -0.35:
        stop_buzzer()
        break
    else:
        sound_buzzer()
    
    # Print data for debugging
    print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
    print(f"Distance : {distance_cm} cm",end="\r")
    sleep(0.2)