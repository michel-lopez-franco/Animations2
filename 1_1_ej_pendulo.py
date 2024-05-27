
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


# En este ejemplo quiero hacer una animacion de una senoidal 

t_init = 0
t_end = 10
dt = 0.01

t = np.arange(0,t_end+dt,dt)
x = t
y = np.sin(t)
dotx = np.zeros(len(t))

#plt.plot(x,y)
#plt.scatter(x[0],y[0],c='red',s=100) # Es lo que quiero animar

def update_plot(num):
    line.set_data(x[0:num],y[0:num])
    dot.set_data(x[num-1:num],y[num-1:num])
    dot2.set_data(dotx[num-1:num],y[num-1:num])
    resorte.set_data([0,0],[1,0+y[num]])

    return line, dot,dot2,resorte

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
#gs = gridspec.GridSpec(3,3)
gs = gridspec.GridSpec(2,2)

ax0 = fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9) )
line, = ax0.plot([],[], c='blue', lw=2)
dot, = ax0.plot([],[], 'o', c='red', lw=100)
ax0.set_xlim(x[0],x[-1])
ax0.set_ylim(-1.5,1.5)

ax1 = fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9) )
ax1.hlines(0,-1,1, color='black')
#ax1.vlines(0,-1,1, color='black')
resorte, = ax1.plot([],[], c='blue', lw=2)
dot2, = ax1.plot([],[], 'o', c='red', lw=100)
ax1.set_xlim(-1,1)
ax1.set_ylim(-1,1)

plane_ani =  animation.FuncAnimation(fig, update_plot, frames=len(t), 
                                     interval=10, repeat=True, blit=True)
#plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, 
#                                    interval=5,repeat=False,blit=True)

plt.show()


