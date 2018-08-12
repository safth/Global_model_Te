# global model Principles of Plasma Discharges and Materials Processing
# Lieberman p.333
# calculate the electron temperature from charge particle conservation at low
# presure <1Torr. This model consider that charge particle are cerated by direct Sigma_Ar_ionization
# on the ground state and loss by difffusion to the wall with an effective diffusion length.

import numpy as np
import matplotlib.pyplot as plt
from rate_calc import rate_calc

# input value
p_temp = np.linspace(5,80,100); #mtorr,range of pression you want to know Te
Te = np.linspace(0.5,10,1000); #Max and min value of possible Te
R = 0.080; # Radius of the plasma (reactor)
L = 0.20;  # length of the plasma (reactor)
#========================================================================
#========================================================================

#constant
mi = 6.63e-26; # Argon mass (Kg)
e  = 1.6e-19;  # electron charge
k  = 1.38e-23; # Boltzmann constant


# first we calculate the reaction rate for ionization
k_iz=[]
for iTe in Te:
    # cross section from Lxcat. you can change it...
    # it takes Te, filename, exposant =1 for maxwellian distribution.
    # (this can calculate a reaction rate with a generalized EEDF)
    k_iz.append(rate_calc(iTe,'Sigma_Ar_ionization.txt',1))


# according to Lieberman.


# some placeholders.
p=[]
n=[]
lambda_i=[]
h_R = []
h_L = []
d_eff = []
y = []
v_B = np.sqrt(e*Te/mi); # Bohm velocity
#loop on the pressure
for j in range(len(p_temp)):
    p.append((133.3224e-3)*p_temp[j]) # pressure : mtorr to pascal
    n.append(p[j]/(k*300)) #number density in m^-3
    #ion mean free path
    lambda_i.append( 1/(n[j]*1e-18) ) #1e-18 cross section from lieberman
    #parameters from lieberman to calculate d_eff, the effective size of the plasma
    h_R.append(0.8*(4+R/lambda_i[j]**(-1/2)))
    h_L.append(0.86*(3+L/(2*lambda_i[j])**(-1/2)))

    d_eff.append(((1/2)*R*L) / (R*h_L[j] + L*h_R[j]))
    x = [] #placeholder
    #for a given Pressure, calculate at wich Te the transandendal equation is satisfied
    for i in range(len(Te)):
        x.append(n[j]*d_eff[j]*(k_iz[i]/v_B[i]))
        if x[i] > 1:
            y.append(Te[i])
            break
plt.plot(p_temp,y)
plt.show()
