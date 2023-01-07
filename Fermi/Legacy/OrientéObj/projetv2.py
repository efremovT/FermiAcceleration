#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:26:44 2022

@author: tefrem49
"""
import numpy as np
import matplotlib.pyplot as plt

class objet2D :
    def __init__(self,posx,posy,vitesse,angle,accelerationx = 0,accelerationy=0 ) :
        """ on considère un objet ponctuelle se déplacant dans un espace 2d 
            avec une vitesse et un angle de propagation par rapport a x.
            pour modifier la direction de propagation il sufira de changer
            theta dans la boucle en temps"""
        self.accelerationx = accelerationx
        self.accelerationy = accelerationy

        self.vitesse = vitesse
        self.angle = angle
        
        self.posx = posx
        self.posy = posy
    
    def move(self) :
        self.posx  += self.vitesse * np.cos(self.angle)
        self.posy  += self.vitesse * np.sin(self.angle)
        
    def accelerate(self) :
        pass
        
    def interact(self,forcex,forcey,mass) :
        self.accelerationx = forcex / mass
        self.accelerationy = forcey / mass
        
    def actualise(self) :
        self.move()
        self.accelerate()
    
    def turn(self,theta) :
        self.angle += theta
        
class particule(objet2D) :
    def __init__(self,posx,posy,vitesse,angle,accelerationx = 0,accelerationy=0 ,charge=0):
        self.charge = charge
        objet2D.__init__(self, posx, posy,vitesse,angle,accelerationx = 0,accelerationy=0 )
        

class nuage(objet2D) :
    
        
        
#test

a = particule(1,1,2,2)
posx= []
posy=[]
for i in range(0,100) :
    a.actualise()
    a.turn(1)
    posx.append(a.posx)
    posy.append(a.posy)
    
    
plt.figure()
plt.plot(posx,posy,"x")
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()