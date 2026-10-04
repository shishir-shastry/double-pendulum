import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sim_solver as sim


#set initial values for all parameters needed in solve_de
theta1_0 = np.pi/12 #rad
theta2_0 = np.pi/2 #rad
omega1_0 = 0 #rad/s
omega2_0 = 0 #rad/s
l1 = 1 #m
l2 = 0.5 #m
g = 9.81 #m/s^2
m1 = 2 #kg
m2 = 1 #kg
t_span = 10 #s
intervals = 250 #no unit

sol = sim.solve_de(theta1_0, omega1_0, theta2_0, omega2_0, 
                                                 l1, l2, g, m1, m2, t_span, intervals)
t = sol.t
theta1 = sol.y[0]
theta2 = sol.y[1]
omega1 = sol.y[2]
omega2 = sol.y[3]

plt.plot(t, theta1)
plt.show()