def windChillTemp(ta, v):
    if ta >= -58 and ta <= 41 and v >= 2:
        twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.16
        return twc
    else:
        return 'Error'
        
# Test Programme:

ta = input('Outside temperature in Fahrenheit:')
v = input('Wind speed in miles per hour:')
def windChillTemp(ta, v):
    if ta >= -58 and ta <= 41 and v >= 2:
        twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.16
        return twc
    else:
        return 'Error'
print 'wind chill index: %s' %(windChillTemp(ta, v))        
