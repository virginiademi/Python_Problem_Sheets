import mayavi as may
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
"EXERCISE 1"
Ex1a=np.zeros((4,4))
print Ex1a
"""
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
 """
Ex1b=np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
print Ex1b
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
"""
Ex1c=np.random.rand(4,4)
print Ex1c
"""
[[ 0.87857404  0.19077504  0.03689595  0.38033618]
 [ 0.14784545  0.90540717  0.57517554  0.16716537]
 [ 0.51152911  0.64020953  0.46483858  0.73494941]
 [ 0.31993644  0.2565937   0.51819691  0.16116351]]
"""

row1=np.linspace(1,17, num=4)
print row1
"[  1.           6.33333333  11.66666667  17.        ]"
row2=np.linspace(1,2, num=4)
print row2
"[ 1.          1.33333333  1.66666667  2.        ]"
row3=np.linspace(100,200, num=4, endpoint=False)
print row3
"[ 100.  125.  150.  175.]"
row4=np.linspace(100,200, num=4)
print row4
"[ 100.          133.33333333  166.66666667  200.        ]"
Ex1d=np.array([[row1],[row2],[row3],[row4]])
"""
[  1.           6.33333333  11.66666667  17.        ]
[ 1.          1.33333333  1.66666667  2.        ]
[ 100.  125.  150.  175.]
[ 100.          133.33333333  166.66666667  200.        ]
"""
Ex1e=Ex1a + Ex1b + Ex1c
print Ex1e
"""
[[  1.30834763   2.72473369   3.43455526   4.17806779]
 [  5.87513039   6.84144923   7.68072185   8.61670526]
 [  9.50631351  10.53135618  11.3848775   12.74683125]
 [ 13.38009196  14.08798046  15.73648538  16.5590564 ]]
"""
print Ex1e [2:3,0:4]
"[[  9.50631351  10.53135618  11.3848775   12.74683125]]"
Ex1f= Ex1b*Ex1b
print Ex1f
"""[[  1   4   9  16]
 [ 25  36  49  64]
 [ 81 100 121 144]
 [169 196 225 256]]
"""
dotprod=np.dot(Ex1b, Ex1b)
print dotprod

"""[[ 90, 100, 110, 120],
       [202, 228, 254, 280],
       [314, 356, 398, 440],
       [426, 484, 542, 600]]
"""
test=dotprod - Ex1f
print test
"""[[ 89  96 101 104]
 [177 192 205 216]
 [233 256 277 296]
 [257 288 317 344]]
"""
print '"Ex1f" is the product of each element of Ex1b with itself; "dotprod" is the row-column multiplication of Ex1b' 
Ex1g= np.sin(Ex1c)**2
print Ex1g
"""[[ 0.12637617  0.00064238  0.23372812  0.50605532]
 [ 0.46441913  0.09378957  0.24979897  0.60898153]
 [ 0.58616569  0.2300743   0.35785742  0.50253525]
 [ 0.17378932  0.47567657  0.01113533  0.00586027]]
 """
Ex1c.T
"""array([[ 0.36344282,  0.7497872 ,  0.87199615,  0.43001062],
       [ 0.02534786,  0.31125212,  0.50026789,  0.76106513],
       [ 0.50459661,  0.52336661,  0.64126779,  0.10572091],
       [ 0.79145364,  0.89526159,  0.78793342,  0.07662734]])
"""
np.diag(Ex1c)
"array([ 0.36344282,  0.31125212,  0.64126779,  0.07662734])"
np.vstack((Ex1a,Ex1b))
"""array([[  0.,   0.,   0.,   0.],
       [  0.,   0.,   0.,   0.],
       [  0.,   0.,   0.,   0.],
       [  0.,   0.,   0.,   0.],
       [  1.,   2.,   3.,   4.],
       [  5.,   6.,   7.,   8.],
       [  9.,  10.,  11.,  12.],
       [ 13.,  14.,  15.,  16.]])
"""
np.hstack((Ex1a,Ex1c))
"""array([[ 0.        ,  0.        ,  0.        ,  0.        ,  0.36344282,
         0.02534786,  0.50459661,  0.79145364],
       [ 0.        ,  0.        ,  0.        ,  0.        ,  0.7497872 ,
         0.31125212,  0.52336661,  0.89526159],
       [ 0.        ,  0.        ,  0.        ,  0.        ,  0.87199615,
         0.50026789,  0.64126779,  0.78793342],
       [ 0.        ,  0.        ,  0.        ,  0.        ,  0.43001062,
         0.76106513,  0.10572091,  0.07662734]])
"""
"EXERCISE 2"
sd= np.loadtxt('stars.dat')
x,y=sd[:,0],sd[:,1]
plt.scatter(x,y)
plt.xlabel('Temperature')
plt.ylabel('Magnitude')
plt.title('Hertzsprung-Russell Diagram')
plt.xlim(16000,0)
plt.ylim(20,-5)
plt.figure()
"EXERCISE 3"
STM=np.loadtxt('stm.dat', float)
plt.imshow(STM)
plt.show()