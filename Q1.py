import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.constants as scc
from scipy import integrate

#funcao utilizada para realizar a integral do modulo scipy
def f(x,y):
    return (1/np.sqrt(1+x**2+y**2))

#funcao que calcula potecial discreto de um elemento de area em relacao a um ponto
# R = distancia entre o elemento de area e o ponto
# P = vetor que indica o ponto a ser medido o pontencial
# r = ponto do elemento de area

def potencial_disc(r,P,q):
    R = np.sqrt((P[0]-r[0])**2 +(P[1]-r[1])**2 + (P[2]-r[2])**2)
    return (1/(4*np.pi*scc.epsilon_0))*(q/R)

#calcula o pontencial da area referente a um ponto P, sendo dividido em elementos de area com lados N
#ro = densidade de carga superficial
# 2*a = lado do quadrado equivalente a area total

def potencial_total(N,P,ro,a):
    #act = elemento de area atual a ser medido o pontencial no ponto P
    act = [a,a,0]
    #pot = soma de todos os pontenciais referentes ao elemento de area
    pot = 0
    #q = carga por elemento de area
    q = ro*(N*N)
    while act[1] > -a:
        act[0] = a
        while act[0] >= -a:
           pot = pot + potencial_disc(act,P,q)
           #anda na coordenada x do espaco
           act[0] -= N
        #anda na coordenada y do espaco
        act[1] -= N
    return pot
#inicializacao das variaveis de acordo com o problema
N = 0.1
P = [0.0,0.0,1.0]
a = 0.1
ro = 10**(-5)
res = [0.0,0.0,0.0,0.0]
fig, ax = plt.subplots()
#resultado analitico realizado pelo scipy
matplotlib.rcParams['axes.unicode_minus'] = False
res_analitc = integrate.nquad(f,[[-0.1,0.1],[-0.1,0.1]]) 
res[0] = ro*1/(4*np.pi*scc.epsilon_0)*res_analitc[0]
print res[0]
#resultado para N = 0.1
res[3] = potencial_total(N,P,ro,a)
print res[3]

#resultado para N = 0.05
N2 = 0.05
res[2] = potencial_total(N2,P,ro,a)
print res[2]
#resultado para N = 0.0001
N3 = 0.0001
res[1] = potencial_total(N3,P,ro,a)
print res[1]
#plotando pontos
x = np.array([0.0,N3,N2,N],dtype=float)
y = np.array(res,dtype=float) 
ax.plot(x,y, 'o')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
