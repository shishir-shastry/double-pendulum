import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sim_solver as sim


#set initial values for all parameters needed in solve_de
theta1_0 = 2*np.pi/3  #rad
theta2_0 = 2*np.pi/3  #rad
omega1_0 = 0 #rad/s
omega2_0 = 0 #rad/s
l1 = 1 #m
l2 = 0.5 #m
g = 9.81 #m/s^2
m1 = 2 #kg
m2 = 1 #kg
t_span = 20 #s
intervals = 400 #no unit

sol = sim.solve_de(theta1_0, omega1_0, theta2_0, omega2_0, 
                                                 l1, l2, g, m1, m2, t_span, intervals)
t = sol.t
theta1 = sol.y[0]
theta2 = sol.y[1]
omega1 = sol.y[2]
omega2 = sol.y[3]

fig, ax_pendulum = plt.subplots()
ax_pendulum.set_xlim(-3,3)
ax_pendulum.set_ylim(-3,3)

#defining points and lines to correspond to the rods and bobs of the double pendulum to animate
pendulum_line1, = ax_pendulum.plot([], [], '-', color='green')
pendulum_line2, = ax_pendulum.plot([], [], '-', color='blue')
pendulum_bob1, = ax_pendulum.plot([], [], 'o', markersize=6, color='green')
pendulum_bob2, = ax_pendulum.plot([], [], 'o', markersize=6, color='blue')

def update(i):
    #for each frame i, set the line segment and point for animation
    
    #set pendulum position for first mass
    x1 = l1*np.sin(theta1[i])
    y1 = -l1*np.cos(theta1[i])
    pendulum_line1.set_data([0,x1],[0,y1])
    pendulum_bob1.set_data([x1],[y1])
    
    #set pendulum position for second mass
    x2 = x1 + l2*np.sin(theta2[i])
    y2 = y1 - l2*np.cos(theta2[i])
    pendulum_line2.set_data([x1,x2],[y1,y2])
    pendulum_bob2.set_data([x2],[y2])
    
    return pendulum_line1, pendulum_bob1, pendulum_line2, pendulum_bob2

anim = FuncAnimation(fig=fig, func=update, frames=intervals, interval=30, blit=True)

#plt.plot(t, theta1)
plt.show()