

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
#dot = (x / 80).astype(int)*80
dot = np.zeros(frame_amount)
n=20
for i in range(0,frame_amount):
    if i == n:
        dot[i] = x[n]
        n = n +20
    else:
        dot[i] = x[n-20]
        
#dot = np.arange(x[0],x[-1]+1,80)
#dot = np.repeat(dot,20)[:len(x)]

doty = dot/200
op = False

def update_plot(num):
    global op
    plane_trajectory.set_data(dot[0:num],doty[0:num])
    
    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]])
    
    stopwatch0.set_text('{:.2f} hrs'.format(t[num]))
    dist_counter0.set_text('{:n} km'.format(x[num]))
    
    if ( doty[num] - y[num] > -0.1 ):
        if op:        
            return plane_trajectory
        else:
            plane_trajectory.set_data(dot[0:num+1],doty[0:num+1])
            op = True
    
    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,\
            stopwatch0,dist_counter0

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)


# Subplot 1
ax0 = fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9) )

# Line following the airplane
plane_trajectory, = ax0.plot([],[], 'r:o', lw=2)

# Airplane lines
plane_1, = ax0.plot([],[], 'k', lw=10)
plane_2, = ax0.plot([],[], 'k', lw=5)
plane_3, = ax0.plot([],[], 'k', lw=5)
plane_4, = ax0.plot([],[], 'k', lw=3)
plane_5, = ax0.plot([],[], 'k', lw=3)

# Draw houses
house_1 = ax0.plot([100,100],[0,1],'k',lw=7)
house_2 = ax0.plot([300,300],[0,1],'k',lw=7)
house_3 = ax0.plot([700,700],[0,.7],'k',lw=15)
house_4 = ax0.plot([900,900],[0,.9],'k',lw=10)
house_5 = ax0.plot([1300,1300],[0,1],'k',lw=25)

# Text information hrs and km
box_object = dict(boxstyle="square",fc=(0.9,0.9,0.9),ec='r',lw=1)
stopwatch0 = ax0.text(1400,0.65,'',size=15,color='g',bbox = box_object)

box_object2 = dict(boxstyle="square",fc=(0.9,0.9,0.9),ec='g',lw=1)
dist_counter0 = ax0.text(1000,0.5,'',size=15,color='r',bbox = box_object2)





plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)
plt.xticks(np.arange(x[0],x[-1]+1,x[-1]/4),size=15)
plt.yticks(np.arange(0,y[-1]+2),size=15)


ax0.set_title('Airplane',fontsize=20)
ax0.set_xlabel('Distance [km]',fontsize=15)
ax0.set_ylabel('Altitude [km]',fontsize=15)
plt.grid(True)
#ax0.set_xlim([0,800*t_end])
#ax0.set_ylim([0,4])


plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, 
                                    interval=10,repeat=True,blit=True)

plt.show()


