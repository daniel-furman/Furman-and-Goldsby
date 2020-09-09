#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues Aug 18 13:27:33 2020
@author: danielfurman
"""
# Sixteen densification rate calculations. The entire creep curve was
# composed of a transient response followed by the steady-state regime,
# with rates calculated by taking time slices during steady-state and
# averaging many thus-approximated rates. Steady-state slices corresponded to
# relatively small changes in density; therefore, the mean relative density
# was considered representative per measurement, and the densification can be 
# taken as density invariant, albeit locally. See one example in the 
# script "calc_dens_rate_example.py"

# Required Libraries:

import pandas as pd
import numpy as np
import glob
import matplotlib.pylab as plt
import warnings
warnings.filterwarnings("ignore")

# Load all experimental data

filenames = sorted(glob.glob('data/compaction*.csv')) #grab filepath names
print('\nThe compaction creep test files are:\n\n',filenames) # print names
data_list1 = [] #intialize empty numpy stack
for f in filenames: #f is index with string filenames
    data_list1.append(np.loadtxt(fname=f, delimiter=',')) #stack arrays
print('\nThere are', len(data_list1), 'total experimental files.')  

num_experiments = len(data_list1) #variable for number of files

# Also load experimental table 

paper_table = pd.read_csv('data/paper_data.csv', delimiter=',', header = 'infer') 
applied_pressure_raw = np.array([0.627, 0.753, 0.878,0.973,1.16,1.16,
                                 0.47,0.59,0.72,1.16,0.251,0.377,
                                 0.44, 0.5967,1.16,1.16]) #In MPa

fig, axes = plt.subplots(1, 3, figsize=(20,4.5)) #inialize matrix of plots
steadystate_slice = data_list1[0][(data_list1[0][:,1]/(60*60)>=10)&
                                  (data_list1[0][:,1]/(60*60)<=115)]
axes[0].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes[0].set_ylim([.74,.744])
axes[0].set_title('Compaction Id 1, First Step')

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[0,'Densification rate'] = dens_rate
paper_table.loc[0, 'Mean dens'] = mean_dens
paper_table.loc[0, 'applied stress'] = applied_pressure_raw[0]/mean_dens

axes[0].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[0].legend(loc = 'lower right', shadow = True)
axes[0].set_ylabel('Density (g/cm^3)')
axes[0].set_xlabel('Time (hours)')

steadystate_slice = data_list1[1][(data_list1[1][:,1]/(60*60)>=0)
                                  &(data_list1[1][:,1]/(60*60)<=33.9)]
axes[1].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes[1].set_ylim([.739,.743])
axes[1].set_title('Compaction Id 2, First Step')

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[3,'Densification rate'] = dens_rate
paper_table.loc[3, 'Mean dens'] = mean_dens
paper_table.loc[3, 'applied stress'] = applied_pressure_raw[3]/mean_dens
 
axes[1].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[1].legend(loc = 'lower right', shadow = True)
axes[1].set_ylabel('Density (g/cm^3)')
axes[1].set_xlabel('Time (hours)')

steadystate_slice = data_list1[2][(data_list1[2][:,1]/(60*60)>=5)
                                  &(data_list1[2][:,1]/(60*60)<=60)]
axes[2].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes[2].set_title('Compaction Id 3, First Step')
x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[11,'Densification rate'] = dens_rate
paper_table.loc[11, 'Mean dens'] = mean_dens
paper_table.loc[11, 'applied stress'] = applied_pressure_raw[11]/mean_dens
axes[2].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[2].legend(loc = 'lower right', shadow = True)
axes[2].set_ylabel('Density (g/cm^3)')
axes[2].set_xlabel('Time (hours)')

fig, axes = plt.subplots(1, 3, figsize=(20,4.5)) #inialize matrix of plots

steadystate_slice = data_list1[3][(data_list1[3][:,1]/(60*60)<=38)
                                  &(data_list1[3][:,1]/(60*60)>=23)]

axes[0].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes[0].set_title('Compaction Id 4, Single step')

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[13,'Densification rate'] = dens_rate
paper_table.loc[13, 'Mean dens'] = mean_dens
paper_table.loc[13, 'applied stress'] = applied_pressure_raw[13]/mean_dens

axes[0].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[0].legend(loc = 'lower right', shadow = True)
axes[0].set_ylabel('Density (g/cm^3)')
axes[0].set_xlabel('Time (hours)')
        
steadystate_slice = data_list1[2][(data_list1[2][:,1]/(60*60)>=140)]

axes[1].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes[1].set_title('Compaction Id 3, Second Step')
x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[10,'Densification rate'] = dens_rate
paper_table.loc[10, 'Mean dens'] = mean_dens
paper_table.loc[10, 'applied stress'] = applied_pressure_raw[10]/mean_dens
 
axes[1].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[1].legend(loc = 'lower right', shadow = True)
axes[1].set_ylabel('Density (g/cm^3)')
axes[1].set_xlabel('Time (hours)')

steadystate_slice = data_list1[4][(data_list1[4][:,1]/(60*60)>=82)
                                  &(data_list1[4][:,1]/(60*60)<=97)]
axes[2].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes[2].set_title('Compaction Id 5, First Step')

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[14,'Densification rate'] = dens_rate
paper_table.loc[14, 'Mean dens'] = mean_dens
paper_table.loc[14, 'applied stress'] = applied_pressure_raw[14]/mean_dens

axes[2].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[2].legend(loc = 'lower right', shadow = True)
axes[2].set_ylabel('Density (g/cm^3)')
axes[2].set_xlabel('Time (hours)')

fig, axes = plt.subplots(1, 3, figsize=(20,4.5)) #inialize matrix of plots

steadystate_slice = data_list1[4][(data_list1[4][:,1]/(60*60)>=128)]
axes[0].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
axes[0].set_title('Compaction Id 5, Second Step ')
x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[12,'Densification rate'] = dens_rate
paper_table.loc[12, 'Mean dens'] = mean_dens
paper_table.loc[12, 'applied stress'] = applied_pressure_raw[12]/mean_dens

axes[0].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[0].legend(loc = 'lower right', shadow = True)
axes[0].set_ylabel('Density (g/cm^3)')
axes[0].set_xlabel('Time (hours)')

axes[1].set_title('Compaction Id 6, First Step')

steadystate_slice = data_list1[5][(data_list1[5][:,1]/(60*60)>=60)
                                  &(data_list1[5][:,1]/(60*60)<=90)]
axes[1].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[9,'Densification rate'] = dens_rate
paper_table.loc[9, 'Mean dens'] = mean_dens
paper_table.loc[9, 'applied stress'] = applied_pressure_raw[9]/mean_dens

axes[1].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[1].legend(loc = 'lower right', shadow = True)
axes[1].set_ylabel('Density (g/cm^3)')
axes[1].set_xlabel('Time (hours)')

axes[2].set_title('Compaction Id 6, Second Step')
steadystate_slice = data_list1[5][(data_list1[5][:,1]/(60*60)>=91)
                                  &(data_list1[5][:,1]/(60*60)<=113)]
axes[2].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[6,'Densification rate'] = dens_rate
paper_table.loc[6, 'Mean dens'] = mean_dens
paper_table.loc[6, 'applied stress'] = applied_pressure_raw[6]/mean_dens

axes[2].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[2].legend(loc = 'lower right', shadow = True)
axes[2].set_ylabel('Density (g/cm^3)')
axes[2].set_xlabel('Time (hours)')

fig, axes = plt.subplots(1, 3, figsize=(20,4.5)) #inialize matrix of plots

steadystate_slice = data_list1[5][(data_list1[5][:,1]/(60*60)>=115)
                                  &(data_list1[5][:,1]/(60*60)<=136)]
axes[0].set_title('Compaction Id 6, Third Step')
axes[0].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[8,'Densification rate'] = dens_rate
paper_table.loc[8, 'Mean dens'] = mean_dens
paper_table.loc[8, 'applied stress'] = applied_pressure_raw[8]/mean_dens

axes[0].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))

axes[0].legend(loc = 'lower right', shadow = True)
axes[0].set_ylabel('Density (g/cm^3)')
axes[0].set_xlabel('Time (hours)')

steadystate_slice = data_list1[5][(data_list1[5][:,1]/(60*60)>=140)]

axes[1].set_title('Compaction Id 6, Fourth Step')

axes[1].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[7,'Densification rate'] = dens_rate
paper_table.loc[7, 'Mean dens'] = mean_dens
paper_table.loc[7, 'applied stress'] = applied_pressure_raw[7]/mean_dens

axes[1].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[1].legend(loc = 'lower right', shadow = True)
axes[1].set_ylabel('Density (g/cm^3)')
axes[1].set_xlabel('Time (hours)')
        
steadystate_slice = data_list1[0][(data_list1[0][:,1]/(60*60)>=140)]

axes[2].set_title('Compaction Id 1, Second Step')

axes[2].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[5,'Densification rate'] = dens_rate
paper_table.loc[5, 'Mean dens'] = mean_dens
paper_table.loc[5, 'applied stress'] = applied_pressure_raw[5]/mean_dens

axes[2].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[2].legend(loc = 'lower right', shadow = True)
fig, axes = plt.subplots(1, 3, figsize=(20,4.5)) #inialize matrix of plots
axes[2].set_ylabel('Density (g/cm^3)')
axes[2].set_xlabel('Time (hours)')

axes[0].set_title('Compaction Id 2, Second Step')

steadystate_slice = data_list1[1][(data_list1[1][:,1]/(60*60)>=60)
                                  &(data_list1[1][:,1]/(60*60)<=79)]
axes[0].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])
x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[4,'Densification rate'] = dens_rate
paper_table.loc[4, 'Mean dens'] = mean_dens
paper_table.loc[4, 'applied stress'] = applied_pressure_raw[4]/mean_dens

axes[0].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[0].legend(loc = 'lower right', shadow = True)
axes[0].set_ylabel('Density (g/cm^3)')
axes[0].set_xlabel('Time (hours)')

axes[1].set_title('Compaction Id 2, Third Step')

steadystate_slice = data_list1[1][(data_list1[1][:,1]/(60*60)>=80)
                                  &(data_list1[1][:,1]/(60*60)<=100)]
axes[1].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[1,'Densification rate'] = dens_rate
paper_table.loc[1, 'Mean dens'] = mean_dens
paper_table.loc[1, 'applied stress'] = applied_pressure_raw[1]/mean_dens
axes[1].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[1].legend(loc = 'lower right', shadow = True)
axes[1].set_ylabel('Density (g/cm^3)')
axes[1].set_xlabel('Time (hours)')

axes[2].set_title('Compaction Id 2, Fourth Step')

steadystate_slice = data_list1[1][(data_list1[1][:,1]/(60*60)>=125)]
axes[2].plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[2,'Densification rate'] = dens_rate
paper_table.loc[2, 'Mean dens'] = mean_dens
paper_table.loc[2, 'applied stress'] = applied_pressure_raw[2]/mean_dens
axes[2].plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
             np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes[2].legend(loc = 'lower right', shadow = True)
axes[2].set_ylabel('Density (g/cm^3)')
axes[2].set_xlabel('Time (hours)')

fig, axes = plt.subplots(1, 1, figsize=(4.8,4)) #inialize matrix of plots

axes.set_title('Compaction Id 7, Single Step')
steadystate_slice = data_list1[6][(data_list1[6][:,1]/(60*60)>=100)
                                  &(data_list1[6][:,1]/(60*60)<=170)]
axes.plot(steadystate_slice [:,1]/(60*60), steadystate_slice [:,7])

x = int(len(steadystate_slice[:,1])/10)
densrates = np.zeros(x)
strainrates = np.zeros(x)
time1 = np.zeros(x)
dense1 = np.zeros(x)
time2 = np.zeros(x)
dense2 = np.zeros(x)

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
mean_dens = np.mean(np.array([np.mean(dense1),np.mean(dense2)]))/.917
paper_table.loc[15,'Densification rate'] = dens_rate
paper_table.loc[15, 'Mean dens'] = mean_dens
paper_table.loc[15, 'applied stress'] = applied_pressure_raw[15]/mean_dens
axes.plot(np.array([np.mean(time1)/(60*60),np.mean(time2)/(60*60)]),
          np.array([np.mean(dense1),np.mean(dense2)]),
             label = 'Steady-state rate = ' + "{:.2e}".format(dens_rate))
axes.legend(loc = 'lower right', shadow = True)
axes.set_ylabel('Density (g/cm^3)')
axes.set_xlabel('Time (hours)')

paper_table.to_csv('data/paper_table_full.csv', index = None, header=True)