# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:06:57 2020

@author: Asha
"""


from spacepy import pycdf
import numpy as np
fgm = '/Users/Asha/Desktop/MMS/05052019_fgm.cdf'
moms = '/Users/Asha/Desktop/MMS/05052019_moms.cdf'
fgm_cdf = pycdf.CDF(fgm)
moms_cdf = pycdf.CDF(moms)

#fgm
print(fgm_cdf)
data = fgm_cdf['mms1_fgm_b_gse_brst_l2'][1280:4880,3]
avg_fgm = np.mean(data)*10**-9
print(avg_fgm)


#radius
data = fgm_cdf['mms1_fgm_r_gse_brst_l2'][2:3,3]
avg_radkm = np.mean(data)
avg_rad = avg_radkm/6378.14
print(avg_rad)


#number density
print(moms_cdf)
data = moms_cdf['mms1_dis_numberdensity_brst'][153:613]
avg_numbdens = np.mean(data)*1000000
print(avg_numbdens)


#Temperature
data = moms_cdf['mms1_dis_temppara_brst'][153:613]
avg_paratemp = np.mean(data)

data = moms_cdf['mms1_dis_tempperp_brst']
avg_perptemp = np.mean(data)

avg_temp = (1/3*(avg_paratemp)+2/3*(avg_perptemp))*11604.525
print(avg_temp)


#constants
boltz = 1.381e-23
mu = 1.257e-6

#beta value
beta = (2*mu*avg_numbdens*boltz*avg_temp)/(avg_fgm)**2
print(beta)   
print(avg_rad)