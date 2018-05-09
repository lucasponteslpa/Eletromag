import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.constants as scc
from scipy import integrate

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
    act = [a,a,0]
    pot = 0
    q = ro*(N*N)
    while act[1] > -a:
        act[0] = a
        while act[0] >= -a:
            #calcula o potencial de acordo com a distribuicao de carga proposta pelo problema
            if act[1] >= 0:
                pot = pot + potencial_disc(act,P,q)
            elif act[1] < 0:
                pot = pot + potencial_disc(act,P,-q)
            act[0] -= N
        act[1] -= N
    return pot
#inicializacao das variaveis de acordo com o problema
teta = [-np.pi/2]
N = 0.0001
P = [0.0,np.sin(teta[0]),np.cos(teta[0])]
a = 0.1
ro = 10**(-5)
res = []
while teta[len(teta)-1] <= np.pi/2:
    #coloca no vetor o potencial correspondente ao ponto P
    res.append(potencial_total(N,P,ro,a))
    #coloca no vetor o angulo da proxima iteracao para calcular o potencial
    teta.append(teta[len(teta)-1]+np.pi/20)
    #atualiza o proximo ponto a ser calculado o pontencial
    P = [0.0,np.sin(teta[len(teta)-1]),np.cos(teta[len(teta)-1])]
#plota resultados
fig, ax = plt.subplots()
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.array(teta[:len(teta)-1],dtype=float)
y = np.array(res,dtype=float) 
ax.plot(x,y, color='red')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()
