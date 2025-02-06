# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:44:41 2022

@author: Murat Berk     2377653
         Gökberk Çiçek  2377810
"""
import numpy as np
import itertools
import math

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

"""
Gauss Elimination operations (using a lot of storage)
                             (Less storage using code provided as 
                              comment at the bottom of the code)
"""

# forward elimination
def forward(A, b):
  
  # go ever each row except the last one (pivots)
    for k in range(0,N-1,1):  # total N-1
      # go over from row k to n (row number of elimination)
      for i in range(k+1,N,1):   #  total n-k
    
        factor = A[i][k]/A[k][k]  # 1 divison
        # go over each column (column number for elimination)
        for j in range(k,N,1): 
          A[i][j] = A[i][j] - factor*A[k][j]  # n-k x and -
                  
        b[i] = b[i] - factor*b[k] # 1 -> x and -
    return (A, b)

def back(A, b):

    x = np.zeros_like(b)
    x[-1] = b[-1]/A[-1][-1]
    
    # go over each row to n
    for i in range(N-2,-1,-1):
      sum = 0.0
      #go over each column
      for j in range(i+1,N,1):
        sum = sum + A[i][j]*x[j]
      
      x[i] = (b[i] - sum)/A[i][i]
    
    return x


"""
Gauss Seidel operations      (using a lot of storage)
                             (Less storage using code provided as 
                              comment at the bottom of the code)
"""
def seidel(A, b):
    n = 0
    x = np.zeros_like(b)
    error_max = 100000
    error_list = [ 0 for i in range(N)]
    x_old = [ 0 for i in range(N)]
    while n < (Niter+1) and error_max > Tol:
        n += 1
        for i in range(N):
            x_old[i] = x[i]

        for i in range(N):
            SUM = 0
            for k in range(N):
                if i != k:
                    SUM += x[k]*A[i][k]
            x[i] = (b[i]-SUM)/A[i][i]
        for i in range(N):
            if x[i] != 0:  ### not to calculate error with initial condition t = 0
                error_list[i] = abs(x[i]-x_old[i]) / x[i]
                error_max = max(error_list)

    return  x, n

print('for gaus elimination answers are: ')
(A,b) = forward(M,r)
x = back(M, r)
for i in range(N):
    print ('x',i,' :%.10g' %x[i])


x, n = seidel(M, r)
print('for gaus-seidel with',n,'iteration answers are: ')
for i in range(N):
    print ('x',i,' :%.10g' %x[i])
 
"""
###### We can REDUCE the STORAGE USEAGE by implamenting simply this code:
def GaussElim():
    x = [ 0 for i in range(N)]
    x[0] = f(t)   ### First particle position
    x[N-1] = 1    ### Last particle position
    print(x)
    for i in range(1, N-1):
        x[N-(i+1)] = (f(t)/(N-(i+1)) + x[N-(i)]) / ((N - i) / (N - (i+1))) 
    return x
"""
"""
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
"""