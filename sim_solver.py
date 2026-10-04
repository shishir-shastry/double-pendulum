import numpy as np
import scipy.integrate as sp
import diff_equations as eq

def solve_de(theta1_0, omega1_0, theta2_0, omega2_0, l1, l2, g, m1, m2, t_span, intervals):
    #solve the differential equation for pendulum in diff_equations.py numerically
    #and return times, angular displacements and angular velocities
    #theta1_0 - initial angle for pendulum bob m1 in radians
    #omega1_0 - initial angular velocity for pendulum bob m1 in rad/s
    #theta2_0 - initial angle for pendulum bob m2 in radians
    #omega2_0 - initial angular velocity for pendulum bob m2 in rad/s
    #l1, l2 - length of each massless rod holding the masses m1 and m2 respectively in metres
    #g - acceleration due to gravity in m/s^2
    #m1, m2 - masses of the teo pendulum bobs in kg
    #t_span - time in seconds over which to integrate
    #intervals - number of discrete time points to store in array
    
    #initialise times and set the initial conditions
    t = np.linspace(0, t_span, intervals)
    y0 = [theta1_0, theta2_0, omega1_0, omega2_0]
    
    sol = sp.solve_ivp(eq.diff_eq_setup, (0,t_span), y0, args=(l1,l2,g,m1,m2), t_eval=t)
    
    return sol