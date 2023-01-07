#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:50:14 2023

@author: efrem
"""

import numpy as np
import matplotlib.pyplot as plt


A = 5
w = 4
X0 = 10


x = np.linspace(0,10,1000)
sinoide = A*np.cos(w*x) + X0

plt.figure(figsize=(7,5))
plt.plot(x,2*x ,label="$v_{balle} = 2t $")
plt.plot(x,sinoide,label="$v_{mur} = 5 \cos (4t) + 10$")
plt.xlabel("t")
plt.ylabel("x")
plt.hlines(5,0,10,colors="black",linestyles="dashed", alpha = 0.6)
plt.hlines(15,0,10,colors="black",linestyles="dashed", alpha = 0.6)
plt.vlines(5/2,-1,21,colors="black",linestyles="dashed", alpha = 0.6)
plt.vlines(15/2,-1,21,colors="black",linestyles="dashed" , alpha = 0.6)
plt.text(2.5,-2,'$t_{min}$')
plt.text(7,-2,'$t_{max}$')
plt.text(-1.5,4.8,'$x_{min}$')
plt.text(-1.5,14.8,'$x_{max}$')
plt.xlim(0,10)
plt.ylim(-0.5,20.5)
plt.legend()
plt.savefig("sinusoplot.png",dpi=500)

A = 5
w = 4
X0 = 10


x = np.linspace(0,10,1000)
sinoide = A*np.cos(w*x) + X0

plt.figure(figsize=(7,5))
plt.plot(x,2*x )
plt.plot(x,sinoide)
plt.xlabel("t")
plt.ylabel("x")
plt.hlines(5,0,10,colors="black",linestyles="dashed", alpha = 0.6)
plt.hlines(15,0,10,colors="black",linestyles="dashed", alpha = 0.6)
plt.vlines(5/2,-1,21,colors="black",linestyles="dashed", alpha = 0.6)
plt.xlim(2,5)
plt.ylim(3,16)

plt.vlines(5*np.pi/4,-1,21,colors="red",linestyles="dashed",label="Borne sup", alpha = 0.6)
plt.vlines(4*np.pi/4,-1,21,colors="green",linestyles="dashed",label="$Borne Inf$", alpha = 0.6)
plt.legend()
plt.savefig("solution.png",dpi=500)