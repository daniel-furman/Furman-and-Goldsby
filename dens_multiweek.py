#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:14:26 2020

@author: danielfurman
"""

# In this script we take several steady-state rate measurements from a 
# compaction test that took place over several weeks. These rates vary 
# from 1.05e-8 to 2.81e-8, revealing the density dependence during firn creep.

# required libraries:

import matplotlib.pylab as plt
import numpy as np
import glob

filenames = sorted(glob.glob('data/compaction*.csv'))
data_list = []
for f in filenames:
    data_list.append(np.loadtxt(fname=f, delimiter=','))

fig, axes = plt.subplots(1, 1, figsize=(7,4.5)) 
steadystate_slicee = data_list[6][(data_list[6][:,1]/(60*60)>=40)&(
    data_list[6][:,1]/(60*60)<=420)]
axes.plot(steadystate_slicee[:,1]/(60*60),
          steadystate_slicee[:,7], label = 'Densification Curve')

results = np.zeros([4,5]) #where we will store rates and densities per slice

# plot many different rates:

steadystate_slice = data_list[6][(data_list[6][:,1]/(60*60)>=90)&(
    data_list[6][:,1]/(60*60)<=140)]
axes.plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

for i in range(0,x):
    dtime = steadystate_slice[:,1][i] - steadystate_slice[:,1][(
        len(steadystate_slice)-(i+1))]
    ddense = steadystate_slice[:,7][i] - steadystate_slice[:,7][(
        len(steadystate_slice)-(i+1))]
    dstrain = steadystate_slice[:,5][i] - steadystate_slice[:,5][(
        len(steadystate_slice)-(i+1))]

    densrates[i] = (ddense/dtime)/.917
    strainrates[i] = dstrain/dtime
    dense1[i] = steadystate_slice[:,7][i]
    time1[i] = steadystate_slice[:,1][i]
    dense2[i] = steadystate_slice[:,7][(len(steadystate_slice)-(i+1))]
    time2[i] = steadystate_slice[:,1][(len(steadystate_slice)-(i+1))]

results[0,1] = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
results[0,0] = np.mean(densrates)
axes.plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),np.array(
    [np.mean(dense1),np.mean(dense2)]),'k', label = 'Steady-state slice')


steadystate_slice = data_list[6][(data_list[6][:,1]/(60*60)>=190)&(
    data_list[6][:,1]/(60*60)<=230)]
axes.plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

for i in range(0,x):
    dtime = steadystate_slice[:,1][i] - steadystate_slice[:,1][(
        len(steadystate_slice)-(i+1))]
    ddense = steadystate_slice[:,7][i] - steadystate_slice[:,7][(
        len(steadystate_slice)-(i+1))]
    dstrain = steadystate_slice[:,5][i] - steadystate_slice[:,5][(
        len(steadystate_slice)-(i+1))]

    densrates[i] = (ddense/dtime)/.917
    strainrates[i] = dstrain/dtime
    dense1[i] = steadystate_slice[:,7][i]
    time1[i] = steadystate_slice[:,1][i]
    dense2[i] = steadystate_slice[:,7][(len(steadystate_slice)-(i+1))]
    time2[i] = steadystate_slice[:,1][(len(steadystate_slice)-(i+1))]


results[1,1] = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
results[1,0] = np.mean(densrates)
axes.plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),np.array(
    [np.mean(dense1),np.mean(dense2)]),'k')

steadystate_slice = data_list[6][(data_list[6][:,1]/(60*60)<=320)&(
    data_list[6][:,1]/(60*60)>=270)]
axes.plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

for i in range(0,x):
    dtime = steadystate_slice[:,1][i] - steadystate_slice[:,1][(len(
        steadystate_slice)-(i+1))]
    ddense = steadystate_slice[:,7][i] - steadystate_slice[:,7][(len(
        steadystate_slice)-(i+1))]
    dstrain = steadystate_slice[:,5][i] - steadystate_slice[:,5][(len(
        steadystate_slice)-(i+1))]

    densrates[i] = (ddense/dtime)/.917
    strainrates[i] = dstrain/dtime
    dense1[i] = steadystate_slice[:,7][i]
    time1[i] = steadystate_slice[:,1][i]
    dense2[i] = steadystate_slice[:,7][(len(steadystate_slice)-(i+1))]
    time2[i] = steadystate_slice[:,1][(len(steadystate_slice)-(i+1))]


results[2,1] = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
results[2,0] = np.mean(densrates)
axes.plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
          np.array([np.mean(dense1),np.mean(dense2)]),'k')



steadystate_slice = data_list[6][(data_list[6][:,1]/(60*60)<=420)&(
    data_list[6][:,1]/(60*60)>=370)]
    
axes.plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

for i in range(0,x):
    dtime = steadystate_slice[:,1][i] - steadystate_slice[:,1][(len(
        steadystate_slice)-(i+1))]
    ddense = steadystate_slice[:,7][i] - steadystate_slice[:,7][(len(
        steadystate_slice)-(i+1))]
    dstrain = steadystate_slice[:,5][i] - steadystate_slice[:,5][(len(
        steadystate_slice)-(i+1))]

    densrates[i] = (ddense/dtime)/.917
    strainrates[i] = dstrain/dtime
    dense1[i] = steadystate_slice[:,7][i]
    time1[i] = steadystate_slice[:,1][i]
    dense2[i] = steadystate_slice[:,7][(len(steadystate_slice)-(i+1))]
    time2[i] = steadystate_slice[:,1][(len(steadystate_slice)-(i+1))]


results[3,1] = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
results[3,0] = np.mean(densrates)
axes.plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),np.array(
    [np.mean(dense1),np.mean(dense2)]),'k')

# set plotting params:

plt.ylabel('Density (g/cm^3)')
plt.xlabel('Hours')
plt.title('Multi-Week Compaction Test', fontweight = 'bold')
plt.grid(axis = 'y')
plt.savefig('images/multidens.png', dpi = 400)

print('The largest measured rate:', "{:.3e}".format(np.max(results[:,0])))
print('The smallest measured rate:', "{:.3e}".format(np.min(results[:,0])))

#calculate flow law predictions:
results[:,2] = 1.16/results[:,1]

T = 233
A = 1.48e5*np.exp(-60000/(8.314*T))
n = 3.74
n3 = 1.625
A_gbs = 0.4431*np.exp(-49000/(8.314*T))
pr = results[:,1]
p = .8966
r = 5.5e-4

#()
for i in range(0,4):
    results[i,3] = (2*A*(1-pr[i])/((1-(1-pr[i])**(1/n))**n))*(((
        2*results[i,2])/n)**n)
    results[i,4] = (2*A_gbs*(1-pr[i])/((1-(1-pr[i])**(1/n3))**n3))*(((
        2*results[i,2])/n3)**n3)*(1/(2*r)**p)
    
print('\nThe largest flow law disl. creep rate:', 
      "{:.3e}".format(np.max(results[:,3])))
print('The smallest flow law disl. creep  rate:',
      "{:.3e}".format(np.min(results[:,3])))
print('The largest flow law disGBS rate:', 
      "{:.3e}".format(np.max(results[:,4])))
print('The smallest flow law disGS  rate:', 
      "{:.3e}".format(np.min(results[:,4])))







