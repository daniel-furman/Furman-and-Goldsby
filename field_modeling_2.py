#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:54:27 2020

@author: danielfurman
"""

# In the second part of "field_modeling" we contrast the natural rates of
# densification with our flow law model predictions. We consider the two
# power law mechanisms resolved from out testing, using the temperature,
# density, and stress conditions from the field profiles. 

# required libraries:
import matplotlib.pylab as plt
from sympy import Symbol
import numpy as np

exec(open('field_modeling.py').read())

print('Firn rates across intermediate densificaiton derived from'+
      'density-pressure profiles:')
print('the mean  rate  is:', np.max(strain_rates['mean']))
print('the min rate  is:', np.min(strain_rates['mean']))
print('the max rate is:', np.mean(strain_rates['mean']))

data_nature[2] #mizuho
R = 8.314 #gas constant
x = Symbol('x')
T = (240) #temp in kelvin
r = 1e-4 #radius in meters
p = .8966
A = 1.48e5*np.exp(-60000/(8.314*T))
A_gbs = 0.443*np.exp(-49000/(8.314*T))
n3 = 1.626
n = 3.74

rate_dl = np.zeros(len(data_nature[2][:,0]))
rate_gbs = np.zeros(len(data_nature[2][:,0]))
rate_gbs1 = np.zeros(len(data_nature[2][:,0]))

for i in range(0,len(data_nature[2][:,0])):
    rate_gbs[i] = ((2*A_gbs*(1-data_nature[2][i,2])/((1-(
        1-data_nature[2][i,2])**(1/n3))**n3))*(((
            2*data_nature[2][i,0])/n3)**n3)*(1/(2*r)**p))
    rate_dl[i] = (2*A*(1-data_nature[2][i,2])/((1-(1-data_nature[2][i,2])**(
        1/n))**n))*(((2*data_nature[2][i,0])/n)**n)
r = 1e-3
for i in range(0,len(data_nature[2][:,0])):
    rate_gbs1[i] = ((2*A_gbs*(1-data_nature[2][i,2])/((1-(1-
        data_nature[2][i,2])**(1/n3))**n3))*(((
            2*data_nature[2][i,0])/n3)**n3)*(1/(2*r)**p))
    
    
plotter = np.zeros([len(data_nature[2][:,2]),9])

plotter[:,0] = data_nature[2][:,2]
plotter[:,1] = rate_gbs
plotter[:,2] = rate_dl
plotter[:,6] = rate_gbs1

plotter = np.sort(plotter, axis=0)
plt.semilogy(plotter[:,0],plotter[:,1], '--',color = 'tab:orange',
             label = 'GSS creep')
plt.semilogy(plotter[:,0],plotter[:,2], '--', color = 'tab:blue',
             label = 'Dislocation creep')
plt.semilogy(plotter[:,0],plotter[:,6], '--', color = 'tab:orange',
             label = 'GSS creep')
plt.fill_between(plotter[:,0], plotter[:,6], y2 = plotter[:,1],
                 alpha = 0.2,color = 'tab:orange')


plt.semilogy([(.833+.8)/2,.85,(.866+.9)/2],[1.275e-11,2.343e-11,1.259e-11],
             'k^', markersize = '9',
             label = 'Natural ice sheet rates')
plt.title('Mizuho', fontweight = 'bold')
plt.ylabel('Log densification rate')
plt.xlabel('Relative Density')

plt.ylim([1e-14,1e-8])

plt.grid(axis = 'x')
plt.xlim([.8,.9])
plt.savefig('images/Mizuho.png', dpi = 400)

plt.figure()
data_nature[0] # vostok


stress = np.arange(.1,.7,.01)
pr = np.zeros(len(stress))
x = Symbol('x')

T = (216) #temp in kelvin
r = 1e-4 #radius in meters



A = 1.48e5*np.exp(-60000/(8.314*T))
A_gbs = 0.443*np.exp(-49000/(8.314*T))


rate_dl = np.zeros(len(data_nature[0][:,0]))
rate_gbs = np.zeros(len(data_nature[0][:,0]))

rate_gbs1 = np.zeros(len(data_nature[0][:,0]))


for i in range(0,len(data_nature[0][:,0])):
    
    rate_gbs[i] = ((2*A_gbs*(1-data_nature[0][i,2])/((1-(1-data_nature[0]
        [i,2])**(1/n3))**n3))*(((2*data_nature[0][i,0])/n3)**n3)*(1/(2*r)**p))
    rate_dl[i] = (2*A*(1-data_nature[0][i,2])/((1-(1-data_nature[0]
        [i,2])**(1/n))**n))*(((2*data_nature[0][i,0])/n)**n)

r = 1e-3
for i in range(0,len(data_nature[0][:,0])):
    rate_gbs1[i] = ((2*A_gbs*(1-data_nature[0][i,2])/((1-(1-data_nature[0]
        [i,2])**(1/n3))**n3))*(((2*data_nature[0][i,0])/n3)**n3)*(1/(2*r)**p))
    
plotter = np.zeros([len(data_nature[0][:,2]),9])

plotter[:,0] = data_nature[0][:,2]
plotter[:,1] = rate_gbs
plotter[:,2] = rate_dl
plotter[:,6] = rate_gbs1

plotter = np.sort(plotter, axis=0)
plt.semilogy(plotter[:,0],plotter[:,1], '--',color = 'tab:orange', 
             label = 'GSS creep')
plt.semilogy(plotter[:,0],plotter[:,2], '--', color = 'tab:blue',
             label = 'Dislocation creep')
plt.semilogy(plotter[:,0],plotter[:,6], '--', color = 'tab:orange',label = '')
plt.fill_between(plotter[:,0], plotter[:,6], y2 = plotter[:,1],  alpha = 0.2,
                 color = 'tab:orange')


plt.semilogy([(.833+.8)/2,.85,(.866+.9)/2],[2.05e-12,1.31e-12,9.38e-13], 'k^',
             markersize = '9',
             label = 'Vostok field data')
plt.title('Vostok', fontweight = 'bold')
plt.ylabel('Log densification rate')
plt.xlabel('Relative Density')


plt.ylim([1e-14,1e-8])
plt.grid(axis = 'x')
plt.xlim([.8,.9])
plt.savefig('images/Vostok.png', dpi = 400)


plt.figure()
data_nature[4] # gisp


stress = np.arange(.1,.7,.01)
pr = np.zeros(len(stress))
x = Symbol('x')

T = (244) #temp in kelvin
r = 1e-4 #radius in meters




A = 1.48e5*np.exp(-60000/(8.314*T))
A_gbs = 0.443*np.exp(-49000/(8.314*T))

rate_dl = np.zeros(len(data_nature[4][:,0]))
rate_gbs = np.zeros(len(data_nature[4][:,0]))

rate_gbs1 = np.zeros(len(data_nature[4][:,0]))



for i in range(0,len(data_nature[4][:,0])):
    rate_gbs[i] = ((2*A_gbs*(1-data_nature[4][i,2])/((1-(1-data_nature[4]
        [i,2])**(1/n3))**n3))*(((2*data_nature[4][i,0])/n3)**n3)*(1/(2*r)**p))
    rate_dl[i] = (2*A*(1-data_nature[4][i,2])/((1-(1-data_nature[4]
        [i,2])**(1/n))**n))*(((2*data_nature[4][i,0])/n)**n)

r = 1e-3
for i in range(0,len(data_nature[4][:,0])):
    rate_gbs1[i] = ((2*A_gbs*(1-data_nature[4][i,2])/((1-(1-data_nature[4]
        [i,2])**(1/n3))**n3))*(((2*data_nature[4][i,0])/n3)**n3)*(1/(2*r)**p))

plotter = np.zeros([len(data_nature[4][:,2]),9])

plotter[:,0] = data_nature[4][:,2]
plotter[:,1] = rate_gbs
plotter[:,2] = rate_dl
plotter[:,6] = rate_gbs1

plotter = np.sort(plotter, axis=0)
plt.semilogy(plotter[:,0],plotter[:,1], '--',color = 'tab:orange',
             label = 'GSS creep')
plt.semilogy(plotter[:,0],plotter[:,2], '--', color = 'tab:blue',
             label = 'Dislocation creep')


plt.semilogy(plotter[:,0],plotter[:,6], '--', color = 'tab:orange',
             label = 'GSS creep')
plt.fill_between(plotter[:,0], plotter[:,6], y2 = plotter[:,1],  alpha = 0.2,
                 color = 'tab:orange')

plt.semilogy([(.833+.8)/2,.85,(.866+.9)/2],[2.0e-11,1.61e-11,1.41e-11], 'k^',
             markersize = '9',
             label = 'GISP 2 field data')
plt.title('GISP 2', fontweight = 'bold')
plt.ylabel('Log densification rate')
plt.xlabel('Relative Density')

plt.ylim([1e-14,1e-8])
plt.grid(axis = 'x')
plt.xlim([.8,.9])
plt.savefig('images/GISP2.png', dpi = 400)

plt.figure()




stress = np.arange(.1,.7,.01)
pr = np.zeros(len(stress))
x = Symbol('x')

T = (245) #temp in kelvin
r = 1e-4 #radius in meters


A = 1.48e5*np.exp(-60000/(8.314*T))
A_gbs = 0.443*np.exp(-49000/(8.314*T))

rate_dl = np.zeros(len(data_nature[1][:,0]))
rate_gbs = np.zeros(len(data_nature[1][:,0]))
rate_gbs1 = np.zeros(len(data_nature[1][:,0]))


for i in range(0,len(data_nature[1][:,0])):
    rate_gbs[i] = ((2*A_gbs*(1-data_nature[1][i,2])/((1-(1-data_nature[1]
        [i,2])**(1/n3))**n3))*(((2*data_nature[1][i,0])/n3)**n3)*(1/(2*r)**p))
    rate_dl[i] = (2*A*(1-data_nature[1][i,2])/((1-(1-data_nature[1][i,2])**(
        1/n))**n))*(((2*data_nature[1][i,0])/n)**n)
r = 1e-3
for i in range(0,len(data_nature[1][:,0])):
    rate_gbs1[i] = ((2*A_gbs*(1-data_nature[1][i,2])/((1-(1-data_nature[1]
        [i,2])**(1/n3))**n3))*(((2*data_nature[1][i,0])/n3)**n3)*(1/(2*r)**p))

    
plotter = np.zeros([len(data_nature[1][:,2]),9])

plotter[:,0] = data_nature[1][:,2]
plotter[:,1] = rate_gbs
plotter[:,2] = rate_dl
plotter[:,6] = rate_gbs1

plotter = np.sort(plotter, axis=0)
plt.semilogy(plotter[:,0],plotter[:,1], '--',color = 'tab:orange', 
             label = 'GSS creep')
plt.semilogy(plotter[:,0],plotter[:,2], '--', color = 'tab:blue',
             label = 'Dislocation creep')


plt.semilogy(plotter[:,0],plotter[:,6], '--', color = 'tab:orange',
             label = 'GSS creep')
plt.fill_between(plotter[:,0], plotter[:,6], y2 = plotter[:,1],  alpha = 0.2,
                 color = 'tab:orange')


plt.semilogy([(.833+.8)/2,.85,(.866+.9)/2],[3.72e-12,3.48e-11,2.57e-12], 'k^',
             markersize = '9', 
             label = 'Byrd field data')
plt.title('Byrd', fontweight = 'bold')
plt.ylabel('Log densification rate')
plt.xlabel('Relative Density')
plt.grid(axis = 'x')
plt.ylim([1e-14,1e-8])
plt.xlim([.8,.9])
plt.savefig('images/Byrd.png', dpi = 400)

plt.figure()
print()





stress = np.arange(.1,.7,.01)
pr = np.zeros(len(stress))
x = Symbol('x')

T = (219) #temp in kelvin
r = 1e-4 #radius in meters


A = 1.48e5*np.exp(-60000/(8.314*T))
A_gbs = 0.443*np.exp(-49000/(8.314*T))
rate_dl = np.zeros(len(data_nature[3][:,0]))
rate_gbs = np.zeros(len(data_nature[3][:,0]))
rate_gbs1 = np.zeros(len(data_nature[3][:,0]))


for i in range(0,len(data_nature[3][:,0])):
    rate_gbs[i] = ((2*A_gbs*(1-data_nature[3][i,2])/((1-(1-data_nature[3]
        [i,2])**(1/n3))**n3))*(((2*data_nature[3][i,0])/n3)**n3)*(1/(2*r)**p))
    rate_dl[i] = (2*A*(1-data_nature[3][i,2])/((1-(1-data_nature[3][i,2])**(
        1/n))**n))*(((2*data_nature[3][i,0])/n)**n)

r = 1e-3
for i in range(0,len(data_nature[3][:,0])):
    rate_gbs1[i] = ((2*A_gbs*(1-data_nature[3][i,2])/((1-(1-data_nature[3]
       [i,2])**(1/n3))**n3))*(((2*data_nature[3][i,0])/n3)**n3)*(1/(2*r)**p))

plotter = np.zeros([len(data_nature[3][:,2]),9])

plotter[:,0] = data_nature[3][:,2]
plotter[:,1] = rate_gbs
plotter[:,2] = rate_dl
plotter[:,6] = rate_gbs1

plotter = np.sort(plotter, axis=0)
plt.semilogy(plotter[:,0],plotter[:,1], '--',color = 'tab:orange', label = '')
plt.semilogy(plotter[:,0],plotter[:,2], '--', color = 'tab:blue',
             label = 'Dislocation creep')

plt.semilogy(plotter[:,0],plotter[:,6], '--', color = 'tab:orange',
             label = 'GSS creep')
plt.fill_between(plotter[:,0], plotter[:,6], y2 = plotter[:,1],  alpha = 0.2,
                 color = 'tab:orange')


plt.semilogy([(.833+.8)/2,.85,(.866+.9)/2],[5.3e-12,1.31e-12,6.46e-12], 'k^',
             markersize = '9',
             label = 'Natural densification rate')
plt.title('Dome C', fontweight = 'bold')
plt.ylabel('Log densification rate')
plt.xlabel('Relative Density')
plt.grid(axis = 'x')
plt.xlim([.8,.9])
plt.ylim([1e-14,1e-8])

plt.savefig('images/DomeC.png', dpi = 400)

plt.figure()
print()