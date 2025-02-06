import numpy as np
import itertools
import math
import time

start_time = time.time()

def f(x):                    ####♥ Definition of the first particle function
    return 0.25*math.sin(np.pi*x)

N = input('Enter the number of particles: ')         ### Input taking
N = int(N)
t = input('Enter the time instant: ')                ### Input taking
t = float(t)
Tol = input('Enter the tolerance to terminate: ')    ### Input taking
Tol = float(Tol)
Niter = input('Enter the maximum number of iterations to terminate: ')
Niter = int(Niter)



temp = itertools.count(1)
M = [[next(temp) for i in range(N)] for i in range(N)]   ##Creating coefficient matrix 
r = [[next(temp) for i in range(1)] for i in range(N)]   ##Creating result matrix

"""
Coefficient Matrix is created below
"""
for i in range(N):
    for k in range(N):
        M[i][k] = 0

for i in range(N):
    for k in range(N):
        if i == 0:
            M[i][i] = 1
            if k != 0:
                M[i][k] = 0
        elif i == N-1:
            M[i][i] = 1
            if k != N-1:
                M[i][k] = 0
        else:
            M[i][i-1] = 1
            M[i][i] = -2
            M[i][i+1] = 1
        
"""
Result Matrix is created below
"""
for i in range(N):
    if i == 0:
        r[i] = f(t)
    elif i == N-1:
        r[i] = 1
    else:
        r[i]= 0


###### We can REDUCE the STORAGE USEAGE by implamenting simply this code:
def GaussElim():
    x = [ 0 for i in range(N)]
    x[0] = f(t)   ### First particle position
    x[N-1] = 1    ### Last particle position
    print(x)
    for i in range(1, N-1):
        x[N-(i+1)] = (f(t)/(N-(i+1)) + x[N-(i)]) / ((N - i) / (N - (i+1))) 
    return x

print('for gaus elimination answers are: ')
x = GaussElim()
for i in range(N):
    print ('x',i,' :%.10g' %x[i])

###### We can REDUCE the STORAGE USEAGE by implamenting simply this code:
def seidel():
    n = 0
    x = [ 0 for i in range(N)]
    error_max = 100000
    error_list = [ 0 for i in range(N)]
    x_old = [ 0 for i in range(N)]
    x[0] = f(t)   ### First particle position
    x[N-1] = 1 ### Last particle position
    while n < (Niter+1) and error_max > Tol:
        n += 1
        for i in range(N):
            x_old[i] = x[i]

        for i in range(1,N-1):
            x[i] = (x[i-1]+x[i+1])/2
        
        for i in range(N):
            if x[i] != 0: ### not to calculate error with initial condition t = 0
                error_list[i] = abs(x[i]-x_old[i]) / x[i]
                error_max = max(error_list)
    return  x, n


x, n = seidel(M, r)
print('for gaus-seidel with',n,'iteration answers are: ')
for i in range(N):
    print ('x',i,' :%.10g' %x[i])
    
end_time = time.time()

elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time, "seconds")