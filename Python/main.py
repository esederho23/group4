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
    
# Initialize motors
m1 = Pin("GP21", Pin.OUT)
m2 = Pin("GP20", Pin.OUT)
m3 = Pin("GP19", Pin.OUT)
m4 = Pin("GP18", Pin.OUT)

en1 = Pin("GP17", Pin.OUT)
en2 = Pin("GP16", Pin.OUT)

# Function to enable motors, power on
def Enable_motor():
    en1(1)  # motor 1 enable, set value 0 to disable
    en2(1)  # motor 2 enable, set value 0 to disable

# Other functions for motor
def Motor1_forward():
    m1(1)
    m2(0)
    
def Motor1_reverse():
    m1(0)
    m2(1)
    
def Motor2_forward():
    m3(1)
    m4(0)
    
def Motor2_reverse():
    m3(0)
    m4(1)
    
def Motor_stop():
    m1(0)
    m2(0)
    m3(0)
    m4(0)

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
    
    #Power motors
    Enable_motor()
    
    # Check if gyro says stop
    if ay < -0.35:
        stop_buzzer()
        Motor_stop()
        break
    else:
        Motor1_forward()
        Motor2_forward()
        sound_buzzer()
        
    # Use motors and turn
    #if distance_cm < 10:
        #Motor_stop()
        #sleep_ms(500)
        #Motor1_forward()
        #Motor2_reverse()
        #sleep_ms(1000)
    #else:
        #Motor1_forward()
        #Motor2_forward()
    
    # Print data for debugging
    print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
    print(f"Distance : {distance_cm} cm",end="\r")
    sleep(0.2)