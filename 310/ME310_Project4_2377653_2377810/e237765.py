import numpy as np
from f import f
from fp import a
from fp import b
from fp import E_s
import matplotlib.pyplot as plt
n = 0
E_a = 1
I_plot = []
f_a = f(a)
f_b = f(b)
count = 2 ## counting started from 2 because of f_a and f_b
print(' Trapezodial Rule:')
while E_a>E_s:
    Sum = 0
    I = 0
    if n == 0:
        n=1
    else:
        n = n*2
    h = (b-a)/n
    for i in range(1,n):
        Sum = Sum + f(a+h*i)
        count += 1       
    I = (h/2)*(f_a+2*Sum+f_b)
    I_plot.append(I)
    E_a = abs(((h**2)/12)*I)
    E_a_p = E_a*100
    print('Segment n: %1.4g' %n,'\t\t Integral values: %1.10g'%I,
          '\t\tApproximate Error: %1.2g' %E_a_p)
    
print('Trapezodial Rule number of function evaluation: ', count)

n = 0
E_a = 1
I_plot2 = []
c1 = 5/9
c2 = 8/9
c3 = 5/9
x1 = -np.sqrt(3/5)
x2 = 0
x3 = np.sqrt(3/5)
print(' \n Gauss Quadrature Rule:')

while E_a>E_s:
    I_old = I
    I = 0
    n +=1
    for i in range(1,(n+1)):
        x_l = a+((b-a)/n)*(i-1)
        x_u = x_l +(b-a)/n
        I = I + (x_u-x_l)/2*(c1*f((x_u+x_l)/2+(x_u-x_l)/2*x1)
                             +c2*f((x_u+x_l)/2+(x_u-x_l)/2*x2)
                             +c3*f((x_u+x_l)/2+(x_u-x_l)/2*x3))
    I_plot2.append(I)
    if n == 1:
        E_a = 1
        print('Segment n: %1.4g' %n,'\t\t Integral values: %1.10g'%I,
              'Approximate Error: -' )
    else:
        E_a = (I-I_old)/I
        E_a_p = E_a*100
        print('Segment n: %1.4g' %n,'\t\t Integral values: %1.10g'%I,
              'Approximate Error: %1.2g' %E_a_p)
        
import scipy.integrate as spi
integrand = lambda x : np.exp(x)
a = 1.5
b = 2.5

result, none = spi.fixed_quad(integrand, a, b, n=5)
print('\n Result from built in function is: ', result)

plt.plot(I_plot, 'g*', I_plot2, 'ro')
plt.title('Trapezoidal vs Gauss Quadrature')
plt.xlabel('number of segments (n for Gauss, 2^n for Trapazoidal)')
plt.ylabel('Calculated integral values I')
plt.show()











    