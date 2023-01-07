#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:13:11 2022

@author: tefrem49
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck


def vn (v0,w,a,d,n) :
    """ v0 vitesse initiale
        w pulsation
        a amplitude oscillation mur
        d distance entre les 2 murs
        n nombre de rebond"""
        
    #def var
    u0 = v0 / 2*a*w
    M = d/2*np.pi*a    
    psi0 = w*d / v0
    
    #position initiale
    un = u0
    psi = psi0
    for i in range(0,n) :
        psi = psi + 2*np.pi*M/un
        un = abs(un + np.sin(psi) )
    
    vn = 2*a*w *un
    return(vn,psi)
    



def veso (u0,psi0,a,d,n=500000) :
    """ v0 vitesse initiale
        w pulsation
        a amplitude oscillation mur
        d distance entre les 2 murs
        n nombre de rebond"""
        
    M = d/2*np.pi*a    
    #position initiale
    un = u0
    psi = psi0
    
    utot = np.zeros(n)
    psitot = np.zeros(n)
    
    for i in range(0,n) :
        un = abs(un + np.sin(psi) )
        psi = psi + 2*np.pi*M/un
        
        
        utot[i] = un
        psitot[i] = psi
    return(utot,psitot)
vesoterique = np.vectorize(veso)

def PsiNormal(psi) :
    x = np.sin(psi)
    y = np.cos(psi)
    psi = np.arctan2(x,y)
    
    return psi
PsiNormalisation = np.vectorize(PsiNormal)

psi0 = np.pi/2 #position initiale
u0 = 2#Vitesse initiale
a=5#amplitude oscillation mur
d=13.6 #distance mur-mur

u,psi = veso(u0,psi0,a,d)

""" il faut maintenant projeter les psi dans l'intervale -pi;pi de manière univoque"""
x = np.sin(psi)
y = np.cos(psi)
psi = np.arctan2(x,y)


plt.figure()
f,ax=plt.subplots(figsize=(5,10))
ax.plot(psi/np.pi,u,",",markersize=0.001,color="black")
ax.set_xlabel("$\psi$")
ax.set_ylabel("u")
ax.set_title("Fermi map")
ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))
#ax.legend()
plt.savefig("Fermimap.png")

"""partie triangulaire"""

def triangle(u0,psi0,w,a,d,n=500000):
    """ v0 vitesse initiale
    w pulsation
    a amplitude oscillation mur
    d distance entre les 2 murs
    n nombre de rebond"""
        
    #position initiale
    vn = u0
    psi = psi0
    
    vtot = np.zeros(n)
    psitot = np.zeros(n)
    
    for i in range(0,n) :
        
        psi = PsiNormal(psi)
        #print(psi)
        
        if (psi < 0) and (psi >= -np.pi ) :
            vn = np.abs(vn-2*a)
            
        elif (psi>0) and (psi <= np.pi) :
            vn = np.abs(vn+2*a)
            
        elif psi==0 :
            vn = vn
            
        else :
            print("error")
        
        if vn != 0 :
            psi = psi + 2*w*d/vn
        #print(psi)
        else :
            return (vtot,psitot)
        
        vtot[i] = vn
        psitot[i] = psi
    return(vtot,psitot)
    
psi0 = np.pi/2 #position initiale
u0 = 2#Vitesse initiale
a=5#amplitude oscillation mur
d=13.6 #distance mur-mur
w=1 #freq

u,psi = triangle(u0,psi0,w,a,d)

""" il faut maintenant projeter les psi dans l'intervale -pi;pi de manière univoque"""
x = np.sin(psi)
y = np.cos(psi)
psi = np.arctan2(x,y)


plt.figure()
f,ax=plt.subplots(figsize=(5,10))
ax.plot(psi/np.pi,u,",",markersize=0.001,color="black")
ax.set_xlabel("$\psi$")
ax.set_ylabel("u")
ax.set_title("Fermi map triangulaires")
ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))
#ax.legend()
plt.savefig("triangulaire.png")