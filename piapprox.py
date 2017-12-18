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