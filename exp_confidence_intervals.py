#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:05:18 2020

@author: danielfurman
"""

# Densification rate (dp/p)dt versus applied stress (log-log space).
# Uncertainty estimates of the linear slope {n = 1.57 ± 0.22, n = 1.68 ± 0.45,
# n = 3.74 ± 1.02} represent the 95% confidence intervals of each linear
# regression, which are plotted below.

# These rate data also constrain a flow law model (see Firn_notebook.ipynnb)
# by taking the rate-limiting mechanism as dominant.

# Required Libraries:

import numpy as np
import matplotlib.pylab as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats

paper_table = pd.read_csv('data/paper_table_full.csv', delimiter=',',
                          header = 'infer') 

# log-log linear regression of power law relationship for green series
y = np.array(paper_table['Densification rate'][6:10])
X = np.array(paper_table['applied stress'][6:10])
y = np.log(y)
X = np.log(X)

slope, intercept, r_value, p_value, std_err = stats.linregress(X,y)
reg_conf = 1.96*std_err # 95 percent confidence interval

# reshape for sklearn library
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)
reg = LinearRegression().fit(X, y)


# log-log linear regression of power law relationship for blue series
y = np.array(paper_table['Densification rate'][10:15])
X = np.array(paper_table['applied stress'][10:15])
y = np.log(y)
X = np.log(X)

slope, intercept, r_value, p_value, std_err = stats.linregress(X,y)
reg1_conf = 1.96*std_err # 95 percent confidence interval

# reshape for sklearn library
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)
reg1 = LinearRegression().fit(X, y)


# log-log linear regression of power law relationship for red series
y = np.array(paper_table['Densification rate'][0:6])
X = np.array(paper_table['applied stress'][0:6])
y = np.log(y)
X = np.log(X)

slope, intercept, r_value, p_value, std_err = stats.linregress(X,y)
reg2_conf = 1.96*std_err # 95 percent confidence interval

# reshape for sklearn library
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)
reg2 = LinearRegression().fit(X, y)


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
plt.ylabel('$log$  $\.\epsilon$  (dp/pdt)')
plt.xlabel('$log$ $\sigma$ (Mpa)')
plt.title('Experimental Densification Rates, 233 K', fontweight = 'bold')
plt.grid(axis = 'y')
plt.xlim([6e-3,10])
plt.ylim([1e-13,1e-6])

# initiate x axis stretching to polar rates of densification
stress = np.arange(6e-3, 10,.001)

# plot the linear regression and uncertainty intervals
plt.loglog(stress,(np.exp(reg.intercept_)*stress**reg.coef_[0]),
           'g--', alpha = .7, lw = 3, label = '')
plt.fill_between(stress, np.exp(reg.intercept_)*stress**(1.68-reg_conf),
                 y2=np.exp(reg.intercept_)*stress**(1.68+reg_conf),
                 alpha = 0.3,color = 'green')

plt.loglog(stress,(np.exp(reg1.intercept_)*stress**reg1.coef_[0]),
           'b--', alpha = .7, lw = 3, label = '')
plt.fill_between(stress, np.exp(reg1.intercept_)*stress**(1.57-reg1_conf),
                 y2=np.exp(reg1.intercept_)*stress**(1.57+reg1_conf),
                 alpha = 0.3,color = 'blue')

plt.loglog(stress,(np.exp(reg2.intercept_)*stress**reg2.coef_[0]),
           'r--', alpha = .7, lw = 3, label = '')
plt.fill_between(stress, np.exp(reg2.intercept_)*stress**(3.74-reg2_conf),
                 y2=np.exp(reg2.intercept_)*stress**(3.74+reg2_conf),
                 alpha = 0.3,color = 'red')

plt.legend(loc='lower right', shadow = True)
#plt.savefig('images/expinterv.png', dpi = 400)



