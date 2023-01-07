#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:13:11 2022

@author: tefrem49
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

"""On va redefinir tchoc comme une recherche de 0 d'une fonction non linéaire"""


""" On cherche a trouver les racines de cette fonction , en particulier celle
de plus basse valeur."""
def posmur(t,w,A,x0) :
    return np.cos(w*t) * A +x0
posmur=np.vectorize(posmur)

def posballe(t,vobj) :
    return vobj*t

def collision(t,w,A,x0,vobj) :
    return posmur(t,w,A,x0) - posballe(t,w,A,x0,vobj)


def Vmur(t,w) :
    return -w*np.sin(w*t)


""" quel vitesse atteint la particule apres nchoc avec
le mur mouvant """


    
def vma(w,x0,A,vobj,n=1000,vballevieux=-5) :

    for i in range(0,n):
    
        #Choc avec mur immovible
        vobj = -vobj
        
        Tchoc = opt.fsolve(collision,[-A +x0],args = (w,A,x0,vobj))
        #Choc avec mur mouvant
        vobj = - (vobj + 2*Vmur(Tchoc,w))
    
    vmaxi = vobj
    return(vmaxi)
 
vmax = np.vectorize(vma)

"""le mur"""
#position mur mouvant
x0 = 19

#frequence oscillation du mur
w  = 4

#Amplitude oscillation
A = 0.5

#Vitesse objet
vobj = 10
vballevieux = -1




""" ICI RECHERCHE DU TEMPS DE COLLISIONS"""

""" Le temps minimum où la balle et le mur peuvent entrer en collision
    est à une distance -A +x0 par minimisation de la fonction posmur"""
    
tchoc = opt.fsolve(collision,[-A +x0],args = (w,A,x0,vobj))

print(tchoc)




#=========================================================================#
vimax,iteration = vite(w,x0,A,vobj)


plt.figure()
plt.plot(np.arange(0,iteration),np.abs(vimax))
plt.xlabel("itération")
plt.ylabel("vitesse")
plt.title("Vitesse de l'objet")
plt.show()

freq = np.arange(0,20)
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