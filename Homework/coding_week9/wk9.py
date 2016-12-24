'''
# import libdw.sm as sm

# COHORT
# Q1
import sm
class CM(sm.SM):
    def __init__(self, startState):
        self.startState = startState

    def getNextValues (self, state, inp):
        if state == 0:
            if inp == 50:
                nextState = 1
                outp = (50, '--',0)
            elif inp == 100:
                nextState = 0
                outp = (0, 'coke', 0)
            else:
                nextState = 0
                outp = (0, '--', inp)
        elif state == 1:
            if inp == 50:
                outp = (0, 'coke', 0)
                nextState = 0
            elif inp == 100:
                nextState = 0
                outp = (0, 'coke', 50)
            else:
                nextState = 0
                outp = (0, 'coke', inp)
        return (nextState, outp)


# Q5 question refer to tutor
# import sm
class CountingStateMachine(sm.SM):
    
    startState = 0
    
    def getNextValues(self, state, inp):
        if state == 1:
            return state+1, inp
        elif state % 2 == 0:
            return state+1, 0
        else:
            return state+1, inp
     
    
# HOMEWORK    
# Q3 question refer to tutor
# import sm
import libdw.sm as sm
class CommentsSM(sm.SM):
    startState = 'Non'

    def getNextValues(self, state, inp):
        if state == 'Non':
            if inp == '#':
                return('can','#')
            else:
                return('Non', None)
        if state == 'can':
            if inp != '\n':
                return('can',inp)
            else:
                return('Non',None)


'''        
# Q4 question refer to tutor
# import sm
import libdw.sm as sm
class FirstWordSM(sm.SM):
    startState = 'out'

    def getNextValues(self, state, inp):
        if state == 'out':
            if inp == '\n':
                return 'out',None
            elif inp == ' ':
                return 'out',None
            else:
                return 'in', inp
        elif state == 'in':
            if inp == ' ':
                return 'middle', None
            elif inp == '\n':
                return 'out',None
            else:
                return 'in', inp
        elif state == 'middle':
            if inp != '\n':
                return 'middle',None
            else:
                return 'out',None
            

