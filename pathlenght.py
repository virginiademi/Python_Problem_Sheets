from math import sqrt
def pathlenght(x,y):
    n= len(x)
    lv= [sqrt((x[i]-x[i-1])**2 +(y[i]-y[i-1])**2) for i in range (1,n)]
    L= sum(lv)
    return L  
"TEST FUNCTION"
pts= [(1,1), (2,1), (1,2),(1,1)]
n= len(pts)
x= [pts[i][0] for i in range(n)]
y= [pts[i][1] for i in range(n)] 
print 'Triangular path is %.2f' %pathlenght(x,y)
"Triangular path is 3.41"