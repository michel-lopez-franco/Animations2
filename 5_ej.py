

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up the duration for you animation
t0 = 0 # [hrs]
t_end = 2 # [hrs]
dt = 0.005 # [hrs]

# Create array for time
speed = 1
t = np.arange(t0,t_end + dt,dt)
x = speed*800*t
altitude = 2 # [km]
y = np.ones(len(t))*altitude

# Speed in the x direction
speed_x = np.ones(len(t))* 800 # [km/hr]

################### Animation ###################
frame_amount = int(len(t) /speed)
#interval = 50 # [ms] go to the next frame every 50 ms
#dot = (x / 80).astype(int)*80
dot = np.zeros(frame_amount)

n_init = int(20 / speed)
n= n_init
for i in range(0,frame_amount):
    if i == n:
        dot[i] = x[n]
        n = n + n_init
    else:
        dot[i] = x[n-n_init]
        
#dot = np.arange(x[0],x[-1]+1,80)
#dot = np.repeat(dot,20)[:len(x)]
#doty = dot/1000


def update_plot(num):
    
    # 1st subplot
    plane_trajectory.set_data(dot[0:num],y[0:num])
    
    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]])
    
    vertical_line_plane.set_data([x[num],x[num]],[0,y[num]])
    
    stopwatch0.set_text('{:.2f} hrs'.format(t[num]))
    dist_counter0.set_text('{:n} km'.format(x[num]))
    
    # 2nd subplot
    x_dist.set_data(t[0:num],x[0:num])
    vertical_line.set_data([t[num],t[num]],[0,x[num]])
    horinzontal_line.set_data([t[0],t[num]],[x[num],x[num]])
    
    # 3rd subplot
    #speed.set_data(t[0:num],speed_x[0:num])
    speed.set_data([0,t[num]],[speed_x[num], speed_x[num] ] )
    vertical_line_speed.set_data([t[num],t[num]],[0,speed_x[num]])
    
    if num != 0:
        division_x_dist.set_text(str(int(x[num])))
        division_time.set_text(str(round(t[num],3) ))
        division_speed.set_text("= "+str( int( round(x[num]/t[num], 1) ) ) +" km/hr" )
    
    #division_x_dist
    #division_time_dist
    
    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,\
            stopwatch0,dist_counter0,x_dist,vertical_line,horinzontal_line,\
            vertical_line_plane,speed,vertical_line_speed, \
            division_x_dist,division_time,division_speed

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

# Draw line
vertical_line_plane, = ax0.plot([],[],'k:o',lw=2,label='vertical line')

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

# Set up the plot

plt.xlim(x[0],x[-1]/speed)
plt.ylim(0,y[0]+1)
plt.xticks(np.arange(x[0],x[-1]/speed+1,(x[-1]/speed)/4),size=15)
plt.yticks(np.arange(0,y[-1]+2),size=15)
ax0.set_title('Airplane',fontsize=20)
ax0.set_xlabel('Distance [km]',fontsize=15)
ax0.set_ylabel('Altitude [km]',fontsize=15)
plt.grid(True)
#ax0.set_xlim([0,800*t_end])
#ax0.set_ylim([0,4])


# Subplot 2
ax2 = fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9) )

x_dist, = ax2.plot([],[],'-b',lw=3,label='X=800*t')
horinzontal_line, = ax2.plot([],[],'r:o',lw=2,label='horizontal line')
vertical_line, = ax2.plot([],[],'g:o',lw=2,label='vertical line')

plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1])
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4))
plt.yticks(np.arange(x[0],x[-1]+1,x[-1]/4))
plt.xlabel("time [hrs]",fontsize=15)
plt.ylabel("x-distance [km]",fontsize=15)
plt.title("Distance vs Time", fontsize=15)
plt.grid(True)
plt.legend(loc='upper left',fontsize='x-large')


# Subplot 3
ax4 = fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9) )
speed, = ax4.plot([],[],'-b',lw=3,label='FUNCTION: $ \\frac{\Delta X}{\Delta t}$ = 800')
vertical_line_speed, = ax4.plot([],[],'b:o',lw=2)
division_line = ax4.plot([0.08,0.37],[995,995],'k',linewidth=1)
#division_x_dist = ax4.text(0.4,995,'$\\frac{800}{1}$',fontsize=15)
division_x_dist = ax4.text(0.1,1015,'',fontsize=20,color='r')
division_time = ax4.text(0.1,865,'',fontsize=20,color='g')
division_speed = ax4.text(0.4,950,'',fontsize=20,color='b')


plt.xlim(t[0],t[-1])
plt.ylim(x[0],speed_x[-1]*2)
plt.xticks(np.arange(t[0],t[-1]+dt,t[-1]/4),size=10)
plt.yticks(np.arange(0,speed_x[-1]*2+1,speed_x[-1]*2/4),size=10)
plt.xlabel("time [hrs]",fontsize=15)
plt.ylabel("x-distance [km]",fontsize=15)
plt.title("Speed as a function of time", fontsize=15)
plt.grid(True)
plt.legend(loc='upper right',fontsize='x-large')



plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, 
                                    interval=2,repeat=True,blit=True)

plt.show()


