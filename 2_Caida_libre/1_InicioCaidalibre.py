import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import numpy as np


# time array
t0 = 0 
t_end = 12
dt = 0.02
t = np.arange(t0, t_end+dt, dt)

# gravitational acceleration
g_Earth = -9.8 #m/s^2
g_Mars = -3.7 #m/s^2
g_Moon = -1.6 #m/s^2

# position y arrays
n =2 
y_i = 100 #m
y_Earth = y_i + 0.5*g_Earth*t**2
y_Mars = y_i + 0.5*g_Mars*t**2
y_Moon = y_i + 0.5*g_Moon*t**2

# velocity y arrays
y_Earth_velocity = n*0.5*g_Earth*t**(n-1)
y_Mars_velocity = n*0.5*g_Mars*t**(n-1)
y_Moon_velocity = n*0.5*g_Moon*t**(n-1)

# acceleration y arrays
#y_Earth_acceleration = (n-1)*0.5*g_Earth*t**(n-2)
y_Earth_acceleration = (n-1)*g_Earth*t**(n-2)
y_Mars_acceleration = (n-1)*g_Mars*t**(n-2)
y_Moon_acceleration = (n-1)*g_Moon*t**(n-2)


def create_circle(r):
    degrees= np.arange(0,361,1)
    radians = degrees*np.pi/180 #np.radians(degrees)
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y

radius = 20
sphere_x_Earth, sphere_y_Earth = create_circle(radius)
sphere_x_Mars, sphere_y_Mars = create_circle(radius)
sphere_x_Moon, sphere_y_Moon = create_circle(radius)

#np.set_printoptions(precision=2, suppress=True)
#print(sphere_x_Earth)
# print(sphere_y_Earth)
# exit()

##################### Animation #####################   
frame_amount = len(t)
width_ratio = 1.2
y_f = -10 #m
dy = 10 #m

def update_plot(num):
    
    if ( (y_Earth[num]) >= radius):
        sphere_Earth.set_data(sphere_x_Earth,sphere_y_Earth+y_Earth[num])
        alt_E.set_data(t[:num],y_Earth[:num])
        vel_E.set_data(t[:num],y_Earth_velocity[:num])
        acc_E.set_data(t[:num],y_Earth_acceleration[:num])
        
        sphere_Mars.set_data(sphere_x_Mars,sphere_y_Mars+y_Mars[num])
        alt_Ma.set_data(t[:num],y_Mars[:num])
        vel_Ma.set_data(t[:num],y_Mars_velocity[:num])
        acc_Ma.set_data(t[:num],y_Mars_acceleration[:num])
        
        sphere_Moon.set_data(sphere_x_Moon,sphere_y_Moon+y_Moon[num])
        alt_Mo.set_data(t[:num],y_Moon[:num])
        vel_Mo.set_data(t[:num],y_Moon_velocity[:num])
        acc_Mo.set_data(t[:num],y_Moon_acceleration[:num])
        
    return  sphere_Earth, alt_E, vel_E, acc_E, \
            sphere_Mars, alt_Ma, vel_Ma, acc_Ma, \
            sphere_Moon, alt_Mo, vel_Mo, acc_Mo


fig = plt.figure(figsize=(16, 9),dpi=120,facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3, 4)


# Create object for Eart
ax0 = fig.add_subplot(gs[:,0],facecolor=(0.9,0.9,0.9))
sphere_Earth, = ax0.plot([],[],'k',lw=3)
land_Earth, = ax0.plot([-radius*width_ratio,radius*width_ratio],[-5,-5],lw=38)

plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_f,y_i+dy,dy))
plt.ylabel('Altura [m]')
#plt.xlabel('Distancia [m]')
plt.title('Tierra')

# Create object for Mars
ax1 = fig.add_subplot(gs[:,1],facecolor=(0.9,0.9,0.9))
sphere_Mars, = ax1.plot([],[],'k',lw=3)
land_Mars, = ax1.plot([-radius*width_ratio,radius*width_ratio],[-5,-5],'orangered',lw=38)

plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_f,y_i+dy,dy))
#plt.ylabel('Altura [m]')
#plt.xlabel('Distancia [m]')
plt.title('Mars')

# Create object for Moon
ax2 = fig.add_subplot(gs[:,2],facecolor=(0.9,0.9,0.9))
sphere_Moon, = ax2.plot([],[],'k',lw=3)
land_Moon, = ax2.plot([-radius*width_ratio,radius*width_ratio],[-5,-5],'gray',lw=38)

plt.xlim(-radius*width_ratio, radius*width_ratio)
plt.ylim(y_f,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_f,y_i+dy,dy))
#plt.ylabel('Altura [m]')
#plt.xlabel('Distancia [m]')
plt.title('Moon')


# Create position function
ax3 = fig.add_subplot(gs[0,3],facecolor=(0.9,0.9,0.9))
alt_E, =  ax3.plot([],[],'',lw=3,label='Alt_Earth'+str(y_i)+' +('+str(round(g_Earth/2,1))+')t^'+str(n)+' [m]' )
alt_Ma, = ax3.plot([],[],'orangered',lw=3,label='Alt_Mars'+str(y_i)+' +('+str(round(g_Earth/2,1))+')t^'+str(n)+' [m]' )
alt_Mo, = ax3.plot([],[],'gray',lw=3,label='Alt_Moon'+str(y_i)+' +('+str(round(g_Earth/2,1))+')t^'+str(n)+' [m]' )

plt.xlim(0,t_end)
plt.ylim(0,y_i)
plt.legend(loc=(0.6,0.7),fontsize='x-small')



# Create velocity function 
ax4 = fig.add_subplot(gs[1,3],facecolor=(0.9,0.9,0.9))
vel_E, = ax4.plot([],[],'',lw=3,label='Vel_Earth ='+ str(g_Earth)+ "t [m/s]" )
vel_Ma, = ax4.plot([],[],'orangered',lw=3,label='Vel_Mars ='+ str(g_Earth)+ "t [m/s]" )
vel_Mo, = ax4.plot([],[],'gray',lw=3,label='Vel_Moon ='+ str(g_Earth)+ "t [m/s]" )

plt.xlim(0,t_end)
plt.ylim(y_Earth_velocity[-1],0)
plt.legend(loc='lower left',fontsize='x-small')


# Create acceleration function
ax5 = fig.add_subplot(gs[2,3],facecolor=(0.9,0.9,0.9))
acc_E, = ax5.plot([],[],'',lw=3,label='Acc_Earth ='+ str(g_Earth)+ " [(m/s)/s = m/s^2]" )
acc_Ma, = ax5.plot([],[],'orangered',lw=3,label='Acc_Mars ='+ str(g_Earth)+ " [(m/s)/s = m/s^2]" )
acc_Mo, = ax5.plot([],[],'gray',lw=3,label='Acc_Moon ='+ str(g_Earth)+ " [(m/s)/s = m/s^2]" )

plt.xlim(0,t_end)
plt.ylim(g_Earth-1,0)
plt.legend(loc=(0.02,0.25),fontsize='x-small')



plane_ani = animation.FuncAnimation(fig, update_plot, \
                    frame_amount,interval=10, repeat=True, blit=True)

print("Animation is running... ")

plt.show()

print("Animation is done!")
exit()




