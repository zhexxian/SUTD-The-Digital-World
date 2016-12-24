import math
import libdw.sm as sm
from soar.io import io
import libdw.gfx as gfx
import libdw.util as util
import libdw.sonarDist as sonarDist

######################################################################
#
#            Brain SM
#
######################################################################

desiredRight = 0.4
forwardVelocity = 0.1


# No additional delay
class Sensor(sm.SM):
    def getNextValues(self, state, inp):
        v = sonarDist.getDistanceRight(inp.sonars)
        print 'Dist from robot center to wall on right', v
        return (state, v)

# inp is the distance to the right
class WallFollower(sm.SM):
    startState = 0
    def getNextValues(self, state, inp):
        k1, k2 = 10, -9.97
        error = desiredRight - inp
        
        return error, io.Action(fvel = forwardVelocity, rvel = k1 * error + k2 * state)


sensorMachine = Sensor()
sensorMachine.name = 'sensor'
mySM = sm.Cascade(sensorMachine, WallFollower())

######################################################################
#
#            Running the robot
#
######################################################################

def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=False)
    robot.gfx.addStaticPlotSMProbe(y=('rightDistance', 'sensor',
                                      'output', lambda x:x))
    robot.behavior = mySM
    robot.behavior.start(traceTasks = robot.gfx.tasks())

def step():
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())

def brainStop():
    pass
