
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

#print(t)
#print("#"*50)
#print(len(t))
#exit()

# Create an x array
x = 800*t

# Create an y array
altitude = 2 # [km]
y = np.ones(len(t))*altitude

#animation.FuncAnimation(fig,update,frames,timeinterval,repeat,blit)
#plane_ani = animation.FuncAnimation(fig, update, frames=100, fargs=(data, line), interval=50)

################### Animation ###################
frame_amount = len(t)
#interval = 50 # [ms] go to the next frame every 50 ms


# Take care of num argument in update_plot
# This argument is the frame number. It is used to update the plot
# with the next frame of data.
# It has tow 0,0 in the beginning   
# num = [0,0,0,1,2,3,...,frame_amount-1] 
# if repeat is True, then num will be like this:
# num = [0,0,0,1,2,3,...,frame_amount-1, 0,0,1,2,3,...,frame_amount-1, 0,0,1,2,3,...,frame_amount-1,...] 
# only add one 0 in the beginning
def update_plot(num):
    #print(num)
    #print(t[0:num])
    #line, = ax0.plot(x[0:num],y[0:num], 'o', c='blue', lw=1)

    plane_trajectory.set_data(x[0:num],y[0:num])

    return plane_trajectory, # check this line with and without the comma

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)


# Subplot 1
#ax0 = plt.subplot(gs[0,:],facecolor=(0.9,0.9,0.9) )
ax0 = fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9) )
plane_trajectory, = ax0.plot([],[], c='blue', lw=2)
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