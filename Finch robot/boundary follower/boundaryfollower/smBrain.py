# -*- coding: utf-8 -*-
import math
import time
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    
    startState = 'Start'

    def getNextValues(self, state, inp):
        sonars = inp.sonars
        angle = math.atan(1-(2**0.5 * sonars[4])/sonars[3])
        d = sonars[4] * math.sin(angle)
        
        angle1 = math.atan(1-(2**0.5 * sonars[3])/sonars[4])
        d1 = sonars[3] * math.sin(angle1)
        
        if state == 'Start':
            if sonars[2]>0.35:
                state, fwd, rot = 'Start',0.2,0
            elif sonars[2]<=0.35:
                state, fwd, rot = 'leftTurn',0,0.7
        elif state == 'leftTurn':
            if sonars[2]>0.35 and (sonars[3]/sonars[4] >= 0.85):
                state, fwd, rot = 'Straight', 0.2, 0
            else:
                state, fwd, rot = 'leftTurn', 0, 0.7

            
        elif state == 'Straight':
            if sonars[4] > 0.5:
                state,fwd,rot='rightTurn',0,0
            elif sonars[2] <0.35:
                state, fwd, rot = 'leftTurn',0,0.7                
            else:
                state,fwd,rot = 'Straight',0.2,0
        elif state=='rightTurn':
            state,fwd,rot = 'rightTurn',0.2,-1.5
            if sonars [2] < 1.2:
                state = 'leftTurn'


        
        print state, sonars[3]/sonars[4]


        return (state, io.Action(fvel = fwd, rvel = rot))

mySM = MySMClass()
mySM.name = 'brainSM'

######################################################################
###
###          Brain methods
###
######################################################################

def plotSonar(sonarNum):
    robot.gfx.addDynamicPlotFunction(y=('sonar'+str(sonarNum),
                                        lambda: 
                                        io.SensorInput().sonars[sonarNum]))

# this function is called when the brain is (re)loaded
def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True, # slime trails
                                  sonarMonitor=True) # sonar monitor widget
    
    # set robot's behavior
    robot.behavior = mySM

# this function is called when the start button is pushed
def brainStart():
    robot.behavior.start(traceTasks = robot.gfx.tasks())

# this function is called 10 times per second
def step():
    inp = io.SensorInput()
    # print inp.sonars[3]
    robot.behavior.step(inp).execute()
    io.done(robot.behavior.isDone())

# called when the stop button is pushed
def brainStop():
    pass

# called when brain or world is reloaded (before setup)
def shutdown():
    pass
'''
            elif d>0:
                if d>0.5:
                    state,fwd,rot='Far',0,0
                if d<0.3:
                    state,fwd,rot = 'Near',0,0
                else:
                    state,fwd,rot = 'Straight',0.2,0
    elif state=='Far':
            if d>0.5:
                state,fwd,rot='Far',0.03,-0.2
            else:
                state,fwd,rot='farExit',0,0
        elif state=='farExit':
            if sonars[3]/sonars[4]<1.45:
                state,fwd,rot='farExit',0,0.2
            else:
                state,fwd,rot='Straight',0,0
        elif state=='Near':
            if d<0.3:
                state,fwd,rot='Near',0.03,0.2

            else:
                state,fwd,rot='nearExit',0,0
        elif state=='nearExit':
            if sonars[3]/sonars[4]>1.45:
                state,fwd,rot='nearExit',0,-0.2
            else:
                state,fwd,rot='Straight',0.2,0
'''