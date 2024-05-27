

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up the duration for you animation
t0 = 0 # [hrs]
t_end = 2 # [hrs]
dt = 0.005 # [hrs]

# Create array for time
t = np.arange(t0,t_end + dt,dt)
x = 800*t
altitude = 2 # [km]
y = np.ones(len(t))*altitude

################### Animation ###################
frame_amount = len(t)
#interval = 50 # [ms] go to the next frame every 50 ms

def update_plot(num):
    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_1.set_data([400+num,800+num],[2,2])

    return plane_trajectory,plane_1 # plane_1,plane_trajectory#

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)


# Subplot 1
ax0 = fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9) )
plane_trajectory, = ax0.plot([],[], c='blue', lw=2)
plane_1, = ax0.plot([],[], 'k', lw=10)

plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)

ax0.set_title('Airplane')
ax0.set_xlabel('Distance [km]')
ax0.set_ylabel('Altitude [km]')
#ax0.set_xlim([0,800*t_end])
#ax0.set_ylim([0,4])


plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, 
                                    interval=5,repeat=False,blit=True)

plt.show()

