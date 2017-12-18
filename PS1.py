import math
print dir(math)
"['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']"
"EXERCISE 3"
x= math.sqrt(17.0)

print x
"4.12310562562"
z= math.factorial(18)

print z
"6402373705728000"

y= math.sin(33)

print y
"0.999911860107"
"EXERCISE4"
height= float(raw_input("Enter the tower height: "))

"Enter the tower height: 20"

time= float(raw_input("Enter the time interval: "))

"Enter the time interval: 2"
h= height-4.905*time**2
print "The height of the ball from the ground: %2f" %h
"The height of the ball from the ground: 0.38"
"""
EXERCISE 5
Show H=((GMT^2)/4Pi^2)^(1/3)-R
v= omega*r
r= R+H
omega= 2Pi/T
using Newton's second Law for circular motion
(1/2)mv^2=(GMm)/(R+H)
substituting the expression for the velocity and the angular velocity and rearranging
H=((GMT^2)/4Pi^2)^(1/3)-R
"""
R= 6371*1000
x= -11
y= 24
z= 1.0/3
M= 5.97*10**y
G= 6.67*10**x
period= float(raw_input("Enter the satellite's period: "))
"Enter the satellite's period: 35000000"
H= ((G*M*(period**2))/4*(math.pi**2)**z)-R
print "The height of the satellite: %.2f " %H
"""
The height of the satellite: 121948443749999977466423148544.00
Enter the satellite's period: 1440
The height of the satellite: 206426361599993610240.00 
Enter the satellite's period: 5400
The height of the satellite: 2902870709999993094144.00 
Enter the satellite's period: 2700
The height of the satellite: 725717677499993423872.00 
The conclusion is that Kepler's Third Law which predicts the proportionality between period and orbit radius is valid
hence H is proportional to T^2/3
"""
"EXERCISE 6"
fo = open ("foo.txt" , "wb")
fo.write( "In all cases in which work is produced by the agencyof heat, a quantityof heat is consumed which is proportional to the work done;and conversely, by the expediture of an equal quantity of work an equal quantity of heat is produced") ;
fo.close()
f1= open ("foo.txt", "r")
"In all cases in which work is produced by the agencyof heat, a quantityof heat is consumed which is proportional to the work done;and conversely, by the expediture of an equal quantity of work an equal quantity of heat is produced"
string= f1.read()
print string[7]
"c"