#=============================Import==========================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#============================Globale==========================
L = 100 #taille espace
#=============================Particule==========================

class particule :
    def __init__(self,position,vitesse,force) :
        self.position = np.random.uniform(0,L)
        self.vitesse = 10 # peut etre random
        self.force = 0

#============================ Gazs ===============================

"""
Les gazs ont :
    - Un nombre
    - Une position
    - Une largeur
    - Une force
    - Une vitesse


"""
N_gazs = 6 #on prend un nombre paire pour que ce soit symétrique #nombre
x_gazs = np.random.rand(N_gazs) * L #position initiale
D_gazs = np.ones(N_gazs)*50 #taille des gazs 

""" force """
temp = np.ones(int(N_gazs))
f_gazs = np.array([])
f_gazs = np.hstack((f_gazs,temp))


"""
On définis la vitesse des gazs de sorte que la vitesse moyenne soit nulle.
Pour ce faire on donne une vitesse aléatoire à la moitié des gazs
et des vitesses opposés à l'autre moitié
"""

temp = np.random.uniform(0,10,int(N_gazs/2))
v_gazs = np.array([])
v_gazs = np.hstack((v_gazs,temp))
v_gazs = np.hstack((v_gazs,-temp))
"""
temp = np.random.rand(N_gazs/2)
np.hstack((v_gazs,temp))
np.hstack((v_gazs,-temp))
"""

# ============================= Force =========================================

def force(x_part,x_gazs,v_gazs,v_part,f_gazs,Longueur_Espace , D_gazs) :
    """ cette fonction détermine les forces auxquels est soumise la particule
    cela dépend de la position de la particule ainsi que de la position des 
    gazs.
    """
    
    
    #La variable force nous sert à stocker les forces soumises à la particule
    
    force = 0
    
    
    #==========================================================================
    #On recentre les gazs et la particule dans la boite
    
    n_gaz = np.floor(x_gazs/L)
    n_part= np.floor(x_part/L)
    
    x_gazs_recentered = x_gazs - n_gaz*L
    x_part_recentered = x_part - n_part*L
    #==========================================================================
    #On vérifie dans quels gazs est la particule
    
    cond1 = (x_part_recentered >= x_gazs_recentered - D_gazs/2) & \
    (x_part_recentered <= x_gazs_recentered + D_gazs/2)
    
    cond2 = (x_part_recentered >= x_gazs_recentered + L - D_gazs/2) & \
    (x_part_recentered <= x_gazs_recentered + L + D_gazs/2)
    
    cond3 = (x_part_recentered >= x_gazs_recentered - L - D_gazs/2) & \
    (x_part_recentered <= x_gazs_recentered - L + D_gazs/2)
    
    
    #==========================================================================
    #On combine les conditions
    cond = cond1 | cond2 | cond3
    print(cond)
    print(np.where(cond)[0])
    #=========================================================================
    #Ici on calcule si les forces sont positive >0 ou <0 en fonction de la 
    #direction de propagation des gazs et de la particule
    
    #Ici on détermine si la particule et le gaz on des vitesse opposé
    #Si oui alors on accelere la particule, si non alors on la décelere
    #décelere = F < 0
    signe = v_gazs[cond] * v_part
    
    f_gazs_temp = f_gazs[np.where(cond)[0]].copy() #seulement les gazs dans lesquels on est
    f_gazs_temp[np.where(signe>0)] = -f_gazs_temp[np.where(signe>0)] #on inverse la force en fonction des vitesses
    print(f_gazs_temp)
    
    
    #==========================================================================
    
    
    
    #Ici on somme les forces des boites qui appliquent leurs force

    force += np.sum(f_gazs_temp)
    
    return force

#Acceleration

def accelerationpart(part,t,force) :
    dvdt = force
    dxdt = part[1]
    
    return [dxdt,dvdt]

def vitessegaz(x_gazs,t,v_gazs) :
    return v_gazs #la vitesse des gazs est constante et ne dép pas de la position


#=========================test==============================================
part = particule(0,1,0)
arraypart = [part.position,part.vitesse]
print(force(part.position,x_gazs,v_gazs,part.vitesse,f_gazs,L,D_gazs))

# #Odeint
print(x_gazs)
# print(v_gazs)
# t = np.linspace(0,10,10)
# x_new = odeint(vitessegaz,x_gazs,t,args=(v_gazs,)) #works allright for gazs
# print(x_new)

res = odeint(accelerationpart,arraypart,t,args=(force()))
#if one of the solution is > or < L : regéneré avec t= cet endroit et x = x-L