'''
(1) Write a Python program that does the following:  
(a) Using the robot to get the temperature reading in Celsius.  Then convert the temperature into Fahrenheit.
Print the Celsius and Fahrenheit temperature in 3 decimal places. For example, The temperature reading in Celsius is 25.000 and Fahrenheit is 77.000
(b) Move the robot full forward for 4 seconds.
(c) Move the robot backward for 3 seconds with 80% on each wheel.
(d) Move the robot in anti-clockwise direction for 5 seconds with the right wheel at 80%.
'''


from time import sleep
from finch import Finch

# PART 1

def temperature(c):
    f = c * 9.0 / 5 + 32
    f = round (f, 3)
    return f

finch = Finch()

c = finch.temperature()
print temperature(c)
print c

# PART 2

finch.wheels(1.0, 1.0)
sleep(4)

# PART 3

finch.wheels(-0.8, -0.8)
sleep(3)

# PART 4

finch.wheels (0, 0.8)
sleep(5)

