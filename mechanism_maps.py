#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:47:04 2020

@author: danielfurman
"""

# Construction of mechanism maps, per Frost and Ashby 1982, Maeno and Ebinuma
# 1982. This script takes a long time to run, over 16 minutes, as the sympy
# solver has to iterate many times. 

# required libraries:
import numpy as np
import matplotlib.pylab as plt
from sympy.solvers import solve
from sympy import Symbol

#set flow law params:
R = 8.314
T = 233
A = 1.48e5*np.exp(-60000/(8.314*T))
n = 3.74
n3 = 1.625
A_gbs = 0.4431*np.exp(-49000/(8.314*T))
pr = .85 #take the mean density for intermediate stage
p = .8966

# set solving conditions
x = Symbol('x')

r = np.arange(1e-6,1e-5,1e-5)
r1 = np.arange(1e-5,1e-4,1e-4)
r2 = np.arange(1e-4,1e-3,1e-3)
r3 = np.arange(1e-3,1e-2,1e-2)
r4 = np.array([1e-2])
r = np.concatenate((r,r1,r2,r3,r4)) #grain sizes 

stress_boundary = np.zeros(len(r)) #initiate stress bounndary


for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(1/(
        2*r[i])**p)) - ((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*x)/n)**n)),x)
    stress_boundary[i] = a[1]
    
fig, ax = plt.subplots()


ax.loglog(stress_boundary, r, label =
          'boundary \n$\.\epsilon$disl.=$\.\epsilon$GBS', linewidth = 5)

# now find rate contours:

r = np.arange(1e-6,1e-5,1e-6)
r1 = np.arange(1e-5,1e-4,1e-5)
r2 = np.arange(1e-4,1e-3,1e-4)
r3 = np.arange(1e-3,1e-2,1e-3)
r4 = np.array([1e-2])
r = np.concatenate((r, r1, r2,r3,r4))
stress41 = np.zeros(len(r))
strain_rate = 1e-6
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(
        1/(2*r[i])**p)-strain_rate),x)
    #print('41',a)
    stress41[i] = a[0]
stress42 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((
        2*x)/n)**n)-strain_rate),x)
    #print('42',a)
    stress42[i] = a[0]

stress31 = np.zeros(len(r))
strain_rate = 1e-8
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(1/(
        2*r[i])**p)-strain_rate),x)
    stress31[i] = a[0]
    #print('31',a)
stress32 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*x)/n)**n)-
               strain_rate),x)
    #print('32',a)
    stress32[i] = a[0]
    
stress21 = np.zeros(len(r))
strain_rate = 1e-10
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(
        1/(2*r[i])**p)-strain_rate),x)
    #print('21',a)
    stress21[i] = a[0]
stress22 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*x)/n)**n)-
               strain_rate),x)
    #print('22',a)
    stress22[i] = a[0]
stress61 = np.zeros(len(r))
strain_rate = 1e-12
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(
        1/(2*r[i])**p)-strain_rate),x)
    #print('61',a)
    stress61[i] = a[0]
stress62 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*x)/n)**n)-
               strain_rate),x)
    #print('62',a)
    stress62[i] = a[0]
    
ax.set_ylabel('Grain radius (m)')
ax.set_xlabel('$log$ $\sigma$ (Mpa)')


ax.set_title('Sintering Mechanism Map: 253 K, .85 pr ', fontweight = 'bold')

ax.set_xlim([1e-2, 10])

ax.set_ylim([1e-6, 1e-2])

ax.loglog(stress42[stress41>stress42],r[stress41>stress42],'--',color='grey',
          label = 'rate contours')
ax.loglog(stress41[stress41<stress42],r[stress41<stress42],'--',color='grey')
ax.loglog(stress32[stress31>stress32],r[stress31>stress32],'--',color='grey')
ax.loglog(stress31[stress31<stress32],r[stress31<stress32],'--',color='grey')
ax.loglog(stress22[stress21>stress22],r[stress21>stress22],'--',color='grey')
ax.loglog(stress21[stress21<stress22],r[stress21<stress22],'--',color='grey')
ax.loglog(stress62[stress61>stress62],r[stress61>stress62],'--',color='grey')
ax.loglog(stress61[stress61<stress62],r[stress61<stress62],'--',color='grey')


# plt.savefig('images/sintering2.png', dpi = 400)


# now repeat for Mars

plt.figure()

T = 165
A = 1.48e5*np.exp(-60000/(8.314*T))
n = 3.74
n3 = 1.625
A_gbs = 0.4431*np.exp(-49000/(8.314*T))
pr = .85
p = .8966
x = Symbol('x')


r = np.arange(1e-6,1e-5,1e-5)
r1 = np.arange(1e-5,1e-4,1e-4)
r2 = np.arange(1e-4,1e-3,1e-3)
r3 = np.arange(1e-3,1e-2,1e-2)
r4 = np.arange(1e-2,1e-1,1e-1)
r = np.concatenate((r,r1,r2,r3,r4))

stress_boundary = np.zeros(len(r))

x = Symbol('x')
for i in range(0,len(r)):

    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(1/(
        2*r[i])**p)) - ((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*x)/n)**n)),x)
    stress_boundary[i] = a[1]
    
fig, ax = plt.subplots()


ax.loglog(stress_boundary, r, label =
          'boundary \n$\.\epsilon$disl.=$\.\epsilon$GBS', linewidth = 5)

r = np.arange(1e-6,1e-5,2e-6)
r1 = np.arange(1e-5,1e-4,2e-5)
r2 = np.arange(1e-4,1e-3,2e-4)
r3 = np.arange(1e-3,1e-2,2e-3)
r4 = np.arange(1e-2,1e-1,2e-2)
r = np.concatenate((r, r1, r2,r3,r4))
stress41 = np.zeros(len(r))
strain_rate = 1e-12
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(
        1/(2*r[i])**p)-strain_rate),x)

    stress41[i] = a[0]
stress42 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((
        2*x)/n)**n)-strain_rate),x)

    stress42[i] = a[0]
ax.loglog(stress42[stress41>stress42],r[stress41>stress42],'--',color='grey',
          label = 'rate contours')
ax.loglog(stress41[stress41<stress42],r[stress41<stress42],'--',color='grey')
 
stress41 = np.zeros(len(r))
strain_rate = 1e-10
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(
        1/(2*r[i])**p)-strain_rate),x)

    stress41[i] = a[0]
stress42 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((
        2*x)/n)**n)-strain_rate),x)

    stress42[i] = a[0]

stress31 = np.zeros(len(r))
strain_rate = 1e-14
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(1/(
        2*r[i])**p)-strain_rate),x)
    stress31[i] = a[0]

stress32 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*x)/n)**n)-
               strain_rate),x)

    stress32[i] = a[0]
    
stress21 = np.zeros(len(r))
strain_rate =  1e-16
for i in range(0,len(r)):
    a = solve(((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((2*x)/n3)**n3)*(
        1/(2*r[i])**p)-strain_rate),x)

    stress21[i] = a[0]
stress22 = np.zeros(len(r))
for i in range(0,len(r)):
    a = solve(((2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*x)/n)**n)-
               strain_rate),x)

    stress22[i] = a[0]

    
ax.set_ylabel('Grain radius (m)')
ax.set_xlabel('$log$ $\sigma$ (Mpa)')


ax.set_title('Sintering Mechanism Map: 165 K, .85 pr ', fontweight = 'bold')

ax.set_xlim([1e-2, 10])

ax.set_ylim([1e-6, 1e-2])

ax.loglog(stress42[stress41>stress42],r[stress41>stress42],'--',color='grey',
          label = 'rate contours')
ax.loglog(stress41[stress41<stress42],r[stress41<stress42],'--',color='grey')
ax.loglog(stress32[stress31>stress32],r[stress31>stress32],'--',color='grey')
ax.loglog(stress31[stress31<stress32],r[stress31<stress32],'--',color='grey')
ax.loglog(stress22[stress21>stress22],r[stress21>stress22],'--',color='grey')
ax.loglog(stress21[stress21<stress22],r[stress21<stress22],'--',color='grey')


# plt.savefig('images/sintering_mars.png', dpi = 400)