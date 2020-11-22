
#check to see if there are better values. 
leg_lift_amt = 15
leg_click_amt = 5
shoulder_fully_forward_right = 180
houlder_fully_forward_right = 0
waddle_foot = 5
waddle_shoulder = 20



def robot_raise_5_clicks():
    for leg in legs:
        for joint in leg.joints:
            if leg.joint != leg.shoulder:
                leg.joint.currAngle += leg_click_amt
                leg.joint.angle = leg.joint.currAngle
    robot.tall = True


def robot_lower_5_clicks():
    for leg in legs:
        for joint in leg.joints:
            if leg.joint != leg.shoulder:
                leg.joint.currAngle -=leg_click_amt
                leg.joint.angle = leg.joint.currAngle
    robot.tall = False


def lift_leg(legNUM):
    leg[legNUM].knee.currAngle += leg_lift_amt
    leg[legNUM].knee.angle = leg[legNUM].knee.currAngle

def lower_leg(legNUM):
    leg[legNUM].knee.currAngle -=leg_lift_amt
    leg[legNUM].knee.angle = leg[legNUM].knee.currAngle

def move_leg_forward_WALL(legNUM):
    lift_leg(legNUM)
    leg[legNUM].shoulder.angle = shoulder_fully_forward
    lower_leg(legNUM)

def move_leg_forward_WALL(legNUM):
    lift_leg(legNUM)
    if legNUM < 3:
        leg[legNUM].shoulder.currAngle = shoulder_fully_forward_right
    else:
        leg[legNUM].shoulder.currAngle = shoulder_fully_forward_left
    actuate(legs)
    lower_leg(legNUM) 

def lift_forward(legNUM):
    leg[legNUM].foot.currAngle += waddle_foot
    actuate(legs)
    if legNUM < 3:
        leg[legNUM].shoulder.currAngle -= waddle_shoulder
    else:
        leg[legNUM].shoulder.currAngle += waddle_shoulder
    actuate(legs)
    leg[legNUM].foot.currAngle -= waddle_foot
    actuate(legs)  

def push_backward(legNUM):
    if legNUM < 3:
        leg[legNUM].shoulder.currAngle += waddle_shoulder
    else:
        leg[legNUM].shoulder.currAngle -=waddle_shoulder
    actuate(legs)

def waddle_step():
    lift_forward(0)
    lift_forward_(5)
    push_backward_right(2)
    push_backward_left(3)
    lift_forward_right(2)
    lift_forward_left(3)
    push_backward_right(0)
    push_backward_left(5)    


def first_legs_climb_wall():
     ## check that we are tall
    if tall == False:
        robot_raise_5_clicks()
    ##raise middle legs
    ## check numbers to make sure they go to correct legs!!
    lift_leg(1)
    lift_leg(4)#check to see if this is the right angle addition to make it work
    ## move front legs one at a time
    move_leg_forward_WALL(0)
    move_leg_forward_WALL(3)

def last_legs_climb_wall():
    ## move front legs one at a time
    move_leg_forward_WALL(2)
    move_leg_forward_WALL(5)

