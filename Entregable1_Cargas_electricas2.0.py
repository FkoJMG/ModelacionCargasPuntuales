import numpy as np
import matplotlib.pyplot as plt

plt.style.use("default")

def Angulo (X_,Y_,N_):
    alpha = []
    for fil in range(N_):
        alpha.append([])        
        for col in range (N_):
            if X_[fil][col] == 0:
                if Y_[fil][col] > 0:
                    alpha[fil].append(np.pi/2)
                else:
                    alpha[fil].append(-np.pi/2)
            elif X_[fil][col] < 0:
                alpha[fil].append(np.arctan(Y_[fil][col]/X_[fil][col])+np.pi)
            else:
                alpha[fil].append(np.arctan(Y_[fil][col]/X_[fil][col]))
    return alpha

def Color (carga):
    if carga > 0:
        color = 'red'
    else:
        color = 'black'
    return color

N = 9
gridMin = -2
gridMax = 2

x = np.linspace(gridMin,gridMax,N)
y = np.linspace(gridMin,gridMax,N)

X,Y = np.meshgrid(x,y)

eps_0 = 8.8542e-12
k_e = 1/(4*np.pi*eps_0)

cargas = int(input("¿Cuantas cargas? "))
Ex = 0
Ey = 0

q_s = []
q_locsX = []
q_locsY = []

for i in range (cargas):
    q = int(input("Magnitud de la carga: "))
    q_locX = int(input("Coordenada x: "))
    q_locY = int(input("Coordenada y: "))
    X_new = X-q_locX
    Y_new = Y-q_locY
    
    Alpha = Angulo(X_new, Y_new, N)
    r_2 = X_new**2+Y_new**2
    
    Ex1 = k_e*(q/r_2)*np.cos(Alpha)
    Ey1 = k_e*(q/r_2)*np.sin(Alpha)

    Ex += Ex1
    Ey += Ey1
    
    q_s.append(q)
    q_locsX.append(q_locX)
    q_locsY.append(q_locY)

mags = np.sqrt(Ex**2+Ey**2)

Ex_unit = Ex/mags
Ey_unit = Ey/mags

fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,Ex_unit,Ey_unit)
for i in range (cargas):
    ax.scatter(q_locsX[i],q_locsY[i],c=Color(q_s[i]),s=1000)
ax.axis([gridMin, gridMax,gridMin,gridMax])
ax.set_aspect('equal','box')
plt.show()
