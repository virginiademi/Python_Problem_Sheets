#Importing programmes that will be used later in the code
from scipy.special import hermite  #needed to plot the wavefunction in the quantum harmonic oscillator
from scipy.integrate import quad
from math import factorial
from pylab import frange
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import tkMessageBox
from scipy import *
import webbrowser
#Defining functions that will be used later in the code to calculate and plot features of the quantum harmonic oscillator
def psi_n(x, n, a):
    """Normalised wavefunction with quantum number n and a=sqrt(hbar/m*omega)"""
    return ((hermite(n)(x/a))*np.exp(-x**(2.)/(2.*a**2)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi*a**2)))
def psi_m(x,m, a):
    """Normalised wavefunction with quantum number m and a=sqrt(hbar/m*omega)"""
    return ((hermite(m)(x/a))*np.exp(-x**(2.)/(2.*a**2)))/(np.sqrt((2.)**(m)*factorial(m)*np.sqrt(np.pi*a**2)))
def classprob_n(x, n):
    """Classical probability for n"""
    return 1./(np.pi*np.sqrt((2*n)+(1.)-x**(2.)))
def quantumprob_n(x, n, a):
    """Quantum probability for n"""
    return (((hermite(n)(x/a))*np.exp(-x**(2.)/(2.*a**2)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi*a**2))))**2
def classprob_m(x, m):
    """Classical probability for m"""
    return 1./(np.pi*np.sqrt((2*m)+(1.)-x**(2.)))
def quantumprob_m(x, m, a):
    """Quantum probability for m"""
    return (((hermite(m)(x/a))*np.exp(-x**(2.)/(2.*a**2)))/(np.sqrt((2.)**(m)*factorial(m)*np.sqrt(np.pi*a**2))))**2
def orthogonality(x, n, m, a):
    """Product of wavefunctions to check orthogonality and normalisation"""
    return (((hermite(n)(x/a))*np.exp(-x**(2.)/(2.*a**2)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi*a**2)))*((hermite(m)(x/a))*np.exp(-x**(2.)/(2.*a**2)))/(np.sqrt((2.)**(m)*factorial(m)*np.sqrt(np.pi*a**2))))
def expect_val(x,n, a):
    """Mean value: <x>"""
    return x*(((hermite(n)(x/a))*exp(-x**(2.)/(2.*a**(2))))/(sqrt((2.)**(n)*factorial(n)*sqrt(pi*a**2))))**2
def expect_val_squared(x, n, a):
    """Mean value squared: <x>^2"""
    return x**(2.)*(((hermite(n)(x/a))*np.exp(-x**(2.)/(2.*a**2)))/(np.sqrt((2.)**(n)*factorial(n)*np.sqrt(np.pi*a**2))))**2
#Reduced Planck's constant H bar
h=1.054571e-34
def energy_n(x, n, omega):
    """Energy of wavefunction for quantum number n"""
    return (n+0.5)*h*omega+(x*0)
def energy_m(x, m, omega):
    """Energy of wavefunction for quantum number m"""
    return (m+0.5)*h*omega+(x*0)
def potential_energy(x, omega):
    """Potential Energy (parabolic) of the wavefunction (quantum number independent)"""
    return 0.5*omega**(2)*x**(2)
#Defining the class which will create the Home page of the program
class Ciao:
    """
    Class for the introductory home page of the GUI
    Methods:
    -constructor(master):
    sets the class as the master,
    adds a picture to the main page,
    creates button that will open the interactive part of the program,
    creates button that closes the program,
    creates button that links to the LaTex report,
    creates introduction to the program
    -ciao_click(): creates the window where the program (QuantumHarmonicOscillator class) will run
    -close_window(): closes the Home page and hence the program
    -latex_click(): opens the LaTex report
    Usage: Creates the frame that will hold the program and sets its functionalities and layout
    """
    def __init__(self, master):
        "Constructor for the main page of the GUI"
        #Creating and personalizing the master frame
        self.master = master
        self.frame=Frame(self.master, bg='chocolate')
        self.frame.grid()
        self.photo=PhotoImage(file='atom.gif')
        self.start=Label(self.frame, image=self.photo)
        self.start.grid(row=1, column=0)
        #Creating buttons to open and close the program and for the LaTex report
        self.ciao=Button(self.frame, text='CLICK TO START', command=self.ciao_click)
        self.ciao.grid(row=0,column=0)
        self.bye= Button(self.frame, text='QUIT', command=self.close_window)
        self.bye.grid(row=1, column=1)
        self.latex=Button(self.frame, text='LEARN MORE', command=self.latex_click)
        self.latex.grid(row=2, column=0)
        #Creating introduction to the program
        text = Text(self.frame)
        text.config(state=NORMAL)
        text.insert(INSERT,'THE QUANTUM HARMONIC OSCILLATOR \nThis program is designed to show some of the fundametal \nfeatures of the quantum harmonic oscillator. \nThe quantum harmonic oscillator is the quantum-mechanical analogy \nof the classical harmonic oscillator. \nBecause an arbitrary potential can usually be approximated as a harmonic \npotential at the proximity of a stable equilibrium point, it is one of the most \nimportant model systems in quantum mechanics.\nFurthermore, it is one of the few quantum-mechanical systems for which \nan exact, analytical solution is known. \nThe quantum harmonic oscillator is very different from its \nclassical counterpart: \n-The energies are quantised, \n-the probability of finding the particle outside the classical\nallowed region is not zero, \n-In all odd states the probability of finding the particle at\nthe centre of the potential well is zero. \nIf you want to see some of these properties CLICK START, or if you want \na deeper insight click LEARN MORE.')
        text.config(state=DISABLED)     #Prevents the user to modify the text
        text.grid(column=1, row=0)
    def ciao_click(self):
        "Click button to run QuantumHarmonicOscillator's class in a new window"
        self.window= Toplevel(self.master)      #A widget container placed in a new top level window
        self.app =QuantumHarmonicOscillator(self.window)
    def close_window(self):
        "Click button to close program"
        self.master.destroy()
    def latex_click(self):
        "Click button to open the LaTex report"
        webbrowser.open_new('report.pdf')
class QuantumHarmonicOscillator:
    """
    Creates the program that will show the quantum harmonic oscillator features
    The Methods MakePlot and MakeIputs creates the canvas and the input frame respectively,
    those two are the only methods which are not used as button commands.
    All other methods are created to be commands for buttons.
    The Objects sets labels, buttons and their geometry (position).
    """
    def __init__(self,master):
        "Constructor: defines methods to create the sections of the program"
        frame=Frame(master)
        frame.pack()
        self.makePlot(frame)
        self.makeInputs(frame)
    def makePlot(self, frame):
        """Sets the figure and the canvas where the functions are plotted"""
        self.figure = Figure(figsize=(7,6), dpi=100, facecolor='goldenrod')
        self.figPlot = self.figure.add_subplot(111)                 #makes a figure object
        self.canvas = FigureCanvasTkAgg(self.figure, frame)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row = 0, column = 0)       #the get_tk_widget.grid places the canvas coordinates to be (0,0) of the master frame
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, frame)   #adds a standard plot toolbar
        self.toolbar.update()
        self.toolbar.grid(row = 7, column = 0)
    def makeInputs(self, frame):
        """
        Creates the following input frames:
        InputFrame 1: frame that holds buttons to adjust plot inputs
        InputFrame 2: frame that holds buttons with plotting options
        InputFrame 3: frame that holds informations about plots and some results
        Sets the buttons,the labels ,the text box into the input frames.
        """
        #Creating Inputframes
        self.inputFrame=Frame(frame)
        self.inputFrame.grid(row=8, column=0)
        self.inputFrame2=Frame(frame)
        self.inputFrame2.grid(row=0, column=2)
        self.inputFrame3=Frame(frame)
        self.inputFrame3.grid(row=0, column=5)
        #Create text boxes for the title and the comments of the plots
        self.title= StringVar()
        self.text = Label(self.inputFrame3, textvariable = self.title, wraplength=300)
        self.title.set("")        #This allows to change the title of when different buttons are pressed
        self.text.grid(column= 3, columnspan=3, row=0)
        self.content= StringVar()
        self.text = Label(self.inputFrame3, textvariable = self.content, wraplength=300)
        self.content.set("")        #This allows to change the content of the text box when different buttons are pressed
        self.text.grid(column= 3, columnspan=3, row=2)
        #Labels for input variables
        self.labeln = Label(self.inputFrame, text = "Value of n", justify=LEFT)   #justify= defines how to align multiple lines of text
        self.labeln.grid(column= 0, row= 1)
        self.labelm = Label(self.inputFrame, text = "Value of m", justify=LEFT)
        self.labelm.grid(column= 0,row= 2)
        self.labela = Label(self.inputFrame, text = "Value of a", justify=LEFT)
        self.labela.grid(column= 0,row= 3)
        self.labelomega = Label(self.inputFrame, text = "Angular frequency", justify=LEFT)
        self.labelomega.grid(column= 4, row= 1)
        #Sliders for input variables, so the user is able to chose values between the fixed range
        self.entern = Scale(self.inputFrame, from_=0, to=30, orient=HORIZONTAL)   #Sliders are extremely usefull in this case as I can fix the min and max value allowed
        self.entern.grid(column = 1, row = 1)
        self.enterm = Scale(self.inputFrame, from_=0, to=30, orient=HORIZONTAL)
        self.enterm.grid(column = 1, row = 2)
        self.entera = Scale(self.inputFrame, from_=1, to=10, orient=HORIZONTAL)
        self.entera.grid(column = 1, row = 3)
        self.enteromega= Scale(self.inputFrame, from_=1, to=20, orient=HORIZONTAL)
        self.enteromega.grid(column = 5, row = 1)
        #Button to create plots
        self.Plot_psi = Button(self.inputFrame2, text ='WAVEFUNCTION', command = self.Wavefunction)
        self.Plot_psi.grid(column = 2, columnspan=3, row = 0)
        self.Plot_prob= Button(self.inputFrame2, text='QUANTUM PROBABILITY', command=self.QuantumProb)
        self.Plot_prob.grid(column= 2, columnspan=3, row=1)
        self.Plot_probclass= Button(self.inputFrame2, text='CLASSICAL PROBABILITY', command=self.ClassicalProb)
        self.Plot_probclass.grid(column= 2, columnspan=3, row=2)
        self.Plot_compare= Button(self.inputFrame2, text='COMPARE PROBABILITY DENSITIES', command=self.Compare)
        self.Plot_compare.grid(column= 2, columnspan=3, row=3)
        self.Plot_energy= Button(self.inputFrame2, text='ENERGY', command=self.Energy)
        self.Plot_energy.grid(column=2, columnspan=3, row=4)
        self.Plot_potential=Button(self.inputFrame2, text='POTENTIAL ENERGY', command= self.Potential)
        self.Plot_potential.grid(column=2, columnspan=3, row=5)
        #Buttons for calculations
        self.Calc_orthog= Button(self.inputFrame2, text='ORTHOGONALITY AND NORMALISATION', command= self.Orthogonality)
        self.Calc_orthog.grid(column=2, columnspan=3, row=6)
        self.Calc_mean= Button(self.inputFrame2, text='EXPECTATION VALUE FOR THE POSITION', command= self.MeanPosition)
        self.Calc_mean.grid(column=2, columnspan=3, row=7)
        #Buttons to help the user adjust paraeters
        self.help_n=Button(self.inputFrame, text="?", command=self.helpme_n)
        self.help_n.grid(column=3, row=1)
        self.help_m=Button(self.inputFrame, text="?", command=self.helpme_m)
        self.help_m.grid(column=3, row=2)
        self.help_a=Button(self.inputFrame, text="?", command=self.helpme_a)
        self.help_a.grid(column=3, row=3)
        self.help_omega=Button(self.inputFrame, text="?", command=self.helpme_omega)
        self.help_omega.grid(column=6, row=1)
        #Buttons to help the user with the program
        self.helpwavefunction=Button(self.inputFrame2, text='?', command=self.help_wavefunction)
        self.helpwavefunction.grid(column=4, row=0)
        self.helpquantump=Button(self.inputFrame2, text='?', command=self.help_quantump)
        self.helpquantump.grid(column=5, row=1)
        self.helpclassicalp=Button(self.inputFrame2, text='?', command=self.help_classicalp)
        self.helpclassicalp.grid(column=5, row=2)
        self.helpcomparep=Button(self.inputFrame2, text='?', command=self.help_comparep)
        self.helpcomparep.grid(column=5, row=3)
        self.helpenergy=Button(self.inputFrame2, text='?', command=self.help_energy)
        self.helpenergy.grid(column=4, row=4)
        self.helppotential=Button(self.inputFrame2, text='?', command=self.help_potential)
        self.helppotential.grid(column=5, row=5)
        self.helporthogonality=Button(self.inputFrame2, text='?', command=self.help_orthogonality)
        self.helporthogonality.grid(column=5, row=6)
        self.helpdeltax=Button(self.inputFrame2, text='?', command=self.help_deltax)
        self.helpdeltax.grid(column=5, row=7)
    def Wavefunction(self):
        """Plots the wavefunctions for quantum numbers n and m using the variables chosen by the user,
        adds legend and shows the plots in the canvas"""
        self.n = int(self.entern.get())
        self.m = int(self.enterm.get())
        self.a = float(self.entera.get())
        self.x = np.linspace(-20, 20, 100000)
        #Clear the calculated data so that different plots won't overlap
        self.figPlot.clear()
        #Adding a picture to show the formula
        self.image=PhotoImage(file='wavefunction.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        #Setting text to show when plotting wavefunctions
        self.title.set("WAVEFUNCTION")
        self.content.set("Note that the wavefunctions for higher quantum number have more humps within the potential well. This corresponds to a shorter wavelength and therefore by the deBroglie relationship they may be seen to have a higher momentum and therefore higher energy.")
        #Plotting wavefunctions and setting labels, title and legend
        self.plot_n = self.figPlot.plot(self.x, psi_n(self.x, self.n, self.a), label='Wavefunction for n={}' .format(self.n), color='red')
        self.plot_m = self.figPlot.plot(self.x, psi_m(self.x, self.m, self.a), label='Wavefunction for m={}' .format(self.m), color='orange')
        self.figPlot.legend(loc="upper right",prop={'size':7})
        self.figPlot.set_title('Wavefunction for harmonic oscillator', size=11)
        self.figPlot.set_ylabel('Wavefunction', size=11)
        self.figPlot.set_xlabel('x', size=11)
        self.canvas.show()
    def QuantumProb(self):
        """Plots probability density for quantum numbers n and m, using the variables chosen by the user,
        adds legend and shows the plots in the canvas"""
        self.n=int(self.entern.get())
        self.m=int(self.enterm.get())
        self.a=float(self.entera.get())
        self.x=np.linspace(-20,20,100000)
        self.figPlot.clear()
        #Adding a picture to show the formula
        self.image=PhotoImage(file='probabilitydensity.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        #Setting text to show when plotting probability densities
        self.title.set("QUANTUM PROBABILITY")
        self.content.set("The quantum probability for a QHO is different from zero in the classically forbidden regions.To find the total probability, the probability density has to be integrated with -infinity and +infinity limits. The total probability should be 1 by definition,  and this is the case if the wavefunction is normalised.")
        #get the values of the variable")
        #Plotting quantum probabilities and setting labels, title and legend
        self.quantum_n=self.figPlot.plot(self.x, quantumprob_n(self.x, self.n, self.a), label='Quantum probability for n={}' .format(self.n), color='red')
        self.quantum_m=self.figPlot.plot(self.x, quantumprob_m(self.x, self.m, self.a), label='Quantum probability for m={}'.format(self.m),color='orange' )
        self.figPlot.legend(loc="upper right", prop={'size':7})
        self.figPlot.set_title('Quantum probability for harmonic oscillator', size=11)
        self.figPlot.set_ylabel('Probability', size=11)
        self.figPlot.set_xlabel('x', size=11)
        self.canvas.show()
    def ClassicalProb(self):
        """Plots classical probability density using the variables chosen by the user,
        adds legend and shows the plots in the canvas"""
        self.n=int(self.entern.get())
        self.m=int(self.enterm.get())
        self.x=np.linspace(-20,20,100000)
        self.figPlot.clear()
        #Adding a picture to show the formula
        self.image=PhotoImage(file='classicalprobability.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        #Setting text to show when plotting probability densities
        self.title.set("CLASSICAL PROBABILITY")
        self.content.set("The classical probability for a harmonic oscillator increases as an exponential at the ends of the motion. It is given by P(x)=1/(pi*sqrt((2*n)+(1)-x^2)) and hence it depends on the diplacement from the equilibrium position and on the quantum number n.")
        #Plotting quantum probabilities and setting labels, title and legend
        self.classical_n=self.figPlot.plot(self.x, classprob_n(self.x, self.n), label='Classical probability for n={}' .format(self.n), color='red')
        self.classical_m=self.figPlot.plot(self.x, classprob_m(self.x, self.m), label='Classical probability for m={}'.format(self.m),color='orange' )
        self.figPlot.legend(loc="upper right", prop={'size':7})
        self.figPlot.set_title('Classical probability for harmonic oscillator', size=11)
        self.figPlot.set_ylabel('Probability', size=11)
        self.figPlot.set_xlabel('x', size=11)
        self.canvas.show()
    def Compare(self):
        self.n=int(self.entern.get())
        self.m=int(self.enterm.get())
        self.a=float(self.entera.get())
        self.x=frange(-10, 10, 0.05)        #Values for x is different from the other parts of the program to make the two probabilities easier to compare
        self.figPlot.clear()
        #Adding a picture to show the formula
        self.image=PhotoImage(file='cat.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        #Setting text to show when plotting probability densities
        self.title.set("COMPARISON BETWEEN CLASSICAL AND QUANTUM PROBABILITY")
        self.content.set("The quantum probability extend into the classically forbidden region, exponentially decaying into that region. Note that in the classical case, the probability is greatest at the ends of the motion since it is moving more slowly and comes to rest instantaneously at the extremes of the motion. For low values of the quantum number there is a little resemblance between the quantum and classical probabilities. For higher quantum numbers the quantum and classical case look more alike.")
        #Plotting quantum probabilities and setting labels, title and legend
        self.quantum_n=self.figPlot.plot(self.x, quantumprob_n(self.x, self.n, self.a), label='Quantum probability for n={}' .format(self.n), color='red')
        self.quantum_m=self.figPlot.plot(self.x, quantumprob_m(self.x, self.m, self.a), label='Quantum probability for m={}'.format(self.m),color='orange' )
        self.classical_n=self.figPlot.plot(self.x, classprob_n(self.x, self.n), label='Classical probability for n={}' .format(self.n), color='blue')
        self.classical_m=self.figPlot.plot(self.x, classprob_m(self.x, self.m), label='Classical probability for m={}'.format(self.m),color='green' )
        self.figPlot.legend(loc="upper right", prop={'size':7})
        self.figPlot.set_title('Comparison between classical and quantum probabilty', size=11)
        self.figPlot.set_ylabel('Probability', size=11)
        self.figPlot.set_xlabel('x', size=11)
        self.canvas.show()
    def Energy(self):
        """Plots energies for quantum numbers n and m, using the variables chosen by the user,
        adds legend and shows the plots in the canvas"""
        self.n=int(self.entern.get())
        self.m=int(self.enterm.get())
        self.omega=float(self.enteromega.get())
        self.x=np.linspace(-10,10,100000)
        self.figPlot.clear()
        #Adding a picture to show the formula
        self.image=PhotoImage(file='energy.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        #Setting text to show when plotting energies
        self.title.set("ENERGY")
        self.content.set("Note that the energy is constant with x and so its plot gives a straight horizontal line. The lowest energy level is called ground state and it's always greater than zero. This is because of the Uncertainy Principle which requires a particle to have some kinetic energy.")
        #Plotting energies and setting labels, title and legend
        self.energ_n=self.figPlot.plot(self.x, energy_n(self.x, self.n, self.omega), label='Energy for n={}' .format(self.n), color='red')
        self.energ_m=self.figPlot.plot(self.x, energy_m(self.x, self.m, self.omega), label='Energy for m={}'.format(self.m),color='orange' )
        self.figPlot.legend(loc="center", prop={'size':7})
        self.figPlot.set_title('Energy for harmonic oscillator', size=11)
        self.figPlot.set_ylabel('Energy/ Joules', size=11)
        self.figPlot.set_xlabel('x', size=11)
        self.canvas.show()
    def Potential(self):
        """Plots the potential energy using the variables chosen by the user,
        adds legend and shows the plots in the canvas"""
        self.omega=float(self.enteromega.get())
        self.x=np.linspace(-20,20,100000)
        self.figPlot.clear()
        #Adding a picture to show the formula
        self.image=PhotoImage(file='potential.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        #Setting text to show when plotting potential
        self.title.set("POTENTIAL ENERGY")
        self.content.set("Note that the potential energy is parabolic. When the potential energy increases the kinetic energy dicreases and vice versa so that the total energy remains constant.")
        #Plotting potential energy and setting labels, title and legend
        self.potent=self.figPlot.plot(self.x, potential_energy(self.x, self.omega), label='Potential Energy for omega={}' .format(self.omega), color='red')
        self.figPlot.legend(loc="upper right", prop={'size':7})
        self.figPlot.set_title('Potential Energy for harmonic oscillator', size=11)
        self.figPlot.set_ylabel('Potential Energy/ Joules', size=11)
        self.figPlot.set_xlabel('x', size=11)
        self.canvas.show()
    def Orthogonality(self):
        self.n=int(self.entern.get())
        self.m=int(self.enterm.get())
        self.a=float(self.entera.get())
        self.x=np.linspace(-20,20,100000)
        self.figPlot.clear()
        #Adding a picture to show the formula
        self.image=PhotoImage(file='normalisation.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        self.title.set("ORTHOGONALITY AND NORMALISATION \nThe integral is equal to 1 when n=m which means that the wavefunctions are normalised.The integral is equal to zero when n is different from m which means that the wavefunctions are orthogonal")
        self.iprod, self.err = quad(orthogonality, -100, 100, args=(self.n, self.m, self.a))
        #Print the results.
        self.content.set('When n is ' + repr(self.n) + ',m is ' + repr(self.m) + ', and a is ' + repr(self.a) + ', the integral of the wavefunctions is equal to ' + repr(self.iprod) + ' with error: ' + repr(self.err))
    def MeanPosition(self):
        self.n=int(self.entern.get())
        self.a=float(self.entera.get())
        self.x=np.linspace(-20,20,100000)
        #Adding a picture to show the formula
        self.figPlot.clear()
        self.image=PhotoImage(file='deltax.gif')
        self.image1=Label(self.inputFrame3, image=self.image)
        self.image1.grid(column=3, row=1)
        self.mean_x, self.errmean_x = quad(expect_val, -50, 50, args=(self.n, self.a))
        self.mean_x2, self.errmean_x2 = quad(expect_val_squared, -100, 100, args=(self.n, self.a))
        #Find the uncertainty in x using the above results
        self.uncertainty_x = sqrt((self.mean_x2)-(self.mean_x)**2.)
        self.title.set("UNCERTAINTY IN POSITION")
        self.content.set('-The expectation value for the position:\n <X> is ' +repr(self.mean_x) +' with an error of ' + repr(self.errmean_x)+'\n -The expectation value for the position squared:\n <X^2> is ' +repr(self.mean_x2) +' with an error of ' + repr(self.errmean_x2)+'\n -The uncertainty in the position:\n Delta(X) is then ' +repr(self.uncertainty_x))
    #Defining functions to show information for the help buttons
    def helpme_n(self):
        "Show info for n"
        tkMessageBox.showinfo(title='QUANTUM NUMBER N', message="All the features studied in this program can be modified by changing the quantum number. As the quantum number increases the QHM merges to the CHM according to the correspondence principles. In this program the maximum allowed value of n has been fixed.")
    def helpme_m(self):
        "Show info for m"
        tkMessageBox.showinfo(title='QUANTUM NUMBER M', message="All the features studied in this program can be modified by changing the quantum number. As the quantum number increases the QHM merges to the CHM according to the correspondence principles. In this program the maximum allowed value of m has been fixed.")
    def helpme_a(self):
        "Show info for a"
        tkMessageBox.showinfo(title='VALUE OF A', message="The value of A depends on the mass, the angular frequency and the planck's constant. Hence this value cannot be zero. In this program the range for A has been fixed.  ")
    def helpme_omega(self):
        "Show info for omega"
        tkMessageBox.showinfo(title='ANGULAR FREQUENCY OMEGA', message="The angular frequency determines the potential energy and the energy, but doesn't affect the other features. This is because the energy is proportional to the angular frequency and to the placnk's constant. In this program the range for omega has been fixed.")
    def help_wavefunction(self):
        'Show info on wavefunction'
        tkMessageBox.showinfo(title='WAVEFUNCTION', message='The Wavefunction is the solution to the Schrodinger equation for the harmonic oscillator. It can be plotted with two quantum numbers n and m.' )
    def help_quantump(self):
        'Show info on quantum probability'
        tkMessageBox.showinfo(title='QUANTUM PROBABILITY', message='The probability of finding a quantum particle at any given value of x is given by the wavefunction squared. This probability can be plotted for different wavefunctions for quantum numbers n and m and for different values of a.' )
    def help_classicalp(self):
        'Show info on classical probability'
        tkMessageBox.showinfo(title='CLASSICAL PROBABILITY', message='The probability of finding an object in any interval dx is just the inverse of its average velocity over that interval. This probability can be plotted for different wavefunctions for quantum numbers n and m. Changing the value for a does not affect this probability. ' )
    def help_comparep(self):
        'Show info on classical vs quantum probability'
        tkMessageBox.showinfo(title='CLASSICAL vs QUANTUM PROBABILITY', message='The QHO is a good example of how different the quantum and the classical results can be. In this program it is possible to compare the probability density for both cases, for quantum numbers n and m. Changing the value for a the quantum probability spreads out.' )
    def help_energy(self):
        'Show info on energy'
        tkMessageBox.showinfo(title='ENERGY', message='The energies for the quantum harmonic oscillator are quantised, hence they have only discrete values. The ground state energy is given by the quantum number=0. In this program the energy can be modified changing the values of n,m or omega.' )
    def help_potential(self):
        'Show info on potential energy'
        tkMessageBox.showinfo(title='POTENTIAL ENERGY', message='The potential energy is parabolic and independent of the quantum number. It does depend on the mass, the displacement from the equilibrium position and the angular frequency. In this program it can be modified changing the value of omega.' )
    def help_orthogonality(self):
        'Show info on orthogonality'
        tkMessageBox.showinfo(title='ORTHOGONALITY', message='The wavefunctions have to be orthogonal and normalized in order to be acceptable. to check this the integral from 0 to L of the complex conjugate of psi_m times psi_n has to be Kronecker delta_mn. In this program it is sufficient changing the values for n, m or a.' )
    def help_deltax(self):
        'Show info on deltaX'
        tkMessageBox.showinfo(title='UNCERTAINTY IN X', message='As the expectation value for position <x> is zero, the delta x is just given by the square root of the expectation velue for the position squared.' )
root=Tk()
root.wm_title("FINAL PROJECT: THE QUANTUM HARMONIC OSCILLATOR")
hello=Ciao(root)
root.mainloop()
