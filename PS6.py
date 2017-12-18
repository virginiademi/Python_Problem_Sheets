"PROBLEM SHEET 6"
#Solving the time-independent Schrodinger Equation H*psi=E*psi:
#the eigenfunctions are the wavefunction psi_n=sqrt(2/L)*sin((n*pi*x)/L);
#the eigenvalues are the energies E=(h^2*n^2*pi^2)/(2m*L^2)
"Exercise 1"
import numpy as np
import matplotlib.pyplot as plt
"Part 1"
#Plotting the wavefunction psi in a way that the user can choose the value for n 
#For this problem the period is set as L=1
def psi_n(x,n):
    A=np.sqrt(2)
    return A*np.sin(n*np.pi*x)     
#the value for x is not defined in the fun Problem solvingction as otherwise integration doesn't work
xvalues=np.linspace(0,1,100)
#Plot for psi_3
plt.subplot(3,1,1)
plt.plot(xvalues, psi_n(xvalues,3))
plt.title(r'$\psi_3$')
#Plot for psi_4
plt.subplot(3,1,2)
plt.plot(xvalues, psi_n(xvalues,4))
plt.title(r'$\psi_4$')
#Plot for psi_3 times psi_4
plt.subplot(3,1,3)
plt.plot(xvalues,((psi_n(xvalues,3))*(psi_n(xvalues,4))))
plt.title(r'$\psi_3\times\psi_4$')
plt.show()
"Part 2"
#Showing that psi_3 and psi_4 are orthogonal by integrating their product from 0 to L
from scipy.integrate import quad
def product(x,n1,n2):
    A=np.sqrt(2)
    return A*np.sin(n1*np.pi*x)*A*np.sin(n2*np.pi*x)
iprod , err = quad ( product , 0 , 1 , args =(3,4) )
print 'value = %2f' %iprod , # the integral of psi_3 times psi_4 between x=0 and x=1
print 'error= {} '.format(err) # the numerical uncertainty in the integral
#Evaluating integral
print ' Exact solution = {} '.format (iprod)
#Product result is approaching zero, if we consider the error the result is correct
"""
value = 0.000000 error= 8.91075920365e-15 
 Exact solution = 3.00657446286e-17 
"""
 #--> hence psi_3 and psi_4 are orthogonal
"Part 3"
#Testing orthogonality and normalization of wavefunctions for different values of n,m
#Integral from 0 to L of the complex conjugate of psi_m times psi_n is Kronecker delta_mn
#the complex conjugate of psi_m=psi_m as the imaginary part is zero
# test 1: n=5 m=6
iprod , err = quad ( product , 0 , 1 , args =(5,6) )
print 'value = %2f' %iprod ,
print 'error= {} '.format(err) 
print ' Exact solution = {} '.format (iprod)
"""
value = -0.000000 error= 8.80866549497e-15 
 Exact solution = -9.70657625038e-17 
"""
#test 2: n=7 m=8
iprod , err = quad ( product , 0 , 1 , args =(7,8) )
print 'value = %2f' %iprod ,
print 'error= {} '.format(err) 
print ' Exact solution = {} '.format (iprod)
"""
value = -0.000000 error= 7.5213549599e-15 
 Exact solution = -3.74555408759e-16 
"""
 #test 3: n=8 m=9
iprod , err = quad ( product , 0 , 1 , args =(8,9) )
print 'value = %2f' %iprod ,
print 'error= {} '.format(err) 
print ' Exact solution = {} '.format (iprod)
"""
value = 0.000000 error= 9.17634778375e-15 
 Exact solution = 1.56668738469e-16 
"""
 #test 4: n=9 m=9
iprod , err = quad ( product , 0 , 1 , args =(9,9) )
print 'value = %2f' %iprod ,
print 'error= {} '.format(err) 
print ' Exact solution = {} '.format (iprod)
"""
value = 1.000000 error= 1.11022302463e-14 
 Exact solution = 1.0 
"""
 #--> hence psi_m and psi_n are orthogonal and normalised as for m=n the solution is 1
"Part 4"
 #the expectation value for x can be calculated: <x>=integral from 0 to L of (psi_n)^2*x dx
def expectation(x,n):
    A=np.sqrt(2)
    return ((A*np.sin(n*np.pi*x))**2)*x
iprod , err = quad ( expectation , 0 , 1 , args =(4) )
print 'value = %.1f' %iprod 
"value: 0.5"
iprod , err = quad ( expectation , 0 , 1 , args =(7) )
print 'value = %.1f' %iprod 
"value: 0.5"
iprod , err = quad ( expectation , 0 , 1 , args =(9) )
print 'value = %.1f' %iprod 
"value: 0.5"
#given that period=1 then the result is correct: <x>=L/2
"Part 5"
def expectation2(x,n):
    A=np.sqrt(2)
    return ((A*np.sin(n*np.pi*x))**2)*(x**2)
iprod , err = quad ( expectation2 , 0 , 1 , args =(4) )
print 'value = %.1f' %iprod 
"value = 0.3"
iprod , err = quad ( expectation2 , 0 , 1 , args =(7) )
print 'value = %.1f' %iprod 
"value = 0.3"
iprod , err = quad ( expectation2 , 0 , 1 , args =(100) )
print 'value = %.1f' %iprod 
"value = 0.3"
#<x^2>=(0.3)L
#Calculating delta(x)=sqrt(<x^2>-<x>^2)
delta=np.sqrt((0.3-(0.5)**2))
print 'delta = %.1f' %delta
"delta = 0.2"
#Value for delta(x)=0.2
"Part 6"
#Showing that for n-->large delta(x)-->L/sqrt(12)~0.28867
#Expectation value for x at n=10000
iprod , err = quad ( expectation , 0 , 1 , args =(10000) )
print 'value = %.5f' %iprod 
"value = 0.50002"
##Expectation value for x^2 at n=10000
iprod , err = quad ( expectation2 , 0 , 1 , args =(10000) )
print 'value = %.5f' %iprod 
"value = 0.33329"
delta=np.sqrt((0.33329-(0.50002)**2))
print 'delta = %.5f' %delta
"delta = 0.28857"
#the quantum result for n-->large matches the classical result
"Exercise 2"
"Part 1"
#Plotting the wavefunction A(x)=((x/L)^3)-(11/7)((x/L)^2)+(4/7)(x/L)
#Setting the period to 1
def A(x):
    return (((x/1)**3.)-((11./7.)*((x/1)**2.))+((4./7.)*(x/1)))
x=np.linspace(-1,1,100)
plt.plot(x,A(x))
plt.title(r'A(x)')
plt.show()
#Boundary Conditions at x=0 and x=L=1
print A(0)
print A(1)
"both 0, hence boundar conditions hold"
"Part 2"
def Asquared(x):
    return (x**(3.)-(11./7.)*x**(2.)+(4./7.)*x)**(2.)
iprod , err = quad (Asquared , 0 , 1 )
constant= np.sqrt(1/iprod)
print constant
"27.1108834235 which is equal to the sqrt(735)"
"Part 3"
#Evaluating coefficients C_n
#C_n= integral from 0 to L of psi_n times f(x)
#Using L=1 and f(x)=A(x)
def psitimesfunction(x,n):
    return (x**(3.)-(11./7.)*x**(2.)+(4./7.)*x)*np.sqrt(2)*np.sin(n*np.pi*x)*np.sqrt(735)
iprod , err = quad ( psitimesfunction , 0 , 1 , args =(1) )
print 'C_1=%.6f' %iprod
iprod , err = quad ( psitimesfunction , 0 , 1 , args =(2) )
print 'C_2=%.6f' %iprod
iprod , err = quad ( psitimesfunction , 0 , 1 , args =(3) )
print 'C_3=%.6f' %iprod
iprod , err = quad ( psitimesfunction , 0 , 1 , args =(4) )
print 'C_4=%.6f' %iprod
iprod , err = quad ( psitimesfunction , 0 , 1 , args =(5) )
print 'C_5=%.6f' %iprod
iprod , err = quad ( psitimesfunction , 0 , 1 , args =(6) )
print 'C_6=%.6f' %iprod
iprod , err = quad ( psitimesfunction , 0 , 1 , args =(100) )
print 'C_100=%.6f' %iprod
#for n-->large coefficients are smaller and smaller, for n=100 C_100=0.000007
"""
C_1=0.353298
C_2=0.927407
C_3=0.013085
C_4=0.115926
C_5=0.002826
C_6=0.034348
C_100=0.000007
"""
"Part 4"
#Showing that the sum of all the coefficients C_n squared is equal to 1
#Defining |C_n|^2 to do the integration
sumC_n=0
for n in range(1,100):
    iprod , err = quad ( psitimesfunction , 0 , 1 , args =(n) )
    sumC_n=sumC_n+ iprod**2
print sumC_n
"0.99999999942"
#The sum of all the coefficients is converging to 1 
"Part 5"
from pylab import frange
#Showing that the sum of all the coefficients C_i squared times n^2 is equal to 3.849
#Definig function that has to be integrated: psi(i)*A*(x), to find coefficients C_i
def C_i(x, i):
    return np.sqrt(2.)*np.sin(i*np.pi*x)*(x**(3.)-(11./7.)*x**(2.)+(4./7.)*x)*np.sqrt(735.)
def coeff(imax):
    values = []
    for i in frange(1, imax):
        iprod, err = quad(C_i, 0, 1, args=(i))
        c = iprod**(2.)*i**(2.)
        values.append(c)
    return values
#calling the function coeff for imax=24
K= coeff(24)
#Sum frmo i=1 to i=24
Sum = sum(K)
print 'The sum of (C_i^2)*i values for i in the range of (0, 24) is ', Sum
"The sum of (C_i^2)*i values for i in the range of (0, 24) is  3.84961819685"
#The expectation value for energy is <E>=3.849*E_0
#The ground energy is given E_0=(h^2/2*pi*m)(n^2*pi^2/L^2)
#Using h=6.63*e^-34 and L=1
def Energy(i):
    return ((6.63e-34)/2.*np.pi)*(i**2)*np.pi**(2.)
#Defining function for coefficients C_i times Energy for i in range (1, imax)
def FindE(imax):
    cenergy = []
    for i in frange(1, imax):
        iprod, errc = quad(C_i, 0, 1, args=(i))
        L = iprod**(2.)*Energy(i)
        cenergy.append(L)
    return cenergy
P= FindE (24)
Psum = sum(P)
#Finally the energy E can be obtained from the ratio between the sum of all C_i over the Ground state energy E_0
Ezero = ((6.63e-34)/2.*np.pi)*1**(2.)*np.pi**(2.)
ratio= Psum/Ezero
print 'The ratio <E>/E_0 is ', ratio
print 'Hence <E>= {}*E_0' .format(ratio)
"The ratio <E>/E_0 is  3.84961819685"
"Hence <E>= 3.84961819685*E_0"
"Exercise 3"
from scipy.special import hermite
from math import factorial
#This special function returns the nth hermite polynomial h_n(x), orthogonal over(inf,-inf) with weigthing function (exp(x**2))
#Testing Hermite polynomial function for n=2
hermite(2)
print hermite(2) 
"4 x - 2"
#Generating function for normalised wavefunctions taking a=1 and choosing n
def psiherm(x,n):
    return ((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi)))
"Part 2"
#Checking that wavefunctions are orthogonal and normalised
def psimpsin(x, n, m):
    return ((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi)))*((hermite(m)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(m)*factorial(m)*np.sqrt(np.pi)))
iprod , err = quad (psimpsin , -10 , 10 , args =(0,0) )
print 'Value of the integral of (n=0 * m=0) = %.5f' %iprod
iprod , err = quad (psimpsin , -10 , 10 , args =(1,0) )
print 'Value of the integral of (n=1 * m=0) = %.5f' %iprod
iprod , err = quad (psimpsin , -10 , 10 , args =(1,1) )
print 'Value of the integral of (n=0 * m=0) = %.5f' %iprod
iprod , err = quad (psimpsin , -10 , 10 , args =(2,0) )
print 'Value of the integral of (n=0 * m=0) = %.5f' %iprod
iprod , err = quad (psimpsin , -10 , 10 , args =(3,3) )
print 'Value of the integral of (n=0 * m=0) = %.5f' %iprod
iprod , err = quad (psimpsin , -10 , 10 , args =(4,5) )
print 'Value of the integral of (n=0 * m=0) = %.5f' %iprod
"""
Value of the integral of (n=0 * m=0) = 1.00000
Value of the integral of (n=1 * m=0) = 0.00000
Value of the integral of (n=0 * m=0) = 1.00000
Value of the integral of (n=0 * m=0) = 0.00000
Value of the integral of (n=0 * m=0) = 1.00000
Value of the integral of (n=0 * m=0) = 0.00000
"""
#The integral is equal to 1 when n=m which means that the wavefunctions are normalised.
#The integral is equal to zero when n is different from m which means that the wavefunctions are orthogonal
"Part 3"
import matplotlib.pyplot as plt
#Probability density is defined as the norm square of psi_n
#Defining probability as a function of (x,n,b) and psi_n as a function of (x,n,a)
#the values of n are chosen by the user 
#a and b are used to shift the graphs vertically
def prob(x, n, b):
    return b+(((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi))))**2
def psi_n(x, n, a):
    return a+((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi)))
#Generating values of x from -10 to 10 in 0.1 steps
x= frange (-8, 10, 0.1)
#Create plot for the wavefunction and the probability density
#First argument gives dimension of grid 2x2
#Second argument gives the starting position at (0,0)
#Third argument gives the column width
plt.subplot2grid((2,2), (0,0), colspan=2)
#Plotting psi_n for n and a from 0 to 10 
plt.plot(x, psi_n(x, 0, 0), label='n=0')
plt.plot(x, psi_n(x, 1, 1), label='n=1')
plt.plot(x, psi_n(x, 2, 2), label='n=2')
plt.plot(x, psi_n(x, 3, 3), label='n=3')
plt.plot(x, psi_n(x, 4, 4), label='n=4')
plt.plot(x, psi_n(x, 5, 5), label='n=5')
plt.plot(x, psi_n(x, 6, 6), label='n=6')
plt.plot(x, psi_n(x, 7, 7), label='n=7')
plt.plot(x, psi_n(x, 8, 8), label='n=8')
plt.plot(x, psi_n(x, 9, 9), label='n=9')
plt.plot(x, psi_n(x, 10, 10), label='n=10')
#Adding title and labels
plt.title(r'Wavefunctions $\psi_n$', fontsize=12)
plt.ylabel(r'$\psi_n(x)$', fontsize=12)
plt.legend(loc="center right",prop={'size':9})
#Same procedure as for plot above
plt.subplot2grid((2,2), (1,0), colspan=2)
#PLotting probability densities for n and a going from 0 to 10
plt.plot(x, prob(x, 0, 0), label='n=0')
plt.plot(x, prob(x, 1, 1), label='n=1')
plt.plot(x, prob(x, 2, 2), label='n=2')
plt.plot(x, prob(x, 3, 3), label='n=3')
plt.plot(x, prob(x, 4, 4), label='n=4')
plt.plot(x, prob(x, 5, 5), label='n=5')
plt.plot(x, prob(x, 6, 6), label='n=6')
plt.plot(x, prob(x, 7, 7), label='n=7')
plt.plot(x, prob(x, 8, 8), label='n=8')
plt.plot(x, prob(x, 9, 9), label='n=9')
plt.plot(x, prob(x, 10, 10), label='n=10')
#Adding title and labels
plt.title('Probability densities $P_n(x)$', fontsize=12)
plt.ylabel(r'$P_n(x)$', fontsize=12)
plt.legend(loc="center right",prop={'size':9})
plt.show()
"Part 4"
#Demonstrating that the expectation value for position is zero for different quantum numbers n
#<x> is defined as integral from -L to L of psi_n complex conj times x times psi_n
def position(x, n):
    return ((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi)))*((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi)))*x
#Calulating <x> for different quantum numbers
iprod, err= quad(position, -1, 1, args=(0))
print '<x> for n=0 %.2f' %iprod
print 'with uncertainty={}' .format(err)
iprod, err= quad(position, -1, 1, args=(8))
print '<x> for n=0 %.2f' %iprod
print 'with uncertainty={}' .format(err)
iprod, err= quad(position, -1, 1, args=(21))
print '<x> for n=0 %.2f' %iprod
print 'with uncertainty={}' .format(err)
"""
<x> for n=0 0.00
with uncertainty=3.93604828406e-15
<x> for n=0 0.00
with uncertainty=1.03583519999e-15
<x> for n=0 0.00
with uncertainty=5.02536829907e-16
"""
"Part 5"
#Calulating <x^2> simply multiplying previous function position by x for n=4,7,10
#Calculating delta x= sqrt(<x^2>-<x>^2) again for n=4,7,10
#Because <x> is zero deltax is simply the sqrt of <x^2>
def position2(x, n):
    return x**(2.)*(((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi))))**2
quantum4, err= quad(position2, -50, 50, args=(4))
deltax=np.sqrt(quantum4)
print '<x^2> for n=4 %.3f' %quantum4
print 'with error={}' .format(err)
print 'deltax for n=4 %.3f' %deltax
quantum7, err= quad(position2, -50, 50, args=(7))
deltax=np.sqrt(quantum7)
print '<x^2> for n=7 %.3f' %quantum7
print 'with error={}' .format(err)
print 'deltax for n=7 %.3f' %deltax
quantum10, err= quad(position2,-50, 50, args=(10))
deltax=np.sqrt(quantum10)
print '<x^2> for n=10 %.3f' %quantum10
print 'with error={}' .format(err)
print 'deltax with x=10 %.3f' %deltax
"""
<x^2> for n=4 4.500
with error=7.60881920707e-09
deltax for n=4 2.121
<x^2> for n=7 7.500
with error=9.36123886927e-08
deltax for n=7 2.739
<x^2> for n=10 10.500
with error=2.02161634265e-08
deltax with x=10 3.240
"""
#Therefore is evident that <x^2>=(2*n+1)/2 and deltax=sqrt((2*n+1)/2) with a small error
quantum4proof=(2*4+1)/2
deltaxproof=np.sqrt(quantum4proof)
print 'compare value from integration: %.2f'%quantum4,'with value from formula: %.2f' %quantum4proof
print 'compare deltax for n=4 2.12 with value from formula: %.2f' %deltaxproof
"compare value from integration: 4.50 with value from formula: 4.00"
"compare deltax for n=4 2.12 with value from formula: 2.00"
"Part 6"
#In the classical interpretation x=x_0sin(omega*t) where <x>=0 and deltax=X_0/sqrt(2)
#Assuming classical and quantum results for delta x were the same x_0=sqrt(2*n+1):
#deltax=sqrt((2*n+1)/2)
#deltax=x_0/sqrt(2)
#sqrt((2*n+1)/2)=x_0/sqrt(2)
#x_0= sqrt(2*n+1)
"Part 7"
#Graphical comparison of quantum and classical probability
#Quantum probability density is given by P(x)=|psi_n|^2
#Classical probability is given by P(x)=1/(pi*sqrt((2*n)+(1)-x^2))
#Defining function for classical probability and quantum probability
def classprob(x, n, a):
    return a+1./(np.pi*np.sqrt((2*n)+(1.)-x**(2.)))
def quantumprob(x, n, b):
    return b+(((hermite(n)(x))*np.exp(-x**(2.)/(2.)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi))))**2
x = frange(-10, 10, 0.05) 
#Plotting the quantum probability fo n=10,30,50
#The value of a shifts the plot width
plt.plot(x, quantumprob(x, 10, 0), label='n=10 quantum')
plt.plot(x, quantumprob(x, 30, 0.5), label='n=30 quantum')
plt.plot(x, quantumprob(x, 50, 1.5), label='n=50 quantum')
#Plotting the classical probability for n=10,30,50
#The value of a shifts the plot width
plt.plot(x, classprob(x, 10, 0), label='n=10 classical')
plt.plot(x, classprob(x, 30, 0.5), label='n=30 classical')
plt.plot(x, classprob(x, 50, 1.5), label='n=50 classical')
#Adding title and labels
plt.title('Comparison between classical and quantum probability', fontsize=11)
plt.legend(loc="center",prop={'size':9})
plt.show()
#Conclusions:
#For the classical case the probability increases as an exponential at the ends of the motion
#For the quantum case the probability is different from zero in the classically forbidden regions
#For low values of n there is a little resemblance between the quantum and classical probabilities
#For high n values the quantum and classical propalities look more alike
#Hence for an extremely large value of n the quantum case and the classical case match