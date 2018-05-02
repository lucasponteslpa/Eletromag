import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.constants as scc
from scipy import integrate

def f(x,y):
    return (1/np.sqrt(1+x**2+y**2))

def bounds():
    return [-0.2,0.2]

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
N = 0.1
P = [0.0,0.0,1.0]
a = 0.1
ro = 10**(-5)
res = [0.0,0.0,0.0,0.0]
fig, ax = plt.subplots()
matplotlib.rcParams['axes.unicode_minus'] = False
res_analitc = integrate.nquad(f,[[-0.1,0.1],[-0.1,0.1]]) 
res[0] = res_analitc[0]
res[3] = potencial_total(N,P,ro,a)


N2 = 0.05
res[2] = potencial_total(N2,P,ro,a)


N3 = 0.0001
res[1] = potencial_total(N3,P,ro,a)
x = np.array([0.0,N3,N2,N],dtype=float)
y = np.array(res,dtype=float) 
ax.plot(x,y, 'o')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
