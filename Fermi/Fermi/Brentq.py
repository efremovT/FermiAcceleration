import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.optimize as opt


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
    
    
    prendre comme borne [tmin,pi/w*n] et si il n'existe pas de qolution
    chercher plus loin entre [pi/w*n ; pi/w*(n+1)]
    
    
    mas comment trouver n ? on va prendre l'entier naturelle juste au dessus
    de w*tmin/pi ou celui juste en dessous de x*tmin/pi +1"""
    
def Bornes(tmin,w):
    """ la fonction floor donne l'entier naturelle inférieure le plus proche"""
    ninf = np.floor( (w * tmin/np.pi) + 1)
    nsup = np.floor( (w * tmin/np.pi )+ 2) #voyons large
    
    borneinf = np.pi / w * ninf
    bornesup = np.pi / w * nsup
    
    # print(tmin,bornesup)
    return borneinf , bornesup

#=============================== On passe a la pratique ======================
def XMur (t,w,A,x0) :
    """ pos la position du mur et DemiPer la demi-periode d'oscillimport numpy as np
import matplotlib.pyplot as plt
import matplotlib as mplation"""
    
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



# =============================================================================
#        
#
#""" On le fais 1aller retour manuellment pour se donner une idée"""
#
#""" 1 - définition valeur initiale """
##Pour le murNewtonRaphson_Dicho
#x_equ_mur = 10
#A = 1
#w = 1
#
##Pour la balle
#x_balle = 1.0
#v = 1
#t = 0
#tavant=0
##precision pour trouver le contact
#eps = 0.01
#
#
#""" 2 - Bornes pour recherche 0 """
#
#tmin,tmax = TExtremum(t,v,x_equ_mur,A,x_balle)
#print("tmin,tmax",tmin,tmax) 
#borneinf,bornesup = Bornes(tmin,w)
#
#""" 3 - Temps de contact avec la raquette """
#
#t = recherche( Contact_raquette , ContactPrime_raquette,tmin,borneinf,bornesup,eps ,  t ,  v = v ,  w = w ,   A = A ,  x0_mur =x_equ_mur ,x0_balle = x_balle,t0=tavant )
#x_balle = XBalle(t,v,x_balle,tavant) 
#tavant=t
#
#""" 4 - actualisation des valeurs """
#v = -v + 2*Vmur(t,w,A,x_equ_mur)
#
#
#
#print("t0",t,"xmur0",XMur(t,w,A,x_equ_mur))
#print("t0",t,"Xballe0",x_balle)
#print("t0",t,"vballe0",v)
#
#
#
#""" 5 - la balle rebondit sur le mur de gauche """
#t = Contact_mur_immobile(t,v,x_balle,tavant)
#v = - v
#
#print("temps contact 1er rebond",Contact_mur_immobile(t,v,x_balle,tavant))
#print("1er rebond x",t,x_balle)
#print("1er rebond v",t,v)
#
#x_balle = 0 #car la position du mur de gauche est 0
#
#tavant=t
#tmin,tmax = TExtremum(t,v,x_equ_mur,A,x_balle)
#print("t1",tmin,tmax)
#print("t1","mur",XMur(t,w,A,x_equ_mur))
#print("t1",x_balle)
#print("t1",XMur(t,w,A,x_equ_mur)-x_balle)
#print("t1","raq",Contact_raquette(t,v,w,A,x_equ_mur,x_balle,tavant))
#
#t = NewtonRaphson_Dicho( Contact_raquette , ContactPrime_raquette,tmin,tmax,eps ,  t ,  v = v ,  w = w ,   A = A ,  x0_mur =x_equ_mur ,x0_balle = x_balle ,t0=tavant)
#x_balle = XBalle(t,v,x_balle,tavant) 
#tavant=t
#print("t1",t)
#""" puis on revient à l'étape 2 """

#=============================================================================

""" EVOLUTION AVEC GRAPHE
    
Pour un graphe du temps 0 à T on doit d'abord déterminer tout les temps de contact
tout les positions de la balle au temps de contact et tout les changement de vitesse
 """
""" On le fais 1aller retour manuellment pour se donner une idée"""

Tfin = 100 #si on veut le graphe sur t secondes d'évolution
t = 0



#Pour le mur
x_equ_mur = 3 #position moyenne du mur
A = 1          #Amplitude des oscillation
w = 0.5          #Fréquence

#Pour la balle
x_balle = 0  #Pos initiale balle Tout va bien
v = 1      #vitesse init balle Tout va bien
t = 0          #Temps initial (phase du mur) Pas bien
tavant=t


v_liste = [v]
t_liste = [t]
x_liste = [x_balle]

#precision pour trouver le contact
eps = 0.005


#for i in range(0,Té,1):
while(t<Tfin):       
    # contact avec le mur mouvant
    tmin,tmax = TExtremum(t,v,A,x_balle,x_equ_mur)
    borneinf,bornesup = Bornes(tmin,w)
    
    # print(Contact_raquette(tmin,v,w,A,x_equ_mur,x_balle,tavant))
    # print(Contact_raquette(bornesup,v,w,A,x_equ_mur,x_balle,tavant))


    t = opt.brentq(Contact_raquette,tmin,tmax,args=(v,w,A,x_equ_mur,x_balle,tavant)) #plus robuste
    
    x_balle = XBalle(t,v,x_balle,tavant)  
    v = -v + 2*Vmur(t,w,A,x_equ_mur)
    tavant=t

    
    t_liste.append(t)
    v_liste.append(v)
    x_liste.append(x_balle)
    # contact avec le mur immobile
    
    t = Contact_mur_immobile(t,v,x_balle,tavant)
    v = - v
    x_balle = 0 #car la position du mur de gauche est 0
    tavant=t
    t_liste.append(t)
    v_liste.append(v)
    x_liste.append(x_balle)
    
#========================== Graphe ===========================================
    
"""création d'un "super" Numpy array des postion et temps"""
N_choc = len(x_liste)
#N_choc = 100
print("nombre de choc :" ,N_choc)


x_evolution = np.array([])
t_evolution = np.array([])
v_evolution = np.array([])
dt = 0.1 #pas de discrétisation en temps

for i in range(0,N_choc -1 ) :
    x_temp = np.arange(x_liste[i] , x_liste [i+1]  , v_liste[i]*dt)
    t_temp = np.arange(t_liste[i] , t_liste[i+1]   , dt)
    v_temp = v_liste[i]*np.ones(len(x_temp))
    
    x_evolution = np.hstack((x_evolution , x_temp))
    t_evolution = np.hstack((t_evolution , t_temp))    
    v_evolution = np.hstack((v_evolution , v_temp))
# Import animation package
import matplotlib.animation as animation

def update_vlines(*, h, x, ymin=None, ymax=None):
    seg_old = h.get_segments()
    if ymin is None:
        ymin = seg_old[0][0, 1]
    if ymax is None:
        ymax = seg_old[0][1, 1]

    seg_new = [np.array([[xx, ymin],
                         [xx, ymax]]) for xx in x]

    h.set_segments(seg_new)




plt.Figure()
fig, ax = plt.subplots()

# ============================= Beautify ======================================
ax.set_xlim([0, x_equ_mur + A])
ax.set_ylim([-0.1,0.1])
ax.title.set_text('Ping-pong de Fermi')
ax.get_yaxis().set_visible(False)

# ============================= Beautify ======================================

scat = ax.scatter(x_evolution[0], 0,animated=True)
line = ax.axvline(x=XMur(t_evolution[0],w,A,x_equ_mur), ymin=-0.15, ymax=15,color='black',animated=True) 

def animate(i):
    scat.set_offsets((x_evolution[i], 0))
    scat.set_label(f"x = {np.round(x_evolution[i],2)} , v={np.round(v_evolution[i],2)} ")
    line.set_xdata((XMur(t_evolution[i],w,A,x_equ_mur)))
    ax.legend(loc='upper left')
    #return scat,

ani = animation.FuncAnimation(fig, animate, repeat=True,
                                    frames=len(x_evolution) - 1, interval=50)

#writer = animation.PillowWriter(fps=15,\
#                                metadata=dict(artist='Me'),\
#                               bitrate=1800)
ani.save('scatter.gif')#, writer=writer)

""" Ca marche plutot bien, il reste plus qu'a optimiser l'ecriture puis faire magnétique"""

plt.figure()
plt.plot(t_evolution,v_evolution)
plt.xlabel("t")
plt.ylabel("v(t)")
plt.title("Vitesse de la balle")
plt.savefig('Scatter.png')