import math
import numpy as np

def rate_calc(Te, file, exposant):
    with open(file) as f:
        w, h = [float(x) for x in next(f).split()] # read first line
        data = []
        for line in f: # read rest of lines
            data.append([float(x) for x in line.split()])
    data = np.array(data) #Energy is 1st column andCross section is 2nd column

    e = 1.602176462*10**(-19)
    me=9.10938188*10**(-31)             #Mass of electron

    B1=exposant*(2./3.)**(3./2.)*(math.gamma(5./(2.*exposant)))**(3./2.)/(math.gamma(3./(2.*exposant)))**(5./2.)
    B2=(2./3.)*math.gamma(5./(2.*exposant))/math.gamma(3./(2.*exposant))
    int = []
    for E,sec in data:
        int.append(sec*E*B1*Te**(-3./2.)*np.exp(-(B2*E/Te)**exposant))

    result = (np.sqrt(2.*e/me))*(np.trapz(np.array(int),data[:,0]));
    return result
