import numpy as np

def diff_eq_setup(t, y, l1, l2, g, m1, m2):
    #define the couple differential equations for a simple double pendulum
    #a simple double pendulum has massless rods
    #t - time in seconds that allows solve_ivp to call the function at each time step
    #y - an array of vectors where each vector is [theta1, theta2, omega1, omega2].
    #theta1, theta2 - angles between each pendulum and vertical in radians
    #omega1, omega2 - the angular velocity of each pendulum in rad/s
    #l1, l2 - length of each massless rod holding the masses m1 and m2 respectively in metres
    #g - acceleration due to gravity in m/s^2
    #m1, m2 - masses of the teo pendulum bobs in kg
    
    theta1, theta2, omega1, omega2 = y
    delta = theta1 - theta2
    
    dtheta1_dt = omega1
    dtheta2_dt = omega2
    
