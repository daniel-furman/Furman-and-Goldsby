#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 11:20:46 2020

@author: danielfurman
"""

# An example (out of sixteen) of a densification rate calculation. Outputs
# were composed of a transient response followed by the steady-state regime,
# with rates calculated by taking time slices during steady-state and
# averaging many thus-approximated rates. Steady-state slices corresponded to
# relatively small changes in density; therefore, the mean relative density
# was considered representative per measurement, and the densification can be 
# taken as density invariant, albeit locally.

# See Firn_notebook.ipynb for all sixteen rate calculations

# Required Libraries:

import numpy as np
import glob
import matplotlib.pylab as plt
import warnings
warnings.filterwarnings("ignore")

# Load experimental data
filenames = sorted(glob.glob('data/compaction*.csv')) #grab filepath names
print('\nThe compaction test example is:\n', filenames[0]) # print names
data_list1 = [] #intialize empty numpy stack
for f in filenames: #f is index with string filenames
    data_list1.append(np.loadtxt(fname=f, delimiter=',')) #stack arrays
print('\nThere are', len(data_list1), 'total experimental files\n'+
      ' (see Firn_notebook.ipynb)') 

fig, axes = plt.subplots(1, 1, figsize=(4.5,3.5)) #inialize matrix of plots
#slice data to "steady-state" section, ie. density invariant
steadystate_slice = data_list1[0][(data_list1[0][:,1]/(60*60)>=10)
                                  &(data_list1[0][:,1]/(60*60)<=115)]
axes.plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes.set_ylim([.74,.744])
axes.set_title('Compaction Id 1, First Step', fontweight = 'bold')
axes.set_ylabel('Density (g/cm^3)')
axes.set_xlabel('Time (hours)')

x = int(len(steadystate_slice[:,1])/10) 

# initiate variables for loop
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

# calculate the averaged densificatio rate, strain rate, and avg dens
for i in range(0,x):
    dtime = steadystate_slice[:,1][i] - steadystate_slice[:,1][
        (len(steadystate_slice)-(i+1))] 
    ddense = steadystate_slice[:,7][i] - steadystate_slice[:,7][
        (len(steadystate_slice)-(i+1))]
    dstrain = steadystate_slice[:,5][i] - steadystate_slice[:,5][
        (len(steadystate_slice)-(i+1))]
    densrates[i] = (ddense/dtime)/.917
    strainrates[i] = dstrain/dtime
    dense1[i] = steadystate_slice[:,7][i]
    time1[i] = steadystate_slice[:,1][i]
    dense2[i] = steadystate_slice[:,7][(len(steadystate_slice)-(i+1))]
    time2[i] = steadystate_slice[:,1][(len(steadystate_slice)-(i+1))]
    dens_rate = np.mean(densrates)  
avg_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917

print('\nThe average relative density (p/p-ice) is:\n ',
      "{:.3}".format(avg_dens))

axes.plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes.legend(loc = 'lower right', shadow = True)