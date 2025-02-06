# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:51:13 2023

@author: Murat Berk
"""
import numpy as np
import matplotlib.pyplot as plt

g_0 = 200
k = 300
T_0 = 60
R_1 = 20
step = 30
r = np.arange(0, R_1,R_1/step)
T = g_0/4/k*(R_1**2-r**2) + T_0


plt.xticks(np.arange(0, R_1,R_1/step))
plt.plot(r, T, '-o', color='r', label='FEM')
plt.xlabel('r')
plt.ylabel('T(r)')
plt.title('Finite Element Solution')
plt.grid(True)
plt.legend()
fig = plt.gcf()
fig.set_size_inches(8.5, 6.5)
plt.show()