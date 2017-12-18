# -*- coding: utf-8 -*-
"PROBLEM SHEET 7"
"Exercise 1"
import matplotlib.pyplot as plt
#Solving differential equation: x''=−4x−0.2x'
#for t from 0 to 20 with the initial conditions x(0)=0 and x'(0)=5
tlist=[]
xlist=[]
vlist=[]            #where v=first derivative of x
alist=[]            #where a=second derivative of x
#Setting initial conidtions
t= 0.0
dt= 0.001   #time step
x= 0.0
v= 5.0
tf= 20.0
k= 4.0
l= 0.2
#Appending initial values to the lists
tlist.append(t)
xlist.append(x)
vlist.append(v)
#Inside of a loop using equations:
#x'(t + ∆t) ≈ x'(t) + x''(t)∆t and x(t + ∆t) ≈ x(t) + x''(t + ∆t)∆t
while t<tf:
    a=-k*x-l*v
    v=v+a*dt
    x=x+v*dt
    t=t+dt
#Appending the new values to the lists
    tlist.append(t)
    xlist.append(x)
    vlist.append(v)
#Plotting the results (position vs time)
plt.figure
plt.plot(tlist, xlist, ls='-', c='r')
plt.xlabel('time')
plt.ylabel('position')
plt.show()
"Exercise 2"
from mpl_toolkits.mplot3d import Axes3D
"""
The following example traces the movement of a charged particle under the influence of electric and
magnetic fields. Here it'ss used the Euler's method which has to be compared with the Runge-Kutta's method.
"""
Ex = 0.0 #  X Component of applied Electric Field
Ey = 2.0
Ez = 0.0
Bx = 0.0 # X Component of applied Magnetic field
By = 0.0
Bz = 4.0
m = 2.0 # Mass of the particle
q = 5.0 # Charge
x = 0.0 # initial position x
y = 0.0 # initial position y
z = 0.0 # initial position z
vx = 20.0 # initial velocity vx
vy = 10.0 # initial velocity vy
vz = 2.0 # initial velocity vz
a = []
b = []
c = []
t = 0.0
dt = 0.01
while t < 10: # trace path until time reaches value e.g. 10
    Fx = q * (Ex + (vy * Bz) - (vz * By) )
    vx = vx + Fx/m * dt # Acceleration = F/m; dv = a.dt
    Fy = q * (Ey - (vx * Bz) + (vz * Bx) )
    vy = vy + Fy/m * dt
    Fz = q * (Ez + (vx * By) - (vy * Bx) )
    vz = vz + Fz/m * dt
    x = x + vx * dt
    y = y + vy * dt
    z = z + vz * dt
    a.append(x)
    b.append(y)
    c.append(z)
    t += dt

fig=plt.figure()
ax = Axes3D(fig)
ax.set_title("Path of charged particle under influence of electric and magnetic fields - Euler's Method")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot3D(a,b,c, color='blue', label='path')
ax.legend(loc='lower left')

plt.show()
#Plotitng the path of a charged particle (with initial position and velocity) 
#under the influence of external magnetic and electric fields
#Components of applied Electric Field
Ex = 0.0 
Ey = 2.0 
Ez = 0.0 
#Components of applied Magnetic field
Bx = 0.0 
By = 0.0 
Bz = 4.0
m = 2.0 #Mass of the particle 
q = 5.0 #Charge
x = 0.0 #initial position x
y = 0.0 #initial position y
z = 0.0 #initial position z
vx= 20.0 #initial velocity vx
vy = 10.0 #initial velocity vy
vz = 2.0 #initial velocity vz
a=[]
b=[]
c=[]
t = 0.0
dt = 0.01
while t < 30: #increasing time interval to see how errors vary with time
    Fx =q*(Ex+(vy*Bz)-(vz*By))
    vx =(vx + ((Fx/m) *dt))         #Acceleration=F/m; dv=a*dt
    Fy =q*(Ey-(vx*Bz)+(vz*Bx)) 
    vy =vy+((Fy/m)*dt)
    Fz =q*(Ez+(vx*By)-(vy*Bx))
    vz =vz +((Fz/m)*dt)
#Because in the code x,y,z depend on Fx,Fy,Fz I realized that applying the RK4 method
#direclty to the position (without defining a new function for the force) works.
#To apply the RK4 method defining values of k for y and of l for x
    k1=dt*(x+vx*dt)
    k2=dt*((x+dt/2)+((vx*dt)+k1/2))
    k3=dt*((x+dt/2)+((vx*dt)+k2/2))
    k4=dt*((x+dt)+((vx*dt)+k3))
    l1=dt*(y+vy*dt)
    l2=dt*((y+dt/2)+((vy*dt)+l1/2))
    l3=dt*((y+dt/2)+((vy*dt)+l2/2))
    l4=dt*((y+dt)+((vy*dt)+l3))
    z =z+vz*dt          #the expression for z doesn't have to be modified as RK4 includes only x,y 
#Appending the modified variables x, y to the lists
    a.append(k1/6+k2/3+k3/3+k4/6)
    b.append(l1/6+l2/3+l3/3+l4/6)
    c.append(z)
    t+= dt
#Plotting figure and adding labels to the plot
fig=plt.figure()
ax = Axes3D(fig)
ax.set_title ("Path of charged particle under influence of electric and magnetic fields- Runge-Kutta's method")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot3D(a,b,c, color='blue', label='path') 
ax.legend(loc='lower left')
plt.show()
#Hence from comparing the two graphs is evident that using the Runge-Kutta's method reduces the error 
#and gives a more accurate result than using Euler's method
"Exercise 3"
from numpy import mgrid , array , sqrt 
import mayavi.mlab as mlab
#Vector field calculated and plotted in the x,y plane
#3D mesh grid which ranges from −100 to 100 in x,y coordinates, with intersections at every 20th value
#making the range for z from -0.1 to 0.1 in order to make the z component negligible
x,y,z = mgrid[-100.:101.:20., -100.:101.:20., -0.1:0.1:20.]
#Store the coordinates of the charge as a vector (array)
# This is to get the best possible symmetry in this specific field 
qpos = array ([10. ,10. ,0])
#The magnitude of the charge 
qcharge = 1.0
# Creating a grid for the electric field . This has the size of # x,y and z, but all the values are now set to zero.
Ex, Ey, Ez = x*0, y*0, z*0
# Calculating the x, y and z distance to the charge at every point in the grid :
rx = x - qpos[0] 
ry=y-qpos[1] 
rz = z - qpos[2]
# Calculating the distance at every point in the grid :
r = sqrt(rx**2 + ry**2 + rz**2)
# Calculating the field for each component at every point in the grid :
Ex = (qcharge / r**2) * (rx / r)
Ey = (qcharge / r**2) * (ry / r) 
Ez = (qcharge / r**2) * (rz / r)
#Drawing the vector field in 3D 
mlab.quiver3d (x,y,z,Ex,Ey,Ez)
#Adding axes labels and title 
mlab.axes(ranges=(-100, 101, -100, 101, 0, 0), xlabel='X', ylabel='Y', zlabel = '', z_axis_visibility = False )
mlab.title('2D Vector Field around a point charge at 10,10,0')
#All the plots have been saved manually as .png files