#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:16:44 2020

@author: danielfurman
"""

# This lengthy script constrains the strain-stress constitutive model, 
# describing densification with several physical variables. We use 
# Eq. 1 to analyze the data, taking each series' mean relative density.
# We then output several plots, including the p parameter calculation,
# the flow law behind the experimental data, and the firn flow law versus 
# the solid ice flow law.  

# required libraries
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sympy.solvers import solve
from sympy import Symbol
import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats

# FLow law fitting

paper_table = pd.read_csv('data/paper_table_full.csv', delimiter=',',
                          header = 'infer') 

plt.ylabel('$log$  $\.\epsilon$  (dl/ldt)')
plt.xlabel('$log$ $\sigma$ (Mpa)')
plt.title('Experimental Data, 233 K', fontweight = 'bold')
stress=np.array([.2, .8, 1.6])

# log-log linear regression of power law relationship for green series
y = np.array(paper_table['Densification rate'][6:10])
X = np.array(paper_table['applied stress'][6:10])
y = np.log(y)
X = np.log(X)
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)
reg2 = LinearRegression().fit(X, y)


# log-log linear regression of power law relationship for blue series
y = np.array(paper_table['Densification rate'][10:15])
X = np.array(paper_table['applied stress'][10:15])
y = np.log(y)
X = np.log(X)
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)
reg = LinearRegression().fit(X, y)

# log-log linear regression of power law relationship for red series
y = np.array(paper_table['Densification rate'][0:6])
X = np.array(paper_table['applied stress'][0:6])
y = np.log(y)
X = np.log(X)
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)
reg1 = LinearRegression().fit(X, y)

print('\nGSS n exponent:',"\n\t{:.4}".format(np.mean(np.array([(
    reg.coef_),(reg2.coef_)]))))
print('Disl creep n exponent:',"\n\t{:.4}".format(np.mean(np.array([(
    reg1.coef_)]))))

#fit p parameter


plt.loglog(stress,(np.exp(reg.intercept_)*stress**reg.coef_[0]), 'b--',
           alpha = .7, lw = 3, label = '')

plt.loglog(stress,(np.exp(reg2.intercept_)*stress**reg2.coef_[0]), 'g--',
           alpha = .9, lw = 3, label = '')

plt.loglog([paper_table['applied stress'][7:10]],
           [paper_table['Densification rate'][7:10]],'g^', markersize=14)
plt.loglog([paper_table['applied stress'][6]],
           [paper_table['Densification rate'][6]],'g^', markersize=14,
           label = 'grain radius = 17 um')

plt.loglog([paper_table['applied stress'][11:15]],
           [paper_table['Densification rate'][11:15]],'bd', markersize=14)
plt.loglog([paper_table['applied stress'][10]],
           [paper_table['Densification rate'][10]],'bd', markersize=14,
           label = 'grain radius = 5 um')

#solving for p
stresses = np.linspace(.4,1.3,10)

for i in stresses:
    plt.axvline(x = i, ymax = 1, ymin = 0, color = 'k', lw = '.6',ls = '-')
    
p = Symbol('p')
n = 1.625

ps = np.zeros(len(stresses))
for i in range(0,len(stresses)):
    ps[i]=( solve((((1-.818)/((1-(1-.818)**(1/n))**n))*((1/(2*1.68e-5)**p)))/(
        (1/(2*5e-6)**p)*((1-.831)/((1-(1-.831)**(1/n))**n))) - ((np.exp(
                reg2.intercept_)*stresses[i]**reg2.coef_[0])/(np.exp(
                    reg.intercept_)*stresses[i]**reg.coef_[0])),p))[0]

print('\n\nGSS p exponent:',"\n\t{:.4}".format(np.mean(ps)))
bs1 = bs.bootstrap(ps, stat_func=bs_stats.mean)
print('the p exponent bootstrapped uncertainty estimate:')
print('\t' + str(bs1))
plus_minus = np.mean([0.89659-0.87511, 0.91622-0.89659])
print('\t%.11g +- %.11g'%(0.89659 ,plus_minus))

stress = np.array(paper_table['applied stress'][6:15])
rate = np.array(paper_table['Densification rate'][6:15])
pr = np.array(paper_table['Mean dens'][6:15])
r = np.array([1.68e-5, 1.68e-5, 1.68e-5, 1.68e-5, 5e-6, 5e-6, 5e-6,5e-6, 5e-6])

#experimental A pre-exponential calculation GBS creep
p = .8966
A = Symbol('A') 
results = np.zeros(len(stress))
T = 233
n3 = 1.625

for i in range(0,len(rate)):
    a = (solve( rate[i] - ((2*A*(1-pr[i])/((1-(1-pr[i])**(1/n3))**n3)) *(((
        2*stress[i])/n3)**n3)*(1/(2*r[i])**p)) ,A))
    results[i] = a[0]/ np.exp(-49000/(8.314*T))
print('\n\nThe A parameter for the GSS flow law is:',
      "\n\t{:.4}".format(np.mean(results)))

bs1 = bs.bootstrap(results,stat_func=bs_stats.mean)
print('The A parameter bootstrapped uncertainty estimate:')
print('\t' + str(bs1))
plus_minus = np.mean([0.44313-0.40187, 0.47870-0.44313])
print('\t%.11g +- %.11g'%(0.44313 ,plus_minus))

#experimental A pre-exp calculation disl creep

stress = np.array(paper_table['applied stress'][0:6])
rate = np.array(paper_table['Densification rate'][0:6])
pr = np.array(paper_table['Mean dens'][0:6])

A = Symbol('A') 
results = np.zeros(len(rate))
T = 233
n = 3.74
for i in range(0,len(rate)):
    a = (solve( rate[i] - ((2*A*(1-pr[i])/((1-(1-pr[i])**(1/n))**n))*(((
        2*stress[i])/n)**n)) ,A))
    results[i] = a[0]/ np.exp(-60000/(8.314*T))
print('The A parameter for the disl creep flow law is:')
print("\t{:.4}".format(np.mean(results)))

bs1 = bs.bootstrap(results,stat_func=bs_stats.mean)
print('The A parameter bootstrapped uncertainty estimate:')
print('\t' + str(bs1))
plus_minus = np.mean([148140-122530, 172780-148140])
print('\t%.11g +- %.11g'%(148140 ,plus_minus))




## Plotting of fit against rate tests:



plt.figure()

# flow law with exp data

R = 8.314
r = 5e-6 #radius in meters, 
A = 1.48e5*np.exp(-60000/(8.314*T))
n = 3.74
n3 = 1.625
A_gbs = 0.4431*np.exp(-49000/(8.314*T))
pr = .831
p = .8966

stress = np.arange(6e-2, 10,.001)
rate_gbs = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_gbs[i] = ((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((
        2*stress[i])/n3)**n3)*(1/(2*r)**p))

rate_dc = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_dc[i] = (2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*stress[i])/n)**n)

plt.loglog(stress[rate_dc>rate_gbs],rate_dc[rate_dc>rate_gbs],
           lw=4,color='dimgrey',alpha=.4, label = 'sole-mechanism flow law')
plt.loglog(stress[rate_dc<rate_gbs],rate_gbs[rate_dc<rate_gbs],
           lw=4,color='dimgrey',alpha=.4)

pr = .818
r = 1.68e-5

stress = np.arange(6e-2, 10,.001)
rate_gbs = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_gbs[i] = ((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((
        2*stress[i])/n3)**n3)*(1/(2*r)**p))

rate_dc = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_dc[i] = (2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*stress[i])/n)**n)

plt.loglog(stress[rate_dc>rate_gbs],rate_dc[rate_dc>rate_gbs],lw=4,
           color='dimgrey',alpha=.4)
plt.loglog(stress[rate_dc<rate_gbs],rate_gbs[rate_dc<rate_gbs],lw=4,
           color='dimgrey',alpha=.4)

r = 1.87e-4
pr=.815
stress = np.arange(6e-2, 10,.001)
rate_gbs = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_gbs[i] = ((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((
        2*stress[i])/n3)**n3)*(1/(2*r)**p))

rate_dc = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_dc[i] = (2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*stress[i])/n)**n)

plt.loglog(stress[rate_dc>rate_gbs],rate_dc[rate_dc>rate_gbs],lw=4,
           color='dimgrey',alpha=.4)
plt.loglog(stress[rate_dc<rate_gbs],rate_gbs[rate_dc<rate_gbs],lw=4,
           color='dimgrey',alpha=.4)


# plot raw experimental rates
plt.loglog([paper_table['applied stress'][1:6]],
           [paper_table['Densification rate'][1:6]],'r*', markersize=17)
plt.loglog([paper_table['applied stress'][0]],
           [paper_table['Densification rate'][0]],'r*', markersize=17,
           label = 'grain radius = 187 um')

plt.loglog([paper_table['applied stress'][7:10]],
           [paper_table['Densification rate'][7:10]],'g^', markersize=14)
plt.loglog([paper_table['applied stress'][6]],
           [paper_table['Densification rate'][6]],'g^', markersize=14,
           label = 'grain radius = 17 um')

plt.loglog([paper_table['applied stress'][11:15]],
           [paper_table['Densification rate'][11:15]],'bd', markersize=14)
plt.loglog([paper_table['applied stress'][10]],
           [paper_table['Densification rate'][10]],'bd', markersize=14,
           label = 'grain radius = 5 um')

plt.loglog([paper_table['applied stress'][15]],
           [paper_table['Densification rate'][15]],'k.', markersize=21,
           label = 'grain radius = 550 um')

# set plotting params
plt.ylabel('$log$  $\.\epsilon$  (dp/p dt)')
plt.xlabel('$log$ $\sigma$ (Mpa)')
plt.title('Experimental Densification Rate, 233 K', fontweight = 'bold')
plt.grid(axis = 'y')
plt.xlim([6e-2,10])
plt.ylim([7e-10,4e-6])

stress = np.arange(.6, 2.2,.2)
plt.loglog(stress,(np.exp(reg1.intercept_)*stress**reg1.coef_[0]), 'r--', 
           alpha = .7, lw = 3, label = '')

stress = np.arange(.3, 2.35,.2)

plt.loglog(stress,(np.exp(reg2.intercept_)*stress**reg2.coef_[0]), 'g--', 
           alpha = .7, lw = 3, label = '')

stress = np.arange(.17, 2.39,.2)

plt.loglog(stress,(np.exp(reg.intercept_)*stress**reg.coef_[0]), 'b--',
           alpha = .7, lw = 3, label = '')

plt.legend(loc='best', shadow = True)

#plt.savefig('images/expdatadens_final.png', dpi = 400)


### Plotting flow law against solid ice flow law


plt.figure()

# set parameters for solid ice flow law (Goldsby 2006)

R = 8.314 #gas constant
T=233
r = 1e-3 #radius in meters
A = 1.2*10**6*np.exp(-60000/(8.314*T))
n = 4
n3 = 1.8
A_gbs = 3.9*10**-3*np.exp(-49000/(8.314*T))

stress = np.arange(.000001, 20,.00005)

rate_gbs = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_gbs[i] = (A_gbs)*((stress[i])**n3)*(1/(2*r))**(1.4)


rate_dc = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_dc[i] = (A)*((stress[i])**n)

plt.loglog(stress,rate_dc+rate_gbs,lw=5,color='blue',alpha=.6,
           label = 'Ice Flow Law (Goldsby 2006)')

# Now contrast with densification flow law

A = 1.481e5*np.exp(-60000/(8.314*T))
n = 3.74
n3 = 1.63
A_gbs = .443*np.exp(-49000/(8.314*T))
p = .897
pr = 0.8

stress = np.arange(.000001, 20,.00005)
rate_gbs = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_gbs[i] = ((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((
        2*stress[i])/n3)**n3)*(1/(2*r)**p))


rate_dc = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_dc[i] = (2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*stress[i])/n)**n)
   
pr=.90
d = r*((1-pr)**(1/3))
stress = np.arange(.000001, 20,.00005)
rate_gbs1 = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_gbs1[i] = ((2*A_gbs*(1-pr)/((1-(1-pr)**(1/n3))**n3))*(((
        2*stress[i])/n3)**n3)*(1/(2*r)**p))


rate_dc1 = np.zeros(len(stress))
for i in range(0,len(stress)):
    rate_dc1[i] = (2*A*(1-pr)/((1-(1-pr)**(1/n))**n))*(((2*stress[i])/n)**n)

plt.fill_between(stress, y1 = rate_dc1+rate_gbs1 ,y2 = rate_dc+rate_gbs,
                 alpha = 0.3,color = 'red')
plt.loglog(stress,rate_dc1+rate_gbs1,lw=5,color = 'red', alpha=.5)
plt.loglog(stress,rate_dc+rate_gbs,lw=5,color='red',alpha=.5,
           label = 'Firn flow law (0.8<pr<0.9)')



plt.ylabel('$log$  $\.\epsilon$  (dp/p dt)')
plt.xlabel('$log$ $\sigma$ (Mpa)')
plt.title('Flow Law Models: T = 233, r = 1 mm')
plt.grid(axis = 'y')
plt.xlim([1e-3,10])
plt.ylim([1e-13,1e-5])
plt.legend()
#plt.savefig('images/genflowlaw.png', dpi = 400)




