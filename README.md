# group4
Moving alarm clock

Pin chart for Raspberry Pi Pico W in Chart.xlsx

To create a working clock, you need the following programs:
imu.py
vector3.py
main.py

Imu and vector3 are for the gyroscope (drivers).
All other programs in the Python-file are test programs for different parts. Use them only in the debugging process.

Start the extra batterypack (6 V) first and then main battery pack (4,5 V). The alarm sounds after 5 seconds. You can change that in main.py in the def Alarm_time() function.

The alarm turns off when you shake the alarm clock.

