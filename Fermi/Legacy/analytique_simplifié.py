#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:13:11 2022

@author: tefrem49
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt



""" On cherche a trouver les racines de cette fonction , en particulier celle
de plus basse valeur."""
def posmur(t,w,A,x0) :
    return np.cos(w*t) * A +x0
posmur=np.vectorize(posmur)

def posballe(t,vobj) :
    return vobj*t

def TempChoc(x0, Vobjet) :
    return x0/Vobjet

TempsChoc=np.vectorize(TempChoc)

def Vmur(t,w) :
    return -w*np.sin(w*t)


""" quel vitesse atteint la particule apres nchoc avec
le mur mouvant """

def vite(w,x0,A,vobj,n=1000) :
    iteration = 0
    vitesse = []
    
    for i in range(0,n):
    
        #Choc avec mur mouvant
        vobj = -vobj - 2*Vmur(x0/vobj,w)
        
        #Choc avec mur immovible
        vobj=-vobj

    
        iteration +=1
        vitesse.append(vobj)
    return(vitesse,iteration)
    
def vma(w,x0,A,vobj,n=1000,vballevieux=-5) :

    for i in range(0,n):
    
                
        #Choc avec mur mouvant
        vobj = -vobj - 2*Vmur(x0/vobj,w)
        
        #Choc avec mur immovible
        vobj = -vobj

    
    vmaxi = vobj
    return(vmaxi)
 
vmax = np.vectorize(vma)

"""le mur"""
#position mur mouvant
x0 = 10

#frequence oscillation du mur
w  = 10

#Amplitude oscillation
A = 5

#Vitesse objet
vobj = 100


vimax,iteration = vite(w,x0,A,vobj)


plt.figure()
plt.plot(np.arange(0,iteration),np.abs(vimax))
plt.xlabel("itération")
plt.ylabel("vitesse")
plt.title("Vitesse de l'objet")
plt.show()


freq = np.arange(0,200)
vmaximum = vmax(freq,x0,A,vobj)


plt.figure()
plt.title("Vitesse max selon frequence")
plt.plot(freq,np.abs(vmaximum),"r")
plt.xlabel("fréquence")
plt.ylabel("Vmax")
plt.show()


xinit = np.arange(1,100)
vmaximu = vmax(10,xinit,A,vobj)

plt.figure()
plt.title("Vitesse max selon position mur")
plt.plot(xinit,np.abs(vmaximu),"y")
plt.xlabel("x0")
plt.ylabel("Vmax")
plt.show()

Amod = np.arange(1,100)
vmaximu = vmax(10,x0,Amod,vobj)

plt.figure()
plt.title("Vitesse max selon amplitude d'oscillation")
plt.plot(Amod,np.abs(vmaximu),"y")
plt.xlabel("A")
plt.ylabel("Vmax")
plt.show()