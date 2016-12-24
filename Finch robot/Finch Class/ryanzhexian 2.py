# -*- coding: cp1252 -*-

'''
(1) Write a Python program that gets the Celsius value from the robot.
Pass the value as an argument to a function called TempConvert.
This function converts Celsius into Fahrenheit and returns the result.
In the main function, prints the return value in 2 decimal places.
For example, if the Celsius value is 25, the output should be
‘The temperature reading in Celsius is 25.00 and Fahrenheit is 77.00’.  
(2) Write a Python program that prompts the user to input the forward
throttle value for both wheels and duration to move forward.
Both of these values are passed as arguments to a function called
Forward which does not return any value. This function moves
the robot forward for x number of seconds using these values.   
For example, if the input values are 0.7 and 3, the robot will move forward
with 70% throttle on both wheels for 3 seconds.  
'''

from time import sleep
from finch import Finch

finch = Finch()

def Temperature(c):
    f = c * 9.0 / 5 + 32
    c = round (c, 2)
    f = round (f, 2)
    print 'The temperature reading in Celcius is %s and Fahrenheit is %s' %(c,f)

Temperature(finch.temperature())

def Forward (a,b):
    finch.wheels(a, a)
    sleep(b)
    return None
a = input('forward throttle value:')
b = input('duration of movement:')

Forward(a,b)




finch.halt()
finch.close()
