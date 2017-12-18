import matplotlib.pyplot as plt
import numpy as np
x=[589.6E-9,589E-9,577E-9,546.1E-9,491.6E-9,435.8E-9,407.8E-9]
y=[1.5172,1.5160,1.5156,1.5166,1.5208,1.5274,1.5307]
plt.errorbar(x,y, xerr=0, yerr=0.0003)
plt.xlabel('Wavelenght (nm)')
plt.ylabel('Refractive index n')
plt.plot(x,y)
plt.title('Dispersion Curve for Prism 1 (D)')
plt.show()
def slope(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2)
slope(float=589.6E-9,float=1.5172,float=407.8E-9,float=1.5307)
print(slope)
RP=slope * 29E-6
print(RP)
r=[589.6E-9,589E-9,577E-9,546.1E-9,491.6E-9,435.8E-9,407.8E-9]
t=[1.5395,1.54491,1.5438,1.5443,1.5487,1.5522,1.5553]
plt.errorbar(r,t, xerr=0, yerr=0.0008)
plt.xlabel('Wavelenght (nm)')
plt.ylabel('Refractive index n')
plt.plot(r,t)
plt.title('Dispersion Curve for Prism 2 (C)')
plt.show()
