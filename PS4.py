"PROBLEM SHEET 4"
"EXERCISE 1"
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
plt.figure(facecolor='white') #to get a white background
#Plotting Sin and Cos
plt.subplot(2,1,1)
x= np.linspace(-np.pi , np.pi, 256, endpoint=True)
C, S =np.cos(x), np.sin(x)
#Setting limits and labelling axes using LaTex
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
#Moving spines of the plot (gca means 'get current axis')
ax = plt.gca() 
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#Plotting
plt.plot(x,C,'b', linewidth=2.5, linestyle="-")
plt.plot(x, S,'r',linewidth=2.5, linestyle="-")
#Adding legend
plt.title(r'Figure showing two subplots, with points labelled using LaTex text', fontsize=11, color='black')
plt.plot(x, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(x, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left') 
#Annotating some points like the 2pi/3 value.
#First drawing a marker on the curve and a straight dotted line. 
#Then using the 'annotate' command to display some text with an arrow.
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',xy=(t, np.sin(t)), xycoords='data',xytext=(+60, +30), textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ],[np.sin(t), ], 50, color='red')
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',xy=(t, np.cos(t)), xycoords='data',xytext=(-90, -50), textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#Adjusting properties of the lines such that labels are visible.
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
#Plotting Exponential (same code procedure)
plt.subplot(2,1,2)
E, F= np.exp(x), np.exp(-x)
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(E.min() * 1.1, E.max() * 1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([0, 10, 20], [r'$0$', r'$10$', r'$exp{(\pi)}$'])
ax = plt.gca() 
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.plot(x,E, 'g', linewidth=2.5, linestyle="-") 
plt.plot(x,F, 'c', linewidth=2.5, linestyle="-")
plt.plot(x, E, color="green", linewidth=2.5, linestyle="-", label="exp")
plt.plot(x, F, color="cyan",  linewidth=2.5, linestyle="-", label="- exp")
plt.legend(loc='lower left') 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
plt.plot([1], color='blue')
plt.annotate(r'$exp(0)=1$', xy=(0, 1), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.scatter([0],np.exp(0), color='blue')
#Generating figure as a '.png' file
plt.savefig("Figure 1", ext="png",close=False, verbose=True)
plt.show()
"EXERCISE 2"
import mayavi
from mayavi import mlab
stm=np.loadtxt( 'stm.dat' ,float)
mlab.surf(stm)
plt.savefig("Figure 2", ext="png", close=False, magnification='auto')
"EXERCISE 3"
import matplotlib.image as mpimg
img=mpimg.imread('NMR_phantom.png')
plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.colorbar()
lum_img=img[:,:,0]
imgplot=plt.imshow(lum_img)
plt.show(imgplot)