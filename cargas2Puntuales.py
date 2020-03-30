import numpy as np
import matplotlib.pyplot as plt

plt.style.use("default")

def Angulo (X_,Y_,N_):
    alpha = []
    for i in range (N_):
        alpha.append([])
    for fil in range (N_):
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

def Color(carga):
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

q = -2e-6
q_loc = [1,-1]
q2 = -2e-6
q2_loc = [-1,1]

X_new = X-q_loc[0]
Y_new = Y-q_loc[1]
X_new2 = X-q2_loc[0]
Y_new2 = Y-q2_loc[1]

alpha = Angulo(X_new,Y_new,N)
r = X_new**2+Y_new**2
alpha2 = Angulo(X_new2,Y_new2,N)
r2 = X_new2**2+Y_new2**2

Ex1 = k_e*(q/r)*np.cos(alpha)
Ey1 = k_e*(q/r)*np.sin(alpha)
Ex2 = k_e*(q2/r2)*np.cos(alpha2)
Ey2 = k_e*(q2/r2)*np.sin(alpha2)

Ex = Ex1 + Ex2
Ey = Ey1 + Ey2

mags = np.sqrt(Ex**2+Ey**2)

Ex_unit = Ex/mags
Ey_unit = Ey/mags

fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(X,Y,Ex_unit,Ey_unit)
ax.scatter(q_loc[0],q_loc[1],c=Color(q),s=1000)
ax.scatter(q2_loc[0],q2_loc[1],c=Color(q2),s=1000)
ax.axis([-2,2,-2,2])
ax.set_aspect('equal','box')

plt.show() 
