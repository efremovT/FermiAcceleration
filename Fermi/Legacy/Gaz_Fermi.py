#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:52:59 2022

@author: tefrem49
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def NewtonRaphson_Dicho( f,fprime , a , b , eps , *args , **kwargs) :
       
    """ 
    - avec f un tableau de valeur , cad une fontion f appliquer a un array t
    - fprime dérver de la fonction f
    - a la borne inférieur de notre recherche
    - b la borne supérieur de notre recherche
    - eps la marge d'erreur admise
    -Extra_args est un tuple avec les argument de f et fprime
    
    Cette fonction est juste la méthode de Newton Raphson dont on améliore 
    la vitesse de convergence grace a un test conditionnel tq : si la racine
    estimé par la dérivé est en dehors de l'intervalle donné en argument
    alors utiliser la méthode de dichotomie
    """
    f(*args ,**kwargs)
    
    
    
    t = a
    tnew = t - (f(t,**kwargs) / fprime(t,**kwargs))
    #changer de borne mieux
    if (f(a,**kwargs) * f(b,**kwargs)) >0 :
        return False
    
    while (abs(tnew-t)>eps):
        """ si on sort de l'intervale a,b alors on utilise dicho"""
        if (tnew > b)  :
            LargeurInterv = b-t
            m = t + LargeurInterv/2
            
            if (f(t,**kwargs) * f(m,**kwargs))  < 0 :
                tnew = m
            else :
                t = m
        if (tnew<a) :
            LargeurInterv = b - t
            m = t + LargeurInterv/2
            #print(m)
            if (f(t,**kwargs) * f(m,**kwargs))  < 0 :
                tnew = m
            else :
                t = m
        
        else :
            """ si on reste dans l'intervalle a,b c'est tres bien alors on recommence"""
            #print('a')
            t = tnew
            tnew = t - f(t,**kwargs) / fprime(t,**kwargs)
        
    #print(t)
    return t

def recherche(f,fprime , t, borneinf , bornesup , eps , *args , **kwargs):
    """ fonction intermédiaire pour calculer forcément un 0 entre deux
    demi-période, n'est utilisable que en cos"""
    res = NewtonRaphson_Dicho( f,fprime , t , borneinf , eps , *args , **kwargs)
    if res == False :
        res = NewtonRaphson_Dicho( f,fprime , borneinf , bornesup , eps , *args , **kwargs)
            
    return res

""" la question des bornes se pose, il faut trouver le 0 de la fonction
    entre tmin et la premiere demi periode on doit donc faire 
   
                                pi/w *n >tmin 
    
    avec n un entier naturelle 
    
    
    prendre comme borne [tmin,pi/w*n] et si il n'existe pas de solution 
    chercher plus loin entre [pi/w*n ; pi/w*(n+1)]
    
    
    mas comment trouver n ? on va prendre l'entier naturelle juste au dessus
    de w*tmin/pi ou celui juste en dessous de x*tmin/pi +1"""
    
def Bornes(tmin,w):
    """ la fonction floor donne l'entier naturelle inférieure le plus proche"""
    ninf = np.floor( w * tmin/np.pi + 1)
    nsup = np.floor( w * tmin/np.pi + 3) #voyons large
    
    borneinf = np.pi / w * ninf
    bornesup = np.pi / w * nsup
    
    return borneinf , bornesup

#=============================== On passe a la pratique ======================
def XMur (t,w,A,x0) :
    """ pos la position du mur et DemiPer la demi-periode d'oscillation"""
    
    pos = x0 + A*np.cos(w*t)
    return pos

def Vmur (t,w,A,x0) :
    v = -A*w*np.sin(w*t)
    return v

def XBalle(t,v,x0_balle,t0) :
    return v*(t-t0) + x0_balle

def Contact_raquette(t,v, w, A , x0_mur ,x0_balle , t0) :
    """ L'equation dont on cherche la première racine"""
    
    res = XMur(t,w,A,x0_mur) - XBalle(t,v,x0_balle,t0)
    
    return res


def ContactPrime_raquette(t,v , w, A , x0_mur ,x0_balle,t0 ) :
    """ Sa dérivé nécessaire pour NR"""
    res = -A*w*np.sin(w*t) - v
    return res

def TExtremum(t,v,A,x_balle,x_mur) : #Avant il y avait x0 = xequmur
    """
       - temps minimum/maximum que prend la balle a toucher le mur
       - Ce sera la base de nos borne pour déterminer les 0 de Contact
       
       """
    tmin = (x_mur - x_balle - A)/v + t
    tmax = (x_mur - x_balle + A)/v + t

    return tmin, tmax

def Contact_mur_immobile(t,v,x_balle,t0,x_mur_gauche =0 ) :
    t = -x_balle/v +t0
    return t

