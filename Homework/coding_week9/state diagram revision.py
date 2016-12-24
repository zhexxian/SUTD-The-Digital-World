# State Diagram Practice

import libdw.sm as sm

class RunMod5(sm.SM):
    startState = 0
    def getNextValues(self,state,inp):
        if state == 0:
            if inp % 5 != 0:
                return 0,0
            else:
                return 1,1
        elif state == 1:
            if inp % 5 != 0:
                return 0,0
            else:
                return 2,2
        elif state == 2:
            if inp%5 != 0:
                return 0,0
            else:
                return 1,1

'''
def getNextValues(self,state,inp):
    if inp %5 == 0:
        if state>1:
            state = 0
        return (state +1, state +1)
    else:
        return (0,0)
B = RunMod5()
print B.transduce([1,2,3,10,20,30,25,4,6,7,10],verbose = True)

'''