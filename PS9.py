"PROBLEM SHEET 9"
"Question 1"
#Investigating the production of X-rays and their interactions with matter using the Monte Carlo Method
#Simulating the production from synchrotron radiation of individual photons, each having a different energy
#Data are dowloaded into a file and a spectra is obtained making a plot
#Generating a set of photon energies such that the probability to have a given photon energy is proportional to the height of the curve
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d 
import numpy as np
xray= np.loadtxt('xray4139.dat')
x,y=xray[:,0],xray[:,1]
E_max = 1.0 * 10**4 #Maximum value for the Energy
f_max = 3.0 * 10**13 #Maximum value for the frequency
#Using interp1d to interpolate linearly f and evaluate the function at every Energy
value= interp1d(x, y)
#E and f represents a point on the energy spectrum plot
accepted_E=[]
accepted_f=[]
for counter in range (1,100000):
    r1 = np.random.uniform(0.0,1.0) 
    r2 = np.random.uniform(0.0,1.0) 
    E = r1 * E_max  
    f = r2 * f_max
    if E > 10: #In this way it fits in the interpolation range
        if f <= value(E):
            accepted_E.append(E)
            accepted_f.append(f)
plt.figure()
plt.plot(x,y,c='r', label='data')
plt.xlabel('Photon Energy (eV)')
plt.ylabel('Photons/sec/mr^2/0.1%BW')
plt.scatter(accepted_E,accepted_f, c='g', label='accepeted photons')
plt.title('Maximum frequency versus allowed Photon Energies')
plt.legend()
plt.show() 
plt.figure()
plt.hist(accepted_E,50)
plt.title('Histogram of accepted photons')
plt.show()
#Hence is confirmed that the probability to accept the photon is proportional to the height of the curve
#Generating photons with the correct energy distribution, for each photon determine its attenuation length and probability of being adsorbed     
#Generating a random number r3 between 0 and 1, if r3<P we say it has been adsorbed, if not it makes it through
#Attenuation lengths as a function of energy is downloaded into a file
attlen = np.loadtxt('xray7173.dat')
#Thickness of the Teflon target in mm
x= 0.1E-3
attenuation_energy = attlen[:,0]
attenuation_length = attlen[:,1]*(10**-6)
value1=interp1d(attenuation_energy,attenuation_length)
lambdaa= 0
length = len(accepted_E)
#Photons that got through the Teflon
phot_through = [] 
for counter in range (1,length): 
    E = accepted_E[counter - 1]
    if E > 30: #chosen by looking at the data file in order to avoid interpolation error 
        lambdaa = value1(E) 
        Probability = 1 - np.exp(-x/lambdaa) #P(photon of energy E being adsorbed before x)=1-e**(-x/lambda(E)) where lambda= attenuation lenght
        r3 = np.random.uniform(0.0,1.0) 
        if r3 >= Probability: #If the random photon is greater than or equal then it has got through the Teflon
            phot_through.append(E) #only add to list if got through
plt.figure()
#Plotting a Histogram of the accepted photons energies
plt.hist(phot_through,bin=50)
plt.title('Histogram of the accepted photon energies')
plt.show()