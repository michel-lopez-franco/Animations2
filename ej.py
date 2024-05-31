
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

t0 = 0 # [hrs]
t_end = 2 # [hrs]
dt = 0.005 # [hrs]

t = np.arange(t0,t_end + dt,dt)
x = 800*t

altitude = 2 # [km]
y = np.ones(len(t))*altitude


################### Animation ###################
frame_amount = len(t)

def update_plot(num):
    #print(num)
    #print(t[0:num])
    #line, = ax0.plot(x[0:num],y[0:num], 'o', c='blue', lw=1)

    #plane_trajectory.set_data(x[0:num],y[0:num])
    
    plane_trajectory.set_data([0,x[num]],[0,y[num]] )
    
    

    return plane_trajectory, # check this line with and without the comma

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Subplot 1
ax0 = fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9) )
plane_trajectory, = ax0.plot([],[], c='blue', lw=2)
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)

ax0.set_title('Airplane')
ax0.set_xlabel('Distance [km]')
ax0.set_ylabel('Altitude [km]')

plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, 
                                    interval=5,repeat=False,blit=True)

plt.show()