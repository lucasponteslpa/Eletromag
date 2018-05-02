import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.constants as scc
from scipy import integrate

def potencial_disc(r,P,q):
    R = np.sqrt((P[0]-r[0])**2 +(P[1]-r[1])**2 + (P[2]-r[2])**2)
    return (1/(4*np.pi*scc.epsilon_0))*(q/R)

def potencial_total(N,P,ro,a):
    act = [a,a,0]
    pot = 0
    q = ro*(N*N)
    while act[1] > -a:
        act[0] = a
        while act[0] >= -a:
           pot = pot + potencial_disc(act,P,q)
           act[0] -= N
        act[1] -= N
    return pot
# plot(x, y, color='green', linestyle='dashed', marker='o',
#                      markerfacecolor='blue', markersize=12).
teta = [-np.pi/2]
N = 0.001
P = [0.0,np.cos(teta[0]),np.sin(teta[0])]
a = 0.1
ro = 10**(-5)
res = []
while teta[len(teta)-1] <= np.pi/2:
    res.append(potencial_total(N,P,ro,a))
    teta.append(teta[len(teta)-1]+np.pi/10)
    P = [0.0,np.cos(teta[len(teta)-1]),np.sin(teta[len(teta)-1])]

fig, ax = plt.subplots()
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.array(teta[:len(teta)-1],dtype=float)
y = np.array(res,dtype=float) 
ax.plot(x,y, 'o')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
