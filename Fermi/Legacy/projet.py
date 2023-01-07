import numpy as np
import matplotlib.pyplot as plt

class objet2D :
    def __init__(self,posx,posy,vitesse_x,vitesse_y,accelerationx = 0,accelerationy=0 , harmonique = False) :
        """position initiale tirée aléa ?
            vitesse initiale selon chaque axe
            acceleration ?"""
        self.harmonique = harmonique 

        self.accelerationx = accelerationx
        self.accelerationy = accelerationy
    
        if self.harmonique == True :
            self.vitesse_x = np.cos(posx) + vitesse_x
            self.vitesse_y = np.sin(posx) + vitesse_y
        
        else :
            self.vitesse_x = vitesse_x
            self.vitesse_y = vitesse_y
        
        self.posx = posx
        self.posy = posy
    
    def move(self) :
        self.posx  += self.vitesse_x
        self.posy  += self.vitesse_y
        
    def accelerate(self) :

        if self.harmonique == True :
            self.vitesse_x = np.cos(self.posx) + self.vitesse_x + self.accelerationx
            self.vitesse_y = np.sin(self.posx) + self.vitesse_y + self.accelerationy
        
        else : 
            self.vitesse_x += self.accelerationx
            self.vitesse_y += self.accelerationy
        
    def interact(self,forcex,forcey,mass) :
        self.accelerationx = forcex / mass
        self.accelerationy = forcey / mass
        
    def actualise(self) :
        self.move()
        self.accelerate()
        
class particule(objet2D) :
    def __init__(self,posx,posy,vitesse_x,vitesse_y,accelerationx = 0,accelerationy=0 ,charge=0,harmonique=False):
        self.charge = charge
        objet2D.__init__(self, posx, posy,vitesse_x,vitesse_y,accelerationx = 0,accelerationy=0 , harmonique = harmonique)
        


        
        
#test
        """
x= np.arange(0.0,10.0,0.1)
y=x.copy()
cosinus = np.cos(x)
sinus = np.sin(x)
"""

a = particule(0,1,0,0,harmonique=True)
print(a.vitesse_x)
print(a.vitesse_y)
x= np.zeros(1000)
y= np.zeros(1000)
for i in range(0,1000):
    a.actualise()
    x[i] = a.posx
    y[i] = a.posy

    #print("pos",a.posx,a.posy,"\n")
    #print(a.vitesse_x)
print(a.posx)
print(a.posy)
    
plt.figure()
plt.plot(x,y,"x-")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.show()
        

