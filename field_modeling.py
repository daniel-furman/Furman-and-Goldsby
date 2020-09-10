#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:16:44 2020

@author: danielfurman
"""

# In this script we calculate the densification versus age series from 
# all five terrestrial ice sheet profiles. Pressure was converted to age
# via division with the accumulation rate of the site (pressure /
# accumulation rate / gravity). We assume accumulation rate is constant, 
# which is clearly a simplifying approximation.

# required libraries
import pandas as pd
import numpy as np

#vostok

vostok = np.loadtxt('data/Vostok.csv', delimiter = ',')#-57 C
accum_rate_vostok = 22 #kg/m^2 year
vostok_icesheet = np.zeros([len(vostok[:,0]),5]) #initialize
vostok_icesheet[:,0] = vostok[:,0] #pressure in mpa
vostok_icesheet[:,1] = vostok[:,1] * 1e3 #density in kg/m3
vostok_icesheet[:,2] = vostok_icesheet[:,1]/917 #relative dens
vostok_icesheet[:,3] = (vostok[:,0]*1e6/accum_rate_vostok)*(31536000)/9.81 
#age in seconds
vostok_icesheet[:,4] = (vostok[:,0]*1e6/accum_rate_vostok)/9.81
#age in years
#print(vostok_icesheet)

#iterate:

byrd = np.loadtxt('data/Byrd.csv', delimiter = ',') #-28 C
accum_rate_byrd = 157 #kg/m^2 year
byrd_icesheet = np.zeros([len(byrd[:,0]),5])
byrd_icesheet[:,0] = byrd[:,0]
byrd_icesheet[:,1] = byrd[:,1]* 1e3
byrd_icesheet[:,2] = byrd_icesheet[:,1]/917
byrd_icesheet[:,3] = (byrd[:,0]*1e6/accum_rate_byrd)*(31536000)/9.81
#seconds
byrd_icesheet[:,4] = (byrd[:,0]*1e6/accum_rate_byrd)/9.81 
#years

mizuho = np.loadtxt('data/Mizuho.csv', delimiter = ',') #-33 c
accum_rate_mizuho = 70 #kg/m^2 year
mizuho_icesheet = np.zeros([len(mizuho[:,0]),5])
mizuho_icesheet[:,0] = mizuho[:,0]
mizuho_icesheet[:,1] = mizuho[:,1]* 1e3
mizuho_icesheet[:,2] = mizuho_icesheet[:,1]/917
mizuho_icesheet[:,3] = (mizuho[:,0]*1e6/accum_rate_mizuho)*(31536000)/9.81
#seconds
mizuho_icesheet[:,4] = (mizuho[:,0]*1e6/accum_rate_mizuho)/9.81 
#years

domec = np.loadtxt('data/Domec2.csv', delimiter = ',') #-54 c
accum_rate_domec= 34 #kg/m^2 year
domec_icesheet = np.zeros([len(domec[:,0]),5])
domec_icesheet[:,0] = domec[:,0]
domec_icesheet[:,1] = domec[:,1]* 1e3
domec_icesheet[:,2] = domec_icesheet[:,1]/917
domec_icesheet[:,3] = (domec[:,0]*1e6/accum_rate_domec)*(31536000)/9.81 
#seconds
domec_icesheet[:,4] = (domec[:,0]*1e6/accum_rate_domec)/9.81 
#years


g2 = np.loadtxt('data/G2.csv', delimiter = ',') #-29 c
accum_rate_g2= 75 #kg/m^2 year
g2_icesheet = np.zeros([len(g2[:,0]),5])
g2_icesheet[:,0] = g2[:,0]
g2_icesheet[:,1] = g2[:,1]* 1e3
g2_icesheet[:,2] = g2_icesheet[:,1]/917
g2_icesheet[:,3] = (g2[:,0]*1e6/accum_rate_g2)*(31536000)/9.81 #seconds
g2_icesheet[:,4] = (g2[:,0]*1e6/accum_rate_g2)/9.81 #years


# Now calculate some statistics

files = [vostok_icesheet,byrd_icesheet,mizuho_icesheet,domec_icesheet,
         g2_icesheet]

data_nature = [] 
average_age = np.zeros(len(files))
average_pressure = np.zeros(len(files))
strain_rates = np.zeros([len(files),4]) 
j=0
for f in files:

    f = f[(f[:,2]>.8) & (f[:,2]<.9)] #intermediate dens only
    average_age[j] = np.mean(f[:,4])
    average_pressure[j] = np.mean(f[:,0])
    np.savetxt('data/icesheet' + str(j) + '.csv', f, delimiter=',' )
    j+=1
    data_nature.append(f) #store in data_nature
    
j = 0    

# Calculate three rates
for f in files:  
    
    f1 = f[(f[:,2]>.8) & (f[:,2]<.833)]
    dtime = np.max(f1[:,3]) - np.min(f1[:,3])
    ddense = (np.max(f1[:,1]) - np.min(f1[:,1]))
    
    strain_rates[j,0] = (ddense/dtime)/917
    
    f2 = f[(f[:,2]>.833) & (f[:,2]<.866)]
    dtime = np.max(f2[:,3]) - np.min(f2[:,3])
    ddense = (np.max(f2[:,1]) - np.min(f2[:,1]))
    strain_rates[j,1] = (ddense/dtime)/917
    f3 = f[(f[:,2]>.866) & (f[:,2]<.9)]
    dtime = np.max(f3[:,3]) - np.min(f3[:,3])
    ddense = (np.max(f3[:,1]) - np.min(f3[:,1]))
    strain_rates[j,2] = (ddense/dtime)/917
    strain_rates[j,3] = (strain_rates[j,0]+strain_rates[j,1]+
                         strain_rates[j,2])/3
    j+=1
    


strain_rates = pd.DataFrame(strain_rates, index = [
    'Vostok', 'Byrd', 'Mizuho', 'Dome C',  'GISP 2'])
strain_rates.columns = ['rate 1 (pr >.833)', 'rate 2 (.833 < pr <.866)', 
                        'rate 3 (.866 < pr)', 'mean']



