from math import *
import numpy as np
import actuation

class Joint:
    def __init__(self, board, channel, minPulse, maxPulse, startAngle):
        self.board = board
        self.channel = channel
        self.minPulse = minPulse
        self.maxPulse = maxPulse
        self.startAngle = startAngle
        self.currAngle = self.startAngle


JOINT1 = Joint(0, 0, 600, 2500, 135)
JOINT2 = Joint(0, 1, 575, 2500, 135)
JOINT3 = Joint(0, 2, 600, 2500, 90)
JOINT4 = Joint(0, 3, 550, 2500, 135)
JOINT5 = Joint(0, 4, 550, 2500, 135)
JOINT6 = Joint(0, 5, 700, 2500, 90)
JOINT7 = Joint(0, 6, 700, 2500, 135)
JOINT8 = Joint(0, 7, 600, 2500, 135)
JOINT9 = Joint(0, 8, 500, 2500, 90)
JOINT10 = Joint(1, 0, 750, 2500, 135)
JOINT11 = Joint(1, 1, 700, 2500, 135)
JOINT12 = Joint(1, 2, 500, 2600, 90)
JOINT13 = Joint(1, 3, 500, 2500, 135)
JOINT14 = Joint(1, 4, 700, 2500, 135)
JOINT15 = Joint(1, 5, 500, 2500, 90)
JOINT16 = Joint(1, 6, 500, 2500, 135)
JOINT17 = Joint(1, 7, 600, 2500, 135)
JOINT18 = Joint(1, 8, 600, 2500, 90)


class Leg:
    def __init__(self, foot, knee, shoulder):
        self.foot = foot
        self.knee = knee
        self.shoulder = shoulder
        self.joints = [foot, knee, shoulder]


LEG1 = Leg(JOINT1, JOINT2, JOINT3)
LEG2 = Leg(JOINT4, JOINT5, JOINT6)
LEG3 = Leg(JOINT7, JOINT8, JOINT9)
LEG4 = Leg(JOINT10, JOINT11, JOINT12)
LEG5 = Leg(JOINT13, JOINT14, JOINT15)
LEG6 = Leg(JOINT16, JOINT17, JOINT18)

LEGS = [LEG1, LEG2, LEG3, LEG4, LEG5, LEG6]


class Hexapod:
    #leg length
    l1=5
    l2=6
    leg_lift_amt = 15
    leg_click_amt = 5
    shoulder_fully_forward_right = 180
    houlder_fully_forward_right = 0
    waddle_foot = 5
    waddle_shoulder = 20
    footNo = 0
    kneeNo = 1
    shoulderNo = 2
    up = 1
    down = -1
    goalFoot = 90
    incAngle = 10
    goalShoulder = 90
    even = 2
    odd = 1

    def __init__(self,step_size,num_step,step_height, tall):
        self.step_size=step_size
        self.num_step=num_step
        self.step_height=step_height
        self.tall = False
    def gait_trajectory(self,leg_height):
        # leg_height: z distance from shoulder to feet when walking, fixed
        y=np.linspace(-step_size,step_size,num_step)
        for i, value in enumerate(y):
            z[i]=sqrt(step_height**2-value**2)+leg_height
        return z
    def IK(x,z):
        theta2=(x**2+z**2-l1**2-l2**2)/(2*l1*l2)
        theta1=atan(z/x)-atan((l2*sin(theta2))/(l1+l2*cos(theta2)))
        return degrees(theta1),degrees(theta2)
    def forward(self,sensor):
        leg_x=20 # x distance from shoulder to feet when walking, fixed
        leg_z=25 # z distance from shoulder to feet when walking, fixed
        z = gait_trajectory(leg_z)
        angle_range=30 # travel range for shoulder angles
        angle_step=angle_range/num_step
        #prepare for walking move 2,4,6 forward half angle range
        for i in range(3):
            leg[i+1].shoulder.currAngle-=angle_range/2
            
        '''
        if sensor==1: #stops walking function/reset angles
            for i in range(6):
                leg[i].shoulder.currAngle=leg[i].shoulder.startAngle
                leg[i].knee.currentAngle=leg[i].knee.startAngle
                leg[i].foot.currentAngle=leg[i].foot.startAngle
                actuate(legs)
            '''
        j = 0
        for i in range(num_step): # walking
            #when j is even, 246 forwards, 135 backwards
            if j%2==0 and i%2==0:
                leg[i].shoulder.currAngle-=angle_step
                leg[i].knee.currAngle+=(IK(leg_x,z[i])[0]-135)
                # -135 to get the angle movement, might need to be adjusted
                # depends on the servo orientation
                leg[i].foot.currAngle += (IK(leg_x, z[i])[1]-135)
            elif j%2==0 and i%2==1:
                leg[i].shoulder.currAngle += angle_step
            # when j is odd, 135 forwards, 246 backwards
            elif j%2==1 and i%2==0:
                leg[i].shoulder.currAngle += angle_step
            elif j%2==1 and i%2==1:
                leg[i].shoulder.currAngle -= angle_step
                leg[i].knee.currAngle += (IK(leg_x, z[i])[0]-135)
                leg[i].foot.currAngle += (IK(leg_x, z[i])[1]-135)
            j+=1
                actuate(legs)
                
    def robot_raise_5_clicks(self):
        for leg in legs:
            for joint in leg.joints:
                if leg.joint != leg.shoulder:
                    leg.joint.currAngle += leg_click_amt
                    leg.joint.angle = leg.joint.currAngle
        robot.tall = True


    def robot_lower_5_clicks(self):
        for leg in legs:
            for joint in leg.joints:
                if leg.joint != leg.shoulder:
                    leg.joint.currAngle -=leg_click_amt
                    leg.joint.angle = leg.joint.currAngle
        robot.tall = False


    def lift_leg(self, legNUM):
        leg[legNUM].knee.currAngle += leg_lift_amt
        leg[legNUM].knee.angle = leg[legNUM].knee.currAngle

    def lower_leg(self, legNUM):
        leg[legNUM].knee.currAngle -=leg_lift_amt
        leg[legNUM].knee.angle = leg[legNUM].knee.currAngle

    def move_leg_forward_WALL(self, legNUM):
        lift_leg(legNUM)
        leg[legNUM].shoulder.angle = shoulder_fully_forward
        lower_leg(legNUM)

    def move_leg_forward_WALL(self, legNUM):
        lift_leg(legNUM)
        if legNUM < 3:
            leg[legNUM].shoulder.currAngle = shoulder_fully_forward_right
        else:
            leg[legNUM].shoulder.currAngle = shoulder_fully_forward_left
        actuate(legs)
        lower_leg(legNUM) 

    def lift_forward(self, legNUM):
        leg[legNUM].foot.currAngle += waddle_foot
        actuate(legs)
        if legNUM < 3:
            leg[legNUM].shoulder.currAngle -= waddle_shoulder
        else:
            leg[legNUM].shoulder.currAngle += waddle_shoulder
        actuate(legs)
        leg[legNUM].foot.currAngle -= waddle_foot
        actuate(legs)  

    def push_backward(self, legNUM):
        if legNUM < 3:
            leg[legNUM].shoulder.currAngle += waddle_shoulder
        else:
            leg[legNUM].shoulder.currAngle -=waddle_shoulder
        actuate(legs)

    def waddle_step(self):
        lift_forward(0)
        lift_forward_(5)
        push_backward_right(2)
        push_backward_left(3)
        lift_forward_right(2)
        lift_forward_left(3)
        push_backward_right(0)
        push_backward_left(5)    


    def first_legs_climb_wall(self):
         ## check that we are tall
        if self.tall == False:
            robot_raise_5_clicks()
        ##raise middle legs
        ## check numbers to make sure they go to correct legs!!
        lift_leg(1)
        lift_leg(4)#check to see if this is the right angle addition to make it work
        ## move front legs one at a time
        move_leg_forward_WALL(0)
        move_leg_forward_WALL(3)

    def last_legs_climb_wall(self):
        ## move front legs one at a time
        move_leg_forward_WALL(2)
        move_leg_forward_WALL(5)
    
    def MoveJoint(self, jointNo,legNo,incAngle,dir):
    leg[legNo].joints[jointNo].currAngle += incAngle*dir
    #0 foot; 1 knee; 2 shoulder

    def MoveJointSet(self, goalAngle,incAngle,jointNo,legSet,dir):
        for k in range(goalAngle/incAngle):
            for i in range(len(LEGS)):
                if i % legSet == 0:
                    MoveJoint(jointNo,i,k*incAngle,dir)
            actuate(legs)


    def even_legs_turn(self):
        MoveJointSet(goalFoot,incAngle,footNo,even,up)
        MoveJointSet(goalShoulder,incAngle,shoulderNo,even,up)
        MoveJointSet(goalFoot,incAngle,footNo,even,down)

    def odd_legs_turn(self):
        MoveJointSet(goalFoot,incAngle,footNo,odd,up)
        MoveJointSet(goalShoulder,incAngle,shoulderNo,odd,up)
        MoveJointSet(goalFoot,incAngle,footNo,odd,down)

