# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 03:12:19 2022

@author: theodore
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 00:11:17 2022

@author: theodore
"""


#=============================Import==========================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#============================Globale==========================
L = 100 #taille espace
#np.random.seed(3)
Tmax = 2000
timeres= 1e-4
vinit = 100
#=============================Particule==========================

class particule :
    def __init__(self,position,vitesse,force) :
        self.position = position
        self.vitesse = vitesse # peut etre random
        self.force = force

#============================ Gazs ===============================

"""
Les gazs ont :
    - Un nombre
    - Une position
    - Une largeur
    - Une force
    - Une vitesse


"""
N_gazs = 2 #on prend un nombre paire pour que ce soit symétrique #nombre
#x_gazs = np.random.rand(N_gazs) * L
x_gazs = np.array([20,60]) #position initiale
D_gazs = np.ones(N_gazs)*20#taille des gazs 

""" force """
temp = np.ones(int(N_gazs))*1
f_gazs = np.array([])
f_gazs = np.hstack((f_gazs,temp))


"""
On définis la vitesse des gazs de sorte que la vitesse moyenne soit nulle.
Pour ce faire on donne une vitesse aléatoire à la moitié des gazs
et des vitesses opposés à l'autre moitié
"""
#temp = np.random.uniform(0,100,int(N_gazs))
#temp = np.random.uniform(0,100,int(N_gazs/2))
temp = np.ones(int(N_gazs/2))*0.00001 #gaz quasi imobile

v_gazs = np.array([])
v_gazs = np.hstack((v_gazs,temp))
v_gazs = np.hstack((v_gazs,-temp))
"""
temp = np.random.rand(N_gazs/2)
np.hstack((v_gazs,temp))
np.hstack((v_gazs,-temp))
"""
#petite fonction qui déplace les gazs
def xgaz(x_gazs,t,v_gazs) :
    res = x_gazs + v_gazs*t
    return res
# ============================= Force =========================================

def forceing(t,part,x_gazs,v_gazs,f_gazs,Longueur_Espace , D_gazs) :
    """ cette fonction détermine les forces auxquels est soumise la particule
    cela dépend de la position de la particule ainsi que de la position des 
    gazs.
    """

    x_gazs_new = xgaz(x_gazs,t,v_gazs)
    x_part = part[0]  
    v_part = part[1]  
    
    #La variable force nous sert à stocker les forces soumises à la particule
    
    force = 0
    
    
    #==========================================================================
    #On recentre les gazs et la particule dans la boite
    
    n_gaz = np.floor(x_gazs_new/L)
    n_part= np.floor(x_part/L)
    
    x_gazs_recentered = x_gazs_new - n_gaz*L
    x_part_recentered = x_part - n_part*L
    #==========================================================================
    #On vérifie dans quels gazs est la particule
    
    cond1 = (x_part_recentered >= x_gazs_recentered - D_gazs/2) & \
    (x_part_recentered <= x_gazs_recentered + D_gazs/2)
    
    cond2 = (x_part_recentered >= x_gazs_recentered + L - D_gazs/2) & \
    (x_part_recentered <= x_gazs_recentered + L + D_gazs/2)
    
    cond3 = (x_part_recentered >= x_gazs_recentered - L - D_gazs/2) & \
    (x_part_recentered <= x_gazs_recentered - L + D_gazs/2)
    
    cond4 = v_gazs != 0 #si gaz a l'arret pas bougé
    #==========================================================================
    #On combine les conditions
    cond = (cond1 | cond2 | cond3) & cond4
    # print(cond)
    # print((cond == False).all())
    #print(np.where(cond)[0])
    
    #Si aucun gaz est en contact on retourne 0
    if (cond == False).all() :
        return [part[1],0]
    #=========================================================================
    """#Ici on calcule si les forces sont positive >0 ou <0 en fonction de la 
    #direction de propagation des gazs et de la particule
    
    #Ici on détermine si la particule et le gaz on des vitesse opposé
    #Si oui alors on accelere la particule, si non alors on la décelere
    #décelere = F < 0
    
    si ils vont dans le meme sens = True 
    sens opposé = False
    
    si vpart = 0 on regarde pas trop : ca sera 1 ou -1 pas grave
    """
    signe_vitesse_part = (v_part > 0)
    signe_vitesse_gaz = (v_gazs[cond]>0)
    xor_signe = np.logical_not(signe_vitesse_part ^ signe_vitesse_gaz)
    
    if v_gazs[cond].size == 0:
        return [part[1],0]
    
    print(signe_vitesse_part,'signev part')
    print(signe_vitesse_gaz,"vitesse gaz")
    #print(v_gazs[cond],"vgaz")
    print(v_part,"signe vpart")
    print(xor_signe)
    # print(xor_signe)
    

    tempo = 1
    
    if signe_vitesse_part :
        tempo = 1
    else :
        tempo = -1
    
    f_gazs_temp = tempo * f_gazs[np.where(cond)[0]].copy() #seulement les gazs dans lesquels on est

    f_gazs_temp[(xor_signe)] = -1 * f_gazs_temp[(xor_signe)]
    
    
    #==========================================================================
    
    
    
    #Ici on somme les forces des boites qui appliquent leurs force

    force += np.sum(f_gazs_temp)
    
    dvdt = force
    dxdt = part[1]
    print(round(t*100/Tmax ,3),"%")
    print(force,"force")# les gazs bougent :)
    return [dxdt,dvdt]

#Acceleration

def accelerationpart(part,t,force) :
    dvdt = force
    dxdt = part[1]
    
    return [dxdt,dvdt]

def vitessegaz(x_gazs,t,v_gazs) :
    return v_gazs #la vitesse des gazs est constante et ne dép pas de la position


#=========================test==============================================
part = particule(np.random.uniform(0,L),vinit,0)
parti = [part.position,part.vitesse]
# print(parti,'pourt')
t = np.arange(0,Tmax, timeres)

# #Odeint
#print(x_gazs)
# print(v_gazs)
# 
#x_new = odeint(vitessegaz,x_gazs,t,args=(v_gazs,)).T #works allright for gazs
# print(x_new)

res = solve_ivp(forceing,(t[0],t[-1]),parti,method='RK45',t_eval = t, args=(x_gazs,v_gazs,f_gazs,L,D_gazs))
x = res["y"][0]
v =  res["y"][1]

x = res["y"][0] - np.floor(res["y"][0]/L) * L


plt.figure()
plt.plot(t,x , label = "position particule")
plt.ylim(0,L)
plt.title("Position en fonction du temps")

plt.figure()
plt.plot(t,v)
plt.title("Vitesse en fonction du temps")





# N_choc = len(x)
# #N_choc = 100



# x_evolution = np.array([])
# t_evolution = np.array([])
# v_evolution = np.array([])
# dt = 0.1 #pas de discrétisation en temps

# for i in range(0,N_choc -1 ) :
#     x_temp = np.arange(x[i] , x[i+1]  , v[i]*dt)
#     t_temp = np.arange(t[i] , t[i+1]   , dt)
#     v_temp = v[i]*np.ones(len(x_temp))
    
#     x_evolution = np.hstack((x_evolution , x_temp))
#     t_evolution = np.hstack((t_evolution , t_temp))    
#     v_evolution = np.hstack((v_evolution , v_temp))
# # Import animation package
# import matplotlib.animation as animation



# def update_vlines(*, h, x, ymin=None, ymax=None):
#     seg_old = h.get_segments()
#     if ymin is None:
#         ymin = seg_old[0][0, 1]
#     if ymax is None:
#         ymax = seg_old[0][1, 1]

#     seg_new = [np.array([[xx, ymin],
#                           [xx, ymax]]) for xx in x]

#     h.set_segments(seg_new)




# plt.Figure()
# fig, ax = plt.subplots()

# # ============================= Beautify ======================================
# ax.set_xlim([0, L])
# ax.set_ylim([-0.1,0.1])
# ax.title.set_text('Ping-pong de Fermi')
# ax.get_yaxis().set_visible(False)

# # ============================= Beautify ======================================

# scat = ax.scatter(x[0], 0)

# def animate(i):
#     scat.set_offsets((x_evolution[i], 0))
#     scat.set_label(f"x = {np.round(x_evolution[i],2)} , v={np.round(v_evolution[i],2)} ")
#     ax.legend(loc='upper left')
#     #return scat,

# ani = animation.FuncAnimation(fig, animate, repeat=True,
#                                     frames=len(x_evolution) - 1, interval=50)

# #writer = animation.PillowWriter(fps=15,\
# #                                metadata=dict(artist='Me'),\
# #                               bitrate=1800)
# ani.save('scatter.mp4')#, writer=writer)

# # """ Ca marche plutot bien, il reste plus qu'a optimiser l'ecriture puis faire magnétique"""

# """MTN IL FAUT ANIMER CHAQUE GAZS"""