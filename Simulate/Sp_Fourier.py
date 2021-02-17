import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import time
#import sys                                                  #<--|Ignore
#sys.path.insert(0,'E:\Worm-Whole\Project\Engine\calculas')  #   |those
#from Intrigation import Intriga                             #<--|lines

def Intriga(function,upper,lower):
    """
    Copyright (C)  2020  Noatic Digital LLB. All rights reserved.

    Returns Intrigation  of a given function.

    Returns Inrigral value of `function` for certain `upper` and `lower`.

    ..version:: 1.0.2

    ..author :: Suman Mandal

    Parameters
    ----------
    function : string 
        Function followed by string i.e, numpy [accessable] 
    Upper : float
        Upper limit of the intrigation
    Lower : float 
        Lower limit of the intrigation
    Returns
    -------
        The intrigral value of the function.
    """
    n=1001
    x=np.linspace(lower,upper,n)
    def g(x):
        return eval(function)
    h=(upper-lower)/n
    y=0
    for i in range(0,n-2,2):
        y=y+(h/3.0)*(g(x[i])+4.0*g(x[i+1])+g(x[i+2]))
    return y

#Input Dash-Board:
n=int(input('No of Cosine and Sine Terms in Your Series : '))
xl=float(input('Lower Limit of the function : '))
xu=float(input('Upper Limit of the function : '))
m=int(input('No of data point : '))

#Time Period:
T=abs(xl-xu)
t=T/2.0

#Function Junction : 

print('Give The equation for Fourier Analysis')
nh=float(input('Give Discontinued point of the function: '))
z1=input('for, %.5f<x<%.5f , Give the function: '%(xl,nh))
z2=input('for, %.5f<x<%.5f , Give the function: '%(nh,xu))

#Coefficeint : an & bn : [Cosine][Sine]
A=[]
B=[]
for _,i in zip(tqdm (range(n),desc="Calculating a[n] & b[n]",ascii=False, ncols=80),range(n)):
    s=i/t
    an0=(1/t)*Intriga(z1+'*np.cos(np.pi*x*{})'.format(s),nh,xl)
    an1=(1/t)*Intriga(z2+'*np.cos(np.pi*x*{})'.format(s),xu,nh)
    an=an0+an1
    bn0=(1/t)*Intriga(z1+'*np.sin(np.pi*x*{})'.format(s),nh,xl)
    bn1=(1/t)*Intriga(z2+'*np.sin(np.pi*x*{})'.format(s),xu,nh)
    bn=bn0+bn1
    B.append(bn)
    A.append(an)
    time.sleep(0.00001)

#Arrangement Series : 
X=np.linspace(xl,xu,m)
Y=np.zeros(m)
for _,i in zip(tqdm (range(m),desc="Arranging all terms....",ascii=False, ncols=80),range(m)):
    y=0.0
    for j in range(n):
        y=y+A[j]*np.cos(np.pi*j*X[i]*(1.0/t))+B[j]*np.sin(np.pi*j*X[i]*(1.0/t))
    Y[i]=y
    time.sleep(0.00001)

fig,ax=plt.subplots(nrows=1,ncols=1)
ax.plot(X,Y)
#simple ploting style used here:
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Fourier Series Graph')
ax.grid()
plt.show()


