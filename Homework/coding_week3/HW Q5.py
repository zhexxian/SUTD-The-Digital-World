import math

######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

######### Add you code below this line
######### Return your answer correct to 3 decimal places




######### Ignore code below this line ######################################

def f(t, y):
    return 3.0+math.exp(-t)-0.5*y

def approx_ode(h,t0,y0,tn):
    y = y0
    t = t0
    '''
    while t < (tn-h):
        y = y + h * f(t, y)
        t += h
    '''
    for i in range(t0,int(tn/h)):
        y+=h*f((i*h),y)
        
    return round(y,3)
    
print approx_ode(0.1,0,1,4)
print approx_ode(0.1,0,1,5)
        

  