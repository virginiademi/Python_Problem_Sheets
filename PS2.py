import math
"EXERCISE 1"
elmnts1 = [ 'Hydrogen' , 'Helium' , 'Lithium' , 'Beryllium' , 'Boron' , 'Carbon' , 'Nitrogen' , 'Oxygen' , 'Fluorine' ,'Neon' ]
print elmnts1
"['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']"
elmnts2 = [ 'Sodium' , 'Magnesium' , 'Aluminum' , 'Silicon' , 'Phosphorus' , 'Sulfur' , 'Chlorine' , 'Argon' , 'Potassium' , 'Calcium' ]
print elmnts2
"['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium']"
print elmnts1 + elmnts2
"['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium']"
elmnts= ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium']
elmnts.append('Scandium')
elmnts.append('Titanium')
elmnts.append('Vanadium')
elmnts.append('Chromium')
elmnts.append('Manganese')
elmnts.append('Iron')
elmnts.append('Cobalt')
elmnts.append('Nickel')
elmnts.append('Copper')
elmnts.append('Zinc')
print elmnts
"['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc']"
print len(elmnts)
"30"
string= elmnts
print string[23]
"Chromium"
"EXERCISE 2"
elements= ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc']
resList= []
for i in elements:
    if i[0]=='S':
        resList.append(i)
print resList
"['Sodium', 'Silicon', 'Sulfur', 'Scandium']"
elements1= ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc']
resList1= []
for m in elements1:
    if len(m) < 5:
        resList1.append(m)
print resList1
"['Neon', 'Iron', 'Zinc']"
"EXERCISE 3"
def area(vertices): return (1.0/2)*(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1)
v1= ('x1','y1'); v2= ('x2','y2'); v3= ('x3','y3')
x1= 0; y1= 0; x2= 1; y2= 0; x3=0; y3=2
vertices= [v1, v2, v3]
triangle1= area(vertices)
print 'Area of triangle is %.2f' %triangle1
"Area of triangle is 1.00"
"EXERCISE 4"
from math import sqrt
def pathlenght(x,y):
    n= len(x)
    lv= [sqrt((x[i]-x[i-1])**2 +(y[i]-y[i-1])**2) for i in range (1,n)]
    L= sum(lv)
    return L 
"TEST FUNCTION"
pts= [(1,1), (2,1), (1,2), (1,1)]
n= len(pts)
x= [pts[i][0] for i in range(n)]
y= [pts[i][1] for i in range(n)] 
print 'Triangular path is %.2f' %pathlenght(x,y)
"Triangular path is 3.41"
"EXERCISE 5"
from math import cos,sin,pi
k= [2,3,4,5,6,7,8,9,10]
for l in k:
    listx = []
    listy = []
    N=2**l 
    i= 0
    while i<=N:
        x= (1.0/2)*cos((2*pi*i)/N)
        y= (1.0/2)*sin((2*pi*i)/N) 
        listx.append(x)
        listy.append(y)
        i+=1 
    print 'Approximate pi is %.2f when' %pathlenght(listx,listy)
    print 'N is equal to:'
    print N
"""
Approximate pi is 2.83 when
N is equal to:
4
Approximate pi is 3.06 when
N is equal to:
8
Approximate pi is 3.12 when
N is equal to:
16
Approximate pi is 3.14 when
N is equal to:
32
Approximate pi is 3.14 when
N is equal to:
64
Approximate pi is 3.14 when
N is equal to:
128
Approximate pi is 3.14 when
N is equal to:
256
Approximate pi is 3.14 when
N is equal to:
512
Approximate pi is 3.14 when
N is equal to:
1024
"""

