#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 12:00:46 2023

@author: efrem
"""
import numpy as np
import matplotlib.pyplot as plt


V_histo = np.load("data.npy")
N_simu = len(V_histo[0])
Nbins = int(1+np.log2(N_simu)) +10
print(Nbins)


plt.figure()
res = plt.hist(V_histo[0],bins = Nbins , histtype="bar" ,color = "orange" , edgecolor="black" )
plt.vlines(100, 0, np.max(res[0]+100),colors='black',linestyles='dashed')
plt.ylim(0,np.max(res[0]+100))
plt.ylabel("$N_{particule}$")
plt.xlabel("$V_{max}$")
plt.savefig("Histogramme.png")