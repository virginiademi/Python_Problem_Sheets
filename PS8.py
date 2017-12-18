# -*- coding: utf-8 -*-
"PROBLEM SHEET 8"
"Question 1"
#Defining a class for the velocity profile of a fluid through a pipe
class VelocityProfile:
    """
    Mathematical function for the velocity profile of a fluid through a pipe
    Methods:
    constructor(R, beta, mu0, n): set initial radius, pressure gradient, 
    viscosity coefficient and viscous properties given by n
    value(r): compute the velocity as a function of r
    formula(): print out the formula for the velocity
    Attributes:
    R:the radius of the pipe
    beta: the pressure gradient
    mu0: the viscosity coefficient
    n: real number reflecting the viscour properties (n=1 for water and air)
    r: distance from the centerline (r=0 is the centerline, r=R is the pipe wall)
    Usage:
    >>>v= Velocity Profile(1,0.06,0.02,0.1)
    >>>velocity1=v.value(0)
    >>>velocity2=v.value(1)
    >>>print v.formula()
    ((beta/2*mu0)**1/n)*(n/(n+1))*(R**(1+(1/n))-r**(1+(1/n)))
    """
    def __init__(self, R, beta, mu0, n):    
        self.R=R
        self.beta=beta
        self.mu0=mu0
        self.n=n
    def value (self, r):
        return ((self.beta/2*self.mu0)**1/self.n)*(self.n/(self.n+1))*(self.R**(1+(1/self.n))-r**(1+(1/self.n)))
    def formula(self):
        return '((beta/2*mu0)**1/n)*(n/(n+1))*(R**(1+(1/n))-r**(1+(1/n))); R=%g' %self.R, 'beta=%g' %self.beta, 'mu0=%g' %self.mu0, 'n=%g' %self.n
#Evaluating the instance velocity as a function of position 
#First parameters: R=1, beta=0.06, mu0=0.02, n=0.1
v=VelocityProfile(1,0.06,0.02,0.1)
velocity1=v.value(0)
velocity2=v.value(1)
print v.formula()
print 'The velocity of the fluid at the center of the pipe is %g' %velocity1, 'at the wall of the pipe is %g' %velocity2
#The velocity at the centerline of the pipe is maximum; at the wall has to be zero by the no-slip condition
#Second parameters: R=2, beta=0.03, mu0=0.02, n=0.1
v=VelocityProfile(2,0.03,0.02,0.1)
velocity3=v.value(0)
velocity4=v.value(1)
print v.formula()
print 'The velocity of the fluid at the center of the pipe is %g' %velocity1, 'at the wall of the pipe is %g' %velocity2
#The velocity at the centerline of the pipe is maximum; at the wall has to be zero by the no-slip condition
"Question 2"
#Implementing the Gravity SuperClass by creating a SubClass for the Electric force
import matplotlib.pyplot as plt 
from numpy import linspace
from pylab import *
class Gravity :
    """Gravity force between two physical objects"""
    def __init__(self, m, M):
        self.m=m #mass of object 1
        self.M=M #mass of object 2
        self.G = 6.67428E-11 #gravity constant, m∗∗3/kg/s∗∗2
    def force(self , r):
        G, m, M= self.G, self.m, self.M
        return G*m*M/r**2
    def visualize(self, r_start , r_stop , n=100):
        r = linspace(r_start , r_stop , n) 
        g=self.force(r)
        plt.plot(r, g)
        plt.title('Gravity force for m=%g, M=%g' % (self.m, self.M))
        plt.show()
class  ElectricForce(Gravity):
    """Electric force between two charges q1 and q2, being a distance r apart in a medium with permittivity μ0"""
    def __init__(self, m, M):
        "set values for charges m=q1, M=q2"
        Gravity.__init__(self, m, M)  #for the electric force m, M are charges q1, q2
        self.G=8.99E9 
    def force(self, r):
        "compute electric force as a function of r, distance between charges"
        return Gravity.force(self, r)
    def visualize(self, r_start, r_stop, n=100):
        "visualize the electric force plot, setting limits for position r (x axes)"
        plt.title('Electric force for q1=%g, q2=%g' % (self.m, self.M))
        Gravity.visualize(self, r_start, r_stop, n=100)
#Calling the ElectricForce Class for charges q1=3 q2=4 at distance 10 meters apart   
E=ElectricForce(3,4)
Fe=E.force(10)  
print 'The Electric (or Coulomb) Force is: %.1f' %Fe
E.visualize(1,15)  
#Comparing ElectricForce Class with Gravity Class when masses m=3(=q1) and M=4(=q2)  at the same distance the charges were r=10
G=Gravity(3, 4)
Fg=G.force(10)
print 'The Gravitational attractive Force is: %.1f' %Fg
G.visualize(1,15)   
"Question 3"
#Creating a basic GUI which contains a set of buttons describing different widgets
from Tkinter import *
class App:
    def __init__(self, master):
        "constructs the frame which will hold all the other widgets"
        frame=Frame(master)
        frame.pack()
        self.button= Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.button1= Button(frame, text="The button widget", command=self.button_widget)
        self.button1.pack(side=LEFT)
    def button_widget(self):
        print "The Button widget is a standard widget,used for different kinds of buttons. A button is something the user interacts with by for istance clicking on it. A button may contain an image or a long text in a single font. An example of a button is what you've clicked on to open this description."
        self.button2= Button(frame, text="The Canvas widget", command=self.canvas_widget)
        self.button2.pack(side=LEFT)
    def canvas_widget(self):
        print "The Canvas widget is a widget for graphics facilities. Examples of graphical objects that can be obtained using a Canvas are geometrical figures, images, and other widgets as well. This widget is used to create graphs and plots,but also to improve custom widgets. "
        self.button3= Button(frame, text="The Entry widget", command=self.entry_widget)
        self.button3.pack(side=LEFT)
    def entry_widget(self):
        print "The Entry widget is a basic widget that gets the input of the user of an application. The input can be just a single line of text in a single font. If the user writes a string too long for the display space available, the content will be scrolled. However the user can use the arrow keys to the invisible parts of the string."
        self.button4= Button(frame, text="The message widget", command=self.message_widget)
        self.button4.pack(side=LEFT)
    def message_widget(self):
        print "The Message widget is a widget designed to display multiline messages. This widget can wrap a text or adjust its width to maintain a given aspect ratio. A short text message can be displayed using a single font."
        self.button5= Button(frame, text="The Pack Geometry Manager", command=self.packgm)
        self.button5.pack(side=LEFT)
    def packgm(self):
        print "The Pack geometry manager is a tool that packs widgets in rows or columns. This pack is literally a 'geometry' manager that can be controlled using different options like fill, expand, and side. The manager handles all the widgets within the same master widget."
root =Tk()
app =App(root)
root.mainloop()
"Question 4"
#Modifiyng the Drummode programme to mode the path of a particle in an electric and magnetic field
import pylab
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
#for the user's inputs/warning messages
import tkMessageBox #output
import tkSimpleDialog #input
import tkFileDialog
from scipy import *
class PathinBandE:
    def __init__(self, master):
        "constructs the frame which will hold all the other widgets"
        frame = Frame(master)
        frame.pack()
        self.makePlot(frame)
        self.makeInputs(frame)
    def makePlot(self, frame):
        "makes a canvas widget to plot (and hence show) the final calculation"
        self.fig = Figure(figsize=(6,4), dpi=150) 
        #Figure object can't just be embeded into Tkinter front end, but has to go in a Canvas widget       
        self.canvas = FigureCanvasTkAgg(self.fig,frame)
        self.canvas.show()
        #Placing grid at coordinates (0,1) of the master frame 
        self.canvas.get_tk_widget().grid(row = 0, column = 1)
        #Adding a standard plot toolbar
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 1)
    def makeInputs(self, frame):
        "builds the frame which will hold all the inputs and their labels"
        InputFrame = Frame(frame)
        InputFrame.grid(column = 0, row = 0)  #coordinates (0,0) of the master frame
        #Labelling in such a way that the variables are displayed 
        self.lblEx = Label(InputFrame, text = "Ex",fg="red", justify=LEFT)
        self.lblEx.grid(column= 0,row= 0)  #coordinates of button position
        self.lblEy = Label(InputFrame, text = "Ey",fg="red", justify=LEFT)
        self.lblEy.grid(column= 0,row= 1)
        self.lblEz = Label(InputFrame, text = "Ez",fg="red", justify=LEFT)
        self.lblEz.grid(column= 0,row= 2)
        self.lblBx = Label(InputFrame, text = "Bx",fg="yellow", justify=LEFT)
        self.lblBx.grid(column= 0,row= 3)
        self.lblBy = Label(InputFrame, text = "By",fg="yellow", justify=LEFT)
        self.lblBy.grid(column= 0,row= 4)
        self.lblBz = Label(InputFrame, text = "Bz",fg="yellow", justify=LEFT)
        self.lblBz.grid(column= 0,row= 5)
        self.lblm = Label(InputFrame, text = "m", justify=LEFT)
        self.lblm.grid(column= 0,row= 6)
        self.lblq = Label(InputFrame, text = "q", justify=LEFT)
        self.lblq.grid(column= 0,row= 7)
        self.lblx = Label(InputFrame, text = "x",fg="blue", justify=LEFT)
        self.lblx.grid(column= 0,row= 8)
        self.lbly = Label(InputFrame, text = "y",fg="blue", justify=LEFT)
        self.lbly.grid(column= 0,row= 9)
        self.lblz = Label(InputFrame, text = "z",fg="blue",justify=LEFT)
        self.lblz.grid(column= 0,row= 10)
        self.lblvx = Label(InputFrame, text = "vx",fg="green", justify=LEFT)
        self.lblvx.grid(column= 0,row= 11)
        self.lblvy = Label(InputFrame, text = "vy",fg="green", justify=LEFT)
        self.lblvy.grid(column= 0,row= 12)
        self.lblvz = Label(InputFrame, text = "vz",fg="green", justify=LEFT)
        self.lblvz.grid(column= 0,row= 13)
        self.lblt = Label(InputFrame, text = "t",fg="purple", justify=LEFT)
        self.lblt.grid(column= 0,row= 14)
        self.lbldt = Label(InputFrame, text = "dt",fg="purple", justify=LEFT)
        self.lbldt.grid(column= 0,row= 15)
        #Defining the Entry Boxes
        self.entEx = Entry(InputFrame)  #Input is chosen by the user
        self.entEx.grid(column = 1, row = 0) #position changed to the righ to facilitate user in typing
        self.entEy = Entry(InputFrame)
        self.entEy.grid(column = 1, row = 1)
        self.entEz = Entry(InputFrame)
        self.entEz.grid(column = 1, row = 2)
        self.entBx = Entry(InputFrame)
        self.entBx.grid(column = 1, row = 3)
        self.entBy = Entry(InputFrame)
        self.entBy.grid(column = 1, row = 4)
        self.entBz = Entry(InputFrame)
        self.entBz.grid(column = 1, row = 5)
        self.entm = Entry(InputFrame)
        self.entm.grid(column = 1, row = 6)
        self.entq = Entry(InputFrame)
        self.entq.grid(column = 1, row = 7)
        self.entx = Entry(InputFrame)
        self.entx.grid(column = 1, row = 8)
        self.enty = Entry(InputFrame)
        self.enty.grid(column = 1, row = 9)
        self.entz = Entry(InputFrame)
        self.entz.grid(column = 1, row = 10)
        self.entvx = Entry(InputFrame)
        self.entvx.grid(column = 1, row = 11)
        self.entvy = Entry(InputFrame)
        self.entvy.grid(column = 1, row = 12)
        self.entvz = Entry(InputFrame)
        self.entvz.grid(column = 1, row = 13)
        self.entt = Entry(InputFrame)
        self.entt.grid(column = 1, row = 14)
        self.entdt = Entry(InputFrame)
        self.entdt.grid(column = 1, row = 15)
        #TPlot function (under last input)
        self.butPlot = Button(InputFrame, text ='PLOT', command = self.calcPattern) #clicking on button runs the Pattern method
        self.butPlot.grid(column = 0, row = 16)
    def Pattern(self):
        Ex = float(self.entEx.get()) #Calculationg variable to be input into the function as a float number (otherwise decimals entered are turned into 0.)
        Ey = float(self.entEy.get()) 
        Ez = float(self.entEz.get())
        Bx = float(self.entBx.get())
        By = float(self.entBy.get())
        Bz = float(self.entBz.get())
        m = float(self.entm.get())
        q = float(self.entq.get())
        x = float(self.entx.get())
        y = float(self.enty.get())
        z = float(self.entz.get())
        vx = float(self.entvx.get())
        vy = float(self.entvy.get())
        vz = float(self.entvz.get())
        a = []
        b = []
        c = []
        t = 0
        dt =float(self.entdt.get())
        #Euler's method is used
        while t < float(self.entt.get()): #traces path until time reaches value
            Fx = q * (Ex + (vy * Bz) - (vz * By) )
            vx = vx + Fx/m * dt     #Acceleration = F/m; dv = a.dt
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
        ax = Axes3D(self.fig)
        ax.set_title("Path of a charged particle in E and B field")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.plot3D(a,b,c, color='blue', label='path')
        ax.legend(loc='lower left')
        #Updating Canvas Widget
        self.canvas.show()      
root = Tk()
drum = PathinBandE(root)
root.mainloop() 