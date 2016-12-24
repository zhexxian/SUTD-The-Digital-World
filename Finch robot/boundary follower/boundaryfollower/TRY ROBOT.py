# -*- coding: utf-8 -*-
import math
import time
import libdw.util as util
import libdw.sm as sm
import libdw.gfx as gfx
from soar.io import io

class MySMClass(sm.SM):
    

    def getNextValues(self, state, inp):
        

        return (state, io.Action(fvel = 0, rvel = 1))

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