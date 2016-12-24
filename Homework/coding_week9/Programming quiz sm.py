import libdw.sm as sm
class RunOfEvenNumbers(sm.SM):
   startState = 'Not'
   def getNextValues(self, state, inp):
      
      if state == 'Not':
          if inp % 2 != 0:
              return 'Not',0
          else:
              return 1,1
      else:
          
          if inp % 2 != 0:
              return 'Not',0
          else:
              
              return state+1,state+1
        
