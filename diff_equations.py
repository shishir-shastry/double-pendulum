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
    
    #the standard differential equations are couples with domega1_dt and domega2_dt
    #appearing in both.
    #by writing the equations in terms of matrices, the inverse can be used to
    #find expressions for domega1_dt and domega2_dt
    
    matrix = np.array([[(m1+m2)*l1, m2*l2*np.cos(delta)], [l2, l1*np.cos(delta)]])
    final_vector = np.array([-m2*l2*omega2**2*np.sin(delta) - (m1+m2)*g*np.sin(theta1), 
                             l1*omega1**2*np.sin(delta) - g*np.sin(theta2)])
    final_vector = np.reshape(final_vector, (2,1))
    
    #initial_vector is a column vector with [domega1_dt, domega2_dt]
    initial_vector = np.dot(np.linalg.inv(matrix), final_vector)
    domega1_dt =  initial_vector[0,0]
    domega2_dt = initial_vector[1,0]
    
    return [dtheta1_dt, dtheta2_dt, domega1_dt, domega2_dt]