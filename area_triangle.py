def area(vertices): return (1.0/2)*(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1)
v1= ('x1','y1'); v2= ('x2','y2'); v3= ('x3','y3')
x1= 0; y1= 0; x2= 1; y2= 0; x3=0; y3=2
vertices= [v1, v2, v3]
triangle1= area(vertices)
print 'Area of triangle is %.2f' %triangle1
"Area of triangle is 1.00"
