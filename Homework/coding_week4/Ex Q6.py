import math
def approx_ode(h,t0,y0,tn):
######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

    t = t0
    y = y0

    while t <= tn:  
        y = y + h* (0.5*f(t,y) + 0.5*f(t+h,y) + h*f(t,y))
        t+=h

    return round(y,3)



######### Ignore code below this line ######################################

def f(t, y):
    return 4.0-t+2.0*y


print approx_ode(0.1, 0, 1, 2.5)