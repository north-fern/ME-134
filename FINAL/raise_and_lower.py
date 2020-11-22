
#check to see if there are better values. 
leg_lift_amt = 15
leg_click_amt = 5
shoulder_fully_forward = 180;

def robot_raise_5_clicks():
    for leg in legs:
        for joint in leg.joints:
            if leg.joint != leg.shoulder:
                leg.joint.currAngle = leg.joint.currAngle + leg_click_amt
                leg.joint.angle = leg.joint.currAngle
    robot.tall = True


def robot_lower_5_clicks():
    for leg in legs:
        for joint in leg.joints:
            if leg.joint != leg.shoulder:
                leg.joint.currAngle = leg.joint.currAngle - leg_click_amt
                leg.joint.angle = leg.joint.currAngle
    robot.tall = False


def lift_leg(legNUM):
    leg[legNUM].knee.currAngle = leg[legNUM].knee.currAngle + leg_lift_amt
    leg[legNUM].knee.angle = leg[legNUM].knee.currAngle

def lower_leg(legNUM):
    leg[legNUM].knee.currAngle = leg[legNUM].knee.currAngle - leg_lift_amt
    leg[legNUM].knee.angle = leg[legNUM].knee.currAngle

def move_leg_forward_WALL(legNUM):
    lift_leg(legNUM)
    leg[legNUM].shoulder.angle = shoulder_fully_forward
    lower_leg(legNUM)

def lift_forward(legSET)


def push_backward(legSET)



def waddle():
    legsetFront = [1 4]
    legsetBack = [3 6]




def climb_wall():

     ## check that we are tall

    if tall == False:
        robot_raise_5_clicks()


    ##raise middle legs
    ## check numbers to make sure they go to correct legs!!
    lift_leg(2)
    lift_leg(5)#check to see if this is the right angle addition to make it work

    ## move front legs one at a time
    move_leg_forward_WALL(1)
    move_leg_forward_WALL(4)
    ## waddle




    ## move back legs one at a time

