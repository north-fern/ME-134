#gait eqns


import math
import numpy as np
## geometric paramets of leg and platform, see figure 4 for geometry

#legnth of legs
l1 = 0 
l2 = 0
l3 = 0
#half width and half height of platform?
a = 0
b = 0
#height of COG
h = 0
# landpark linked to center of gravity. location is calculated to benchmark base R using homogeneous transformation

Ro = 0

# displacement value of center of gravity for sample walk

lam0 = 0

#vector of coordinate of the leg food with repect to R

P1
P2
P3

P = [[P1], [P2], [P3]]

## vector coords of food of leg with respect to R0
pp1
pp2
pp3

pp = [[pp1],[pp2],[pp3]]

#starting point of cycloid with repect to R

pp0  

#end point of cycloid with respect to R

ppn

#string of cycloid measured in same plane
lam00

#period of gait cycle
N

#simple index splint interval N
s

#initialize leg locations with repect to CoG of platform

P01 = [[0],[l2+a],[-h],[1]]
P02 = [[-b],[-l2-a],[-h],[1]]
P03 = [[b],[-l2-a],[-h],[1]]
P04 = [[0],[-l2-a],[-h],[1]]
P05 = [[b],[l2+a],[-h],[1]]
P06 = [[-b],[l2+a],[-h],[1]]

'''
creating equation of motion for platofrm center of grav
'''

## f(t) is a function of time!
X = 0 
#g(x) the vertial acis of CoG may be a func of time and x
Y = 0

#height of cog, can be fixed or variable with x and y
Z = h

#make sure its deriv. of Y!
theta0 = math.arctan(Y)

#distance covered by center of gravity
d = math.sqrt(x**2+y**2)

#overall angle of rotation around z axis of reference
beta = math.arctan(y/x)

#angle of rotation around x0 axis of platform
alpha = 0


'''
motion of legs
'''

# 0--> j aka i, 1---> i aka i-1
def ROT_i_to_j(theta0, theta1, X0, X1, Y0, Y1, p1, p2, p3, p4, p5, p6):
    matrx = [[math.cos(theta0-theta1) -math.sin(theta0-theta1) 0 0],[math.sin(theta0-theta1) math.cos(theta0-theta1) 0 0],[0 0 1 0],[0 0 0 1]]
    lam0 = math.sqrt((X0-X1)**2 + (Y0-Y1)**2)
    lamtransmat = [[1 0 0 -lam0],[0 1 0 0],[0 0 1 0],[0 0 0 1]]
    interim = np.matmul(matrx, lamtransmat)
    pj1 = mp.matmul(intterim, p1)
    pj2 = mp.matmul(intterim, p2)
    pj3 = mp.matmul(intterim, p3)
    pj4 = mp.matmul(intterim, p4)
    pj5 = mp.matmul(intterim, p5)
    pj6 = mp.matmul(intterim, p6)
    return pj1, pj2, pj3, pj4, pj5, pj6


'''
motion of legs in air
'''

#takeoff & Landing

# for landind, use betan/2, hn/2, dn/2, thetan/2, and p0j

def takeoff(beta0, theta0, d0, h0, p1, p2, p3, p4, p5, p6):

    rotbeta0 = [[math.cos(beta0 - theta0) -sin(beta0 - theta0) 0 0],[math.sin(beta0 - theta0) math.cos(beta0 - theta0) 0 0],[0 0 1 0],[0 0 0 1]]
    rotbetatheta = [[math.cos(beta0 - theta0) -sin(beta0 - theta0) 0 0],[math.sin(beta0 - theta0) math.cos(beta0 - theta0) 0 0],[0 0 1 0],[0 0 0 1]]
    dtransmat = [[1 0 0 d0],[0 1 0 0],[0 0 1 0],[0 0 0 1]]
    htransmat = [[1 0 0 h0],[0 1 0 0],[0 0 1 0],[0 0 0 1]]
    intermediate = np.matmul(rotbeta0, htransmat)
    nextstep = np.matmul(intermediate,dtransmat)
    nextstep2 = np.matmul(nextstep, rotbetatheta)
    poj1 = np.matmul(nextstep2, p1)
    poj2 = np.matmul(nextstep2, p2)
    poj3 = np.matmul(nextstep2, p3)
    poj4 = np.matmul(nextstep2, p4)
    poj5 = np.matmul(nextstep2, p5)
    poj6 = np.matmul(nextstep2, p6)
    return poj1, poj2, poj3, poj4, poj5, poj6



#intermediate points

## traveled distances lam00

def travel_dist(ppn, pp0):
    ppnx = ppn[0]
    ppny = ppn[1]
    pp0x = pp0[0]
    pp0y = pp0[1]
    lam = math.sqrt((ppnx - pp0x)**2 + (ppny - pp0y)**2)
    








