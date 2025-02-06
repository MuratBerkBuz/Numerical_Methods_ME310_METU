import numpy as np
import matplotlib.pyplot as plt

# Define parameters
r_i = 0 # inner radius of wire (m)
r_o = 0.02 # outer radius of wire (m)
T_i = 100 # temperature at inner radius (C)
T_o = 25 # temperature at outer radius (C)
Q = 1000 # heat generation rate in inner core (W/m^3)
k = 50 # thermal conductivity of wire (W/m.K)
epsilon = 1e-10 # small number to avoid division by zero

# Define radial distance array
r = np.linspace(r_i, r_o, 100)

# Calculate temperature at each radial distance
T = T_i + Q/(4*np.pi*k)*((r**2)/3 - r_i**2) # temperature in inner core
T[r>=0.01] = T_i + Q/(4*np.pi*k)*((r_i**2)/3 - r[r>=0.01]**2) # temperature in outer core

# Interpolate temperature at r=0.01
T_interp = np.interp(0.01, r, T)

# Replace temperature value at r=0.01 with the interpolated value
T[np.abs(r-0.01) < epsilon] = T_interp

# Plot temperature versus radial distance
plt.plot(r, T)
plt.xlabel('Radial distance (m)')
plt.ylabel('Temperature (C)')
plt.show()
