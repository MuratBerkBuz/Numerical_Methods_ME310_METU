"""
ME310 Project 1

@author: Murat Berk Buzluk
         2377653
         Gökberk Çiçek
         2377810
         
"""
import numpy               
import math
import sys
"""
We retrieve the wanted function with "from f import f" line
If we change f with fx, our input function become fx
f1 = x^2 - (1-x)^5
f2 = x*e^x - 1
f3 = cos(x) - x^3
f4 = ln(x)
f5 = x^5
f6 = e^(x^2+7x-30) - 1
f7 = x^-1 - sin(x) + 1

initial1 = [0.1,1]
initial2 = [−1,1]
initial3 = [0.1,1]
initial4 = [0.5,50]
initial5 = [-0.5,1/3]
initial6 = [2.8,3.1]
initial7 = [-1.3,-0.5]

"""
from f import f
initial = []     # initial values coming from input file

with open('input.txt','r') as function:          ### input taking section
    content = function.readlines()
    for x in content :
        row = x.split()         
        initial.append(float(row[0]))              ### From there you can change which function gonna be solved 
        """
        row[0] = [0.1,1]
        row[1] = [−1,1]
        row[2] = [0.1,1]
        row[3] = [0.5,50]
        row[4] = [-0.5,1/3]
        row[5] = [2.8,3.1]
        row[6] = [-1.3,-0.5]
        """
"""      
If we change the input.txt file and imported function(f and fd) we can get results of other equations

""" 
xl = initial[0]            # We are using first equation and first initial guesses accordingly. 
xu = initial[1]            # To use other equations initial1 can be changed to initialx
errors = initial[2]        # To use other equations initial1 can be changed to initialx
Niter = initial[3]         # To use other equations initial1 can be changed to initialx
Niter = int(Niter)      #turn Niter from float to integer 

# define a small number for zero check
EPS = 100*(numpy.finfo(numpy.float64).tiny)

# Check validity of data. It are enough to only do once
if (f(xl)*f(xu) > 0 or abs(xl - xu) < EPS):
    print('Please correct initial estimates, exiting...\n')
    sys.exit()

######################              POLYNOMIAL METHOD

print('POLYNOMIAL METHOD:\n')
print('Iter \t\t','xl \t\t\t', 'f(xl) \t\t' ,'xu \t\t\t', 'f(xu) \t\t', 'xi \t\t\t','f(xi) \t\t', 'err(%) \t\t', sep='\t', end = "\n")   # Headers

file = open("output_polynomial.txt", "wt")                  # Output .txt file opened

xi = (xu + xl) ## For initilazing to make first approximate error to 100
for i in range(0,Niter):
    x0i = xi
    xi = (xu + xl)/2
    approxE = (abs((xi - x0i)/xi))*100
        
    print(i,'\t\t', format(xl, '.6e'), format(f(xl), '.6e'), format(xu, '.6e'), \
      format(f(xu), '.6e'), format(xi, '.10e'), format(f(xi), '.6e'), \
      format(approxE, '.6e'), sep='\t', end = "\n")
        
    a = (f(xl)-f(xi))/((xl-xi)*(xl-xu)) + (f(xi)-f(xu))/((xu-xi)*(xl-xu))                     # a value to calculate roots
    b = ((f(xl)-f(xi))*(xi-xu))/((xl-xi)*(xl-xu)) - (f(xi)-f(xu))*(xl-xi)/((xu-xi)*(xl-xu))   # b value to calculate roots
    c = f(xi)                                                                                 # c value to calculate roots
    xr = xi - 2*c/(b+numpy.sign(b)*math.sqrt(b**2-4*a*c))                          # New upper or lower bound calculation
    if math.isnan(f(xi)):
        print('This function cannot be solved by Newton-Rapshon Method')
        break
    """
    Below are the lines for writing output file
    
    """
    outpoly = (i+1, format(xi, '1.8f'), format(f(xi), '1.8f'), format(approxE, '1.2f'))         # Tuple created for output.txt file
    for item in outpoly:
        s = str(item)
        file.write(s+ '\t\t')
    file.write('\n')
    
    if numpy.sign(f(xl))*numpy.sign(f(xr)) < 0:              ### New bound calculation if statement
        xu = xr
    else :
        xl = xr
        
    if approxE < errors :            ### if statement for deciding stop or continue 
        break  
    
file.close()  ### closes the temporary file 

######################              BISECTION METHOD

file = open("output_bisection.txt", "wt")                  # Output .txt file opened
xl = initial[0]        # initilazing
xu = initial[1]        # initilazing
errors = initial[2]    # initilazing
Niter = initial[3]     # initilazing
Niter = int(Niter)      # float to integer trasformation
xi = (xu + xl) 
print('\n BISECTION METHOD:\n')     
print('Iter \t\t','xl \t\t\t', 'f(xl) \t\t' ,'xu \t\t\t', 'f(xu) \t\t', 'xi \t\t\t','f(xi) \t\t', 'err(%) \t\t', sep='\t', end = "\n")   # Headers

for i in range(0,Niter): 
    # copy previous estimate
    x0i = xi
    # update the estimate with bisection and compute error
    xi = (xu + xl)/2 
    approxE = (abs((xi-x0i)/xi))*100
    # damp out info
    print(i,'\t\t', format(xl, '.6e'), format(f(xl), '.6e'), format(xu, '.6e'), \
      format(f(xu), '.6e'), format(xi, '.6e'), format(f(xi), '.6e'), \
      format(approxE, '.6e'), sep='\t', end = "\n")
    if math.isnan(f(xi)):
        print('This function cannot be solved by Newton-Rapshon Method')
        break
    
    """
    Below are the lines for writing output file
    
    """
    outpoly = (i+1, format(xi, '1.8f'), format(f(xi), '1.8g'), format(approxE, '.2g'))         # Tuple created for output.txt file
    for item in outpoly:
        s = str(item)
        file.write(s+ '\t\t')
    file.write('\n')
    
    if (approxE < errors or abs(f(xi))< EPS):              # check the error and terminate iterations if necessary
      break
    # decide new bounds 
    if f(xl)*f(xi) < 0:
      xu = xi
    else :
      xl = xi
file.close()
######################              FALSE POSITION METHOD
file = open("output_falseposition.txt", "wt")                  # Output .txt file opened
from f import fp                              ### Different from open method we used derrivative of the equation
xl = initial[0]        # initilazing
xu = initial[1]        # initilazing
errors = initial[2]    # initilazing
Niter = initial[3]     # initilazing
Niter = int(Niter)      # float to integer trasformation
xi = (xu + xl)   
print('\n FALSE POSITION METHOD:\n')    
print('Iter \t\t','xl \t\t\t', 'f(xl) \t\t' ,'xu \t\t\t', 'f(xu) \t\t', 'xi \t\t\t','f(xi) \t\t', 'err(%) \t\t', sep='\t', end = "\n")       # Headers

for i in range(0,Niter): 
    # copy previous estimate
    xi0 = xi
    # update the estimate with false-position and compute approxEor
    xi = xu  -f(xu)*(xl-xu)/(f(xl) -f(xu)) 
    approxE = abs((xi-xi0)/xi)*100
    
    print(i,'\t\t', format(xl, '.6e'), format(f(xl), '.6e'), format(xu, '.6e'), \
          format(f(xu), '.6e'), format(xi, '.6e'), format(f(xi), '.6e'), \
          format(approxE, '.6e'), sep='\t', end = "\n")
    """
    Below are the lines for writing output file
    
    """
    if math.isnan(f(xi)):
        print('This function cannot be solved by Newton-Rapshon Method')
        break
    
    outpoly = (i+1, format(xi, '1.8g'), format(f(xi), '1.8g'), format(approxE, '1.2g'))
    for item in outpoly:
        s = str(item)
        file.write(s+ '\t\t')
    file.write('\n')
    
    # check approxEor and terminate iterations if necessary
    if (approxE < errors or abs(f(xi))< EPS):
      break
    # Decide on new bounds
    if f(xl)*f(xi) < 0:
        xu = xi
    else :
        xl = xi
file.close()

######################              NEWTON RAPSHON METHOD
file = open("output_newton.txt", "wt")                  # Output .txt file opened
xl = initial[0]        # initilazing
xu = initial[1]        # initilazing
errors = initial[2]    # initilazing
Niter = initial[3]     # initilazing
Niter = int(Niter)      # float to integer trasformation
xi = (xu + xl)/2
print('\n NEWTON RAPSHON METHOD:\n')    
print('Iter \t\t', 'xi \t\t\t','f(xi) \t\t', 'err(%) \t\t', sep='\t', end = "\n")
for i in range(0,Niter): 
    # copy previous estimate
    xi0 = xi
    # update the estimate 
    xi = xi  - f(xi)/fp(xi) 
    approxE = (abs((xi-xi0)/xi))*100  # Calculate error
    
    if math.isnan(f(xi)):
        print('This function cannot be solved by Newton-Rapshon Method')
        break
    
    print(i,'\t\t', format(xi, '.6e'), format(f(xi), '.6e'), format(approxE, '.6e'),\
          sep='\t', end = "\n")
    """
    Below are the lines for writing output file
    
    """    
    outpoly = (i+1, format(xi, '1.8g'), format(f(xi), '1.8g'), format(approxE, '.2g'))
    for item in outpoly:
        s = str(item)
        file.write(s+ '\t\t')
    file.write('\n')
    
    # Check error and terminate iterations if necessary
    if (approxE < errors or abs(f(xi))< EPS):
      break
  
file.close()

######################              SECANT METHOD
file = open("output_secant.txt", "wt")                  # Output .txt file opened

xi0 = initial[0]        # initilazing
xi1 = initial[1]        # initilazing
errors = initial[2]    # initilazing
Niter = initial[3]     # initilazing
Niter = int(Niter)      # float to integer trasformation
print('\n SECANT METHOD:\n')    
print('Iter \t\t', 'xi \t\t\t','f(xi) \t\t', 'err(%) \t\t', sep='\t', end = "\n")   # Headers

for i in range(0,Niter): 
    # update the estimate 
    xi = xi0 - f(xi0)*(xi1 - xi0)/(f(xi1) - f(xi0))
    # compute error
    approxE = abs((xi-xi0)/xi)*100
    
    if math.isnan(f(xi)):
        print('This function cannot be solved by Newton-Rapshon Method')
        break
    
    """
    Below are the lines for writing output file
    
    """    
    outpoly = (i+1, format(xi, '1.8g'), format(f(xi), '1.8g'), format(approxE, '1.2g'))
    for item in outpoly:
        s = str(item)
        file.write(s+ '\t\t')
    file.write('\n')
    
    # check error and terminate iterations if necessary
    if (approxE < errors):
      break
    # discard oldest data
    xi1  = xi0 
    # update the new estimate
    xi0 = xi
    
    print(i,'\t\t', format(xi, '.6e'), format(f(xi), '.6e'), format(approxE, '.6e'), \
          sep='\t', end = "\n")
        
file.close() 























