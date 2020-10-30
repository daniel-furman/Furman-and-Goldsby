#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 16:50:41 2020

@author: danielfurman
"""

import pandas as pd
import numpy as np
import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats

master_df_pd = pd.read_csv('data/resamp.csv', delimiter=',', header = 'infer')

# take bootstrapped samples of dens rates calculated for pe = .627 MPa at 253
# K with grain radius of 187 um
samples = np.array( [master_df_pd['experimental densification rate'][0],
                     master_df_pd['experimental densification rate'][1], 
                     master_df_pd['experimental densification rate'][2]] )

bs1 = bs.bootstrap(samples, stat_func=bs_stats.mean)
print('the first rate measurement bootstrapped uncertainty estimate:')
print('\t' + str(bs1))

# take bootstrapped samples of dens rates calculated for pe = 1.16 MPa at 253
# K with grain radius of 187 um
samples = np.array( [master_df_pd['experimental densification rate'][3],
                     master_df_pd['experimental densification rate'][4],
                     master_df_pd['experimental densification rate'][5]] )


bs1 = bs.bootstrap(samples, stat_func=bs_stats.mean)
print('\nthe second rate measurement bootstrapped uncertainty estimate:')
print('\t' + str(bs1))

paper_table = pd.read_csv('data/paper_table_full.csv', delimiter=',',
                          header = 'infer') 

samples = np.array(paper_table['Mean dens'][0:6])
bs1 = bs.bootstrap(samples, stat_func=bs_stats.mean)
print('\nthe density bootstrapped uncertainty for the red series:')
print('\t' + str(bs1))
plus_minus = np.mean([0.81474-0.81147, 0.81811-.81474])
print('\t%.11g +- %.11g'%(.81474 ,plus_minus))

samples = np.array(paper_table['Mean dens'][6:10])
bs1 = bs.bootstrap(samples, stat_func=bs_stats.mean)
print('\nthe density bootstrapped uncertainty for the green series:')
print('\t' + str(bs1))
plus_minus = np.mean([0.81812-0.81029, 0.82447-.81812])
print('\t%.11g +- %.11g'%(0.81812 ,plus_minus))

samples = np.array(paper_table['Mean dens'][10:15])
bs1 = bs.bootstrap(samples, stat_func=bs_stats.mean)
print('\nthe density bootstrapped uncertainty for the green series:')
print('\t' + str(bs1))
plus_minus = np.mean([0.83112-0.82551, 0.83673-.83112])
print('\t%.11g +- %.11g'%(.83112 ,plus_minus))
