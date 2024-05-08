import numpy as np
import matplotlib.pyplot as plt

#Températures (K)
T1= 54.361
T2= 43.772
T3= 23.781

#delta H (kJ/mol)
dH1=0.445
dH2=0.743
dH3=0.094

#constante des gaz parfaits (J/mol/K)
R=8.314

def A(T):
    return 334527*np.exp(-0.234*T)

def solubilite(listeT):
    liste=[]
    for T in listeT:
        etape=0
        if T2<=T<=T1:
            etape=(dH1/R*T1)*(1-T1/T)
        if T3<=T<T2:
            etape=(dH1/R*T1)*(1-T1/T) + (dH2/R*T2)*(1-T2/T)
        if T<=T3:   
            etape= (dH1/R*T1)*(1-T1/T) + (dH2/R*T2)*(1-T2/T) + (dH3/R*T3)*(1-T3/T)
        resultat=np.exp(etape)*1/A(T)  
        liste.append(resultat)
    return liste

T=np.linspace(15,54,100)
plt.plot(T,solubilite(T))
plt.plot(T, 1/A(T))
plt.legend(["Solubilité","1/A"])
plt.xlabel("Température (K)")
plt.ylabel("Solubilité (mol/L)")
plt.title("Solubilité en fonction de la température")
plt.show()