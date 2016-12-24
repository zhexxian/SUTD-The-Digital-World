def posVel(v0,t):
    a = 9.81
    y = float(format((v0 * t - 0.5 * a * t ** 2),'.2f')) #why can't I use round function here?
    y0 = float(format((v0 - a * t),'.2f')) # what are other unicode other than .2f?
    #y = float (format(y, '.2f'))
    #y0 = float (format(y0, '.2f')) # why 
    return (y, y0)

print posVel(2,3)
print posVel(2,3)