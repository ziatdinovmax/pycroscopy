# Oak Ridge National Lab
# Center for Nanophase Materials Sciences
# written by Alvin Tan on 08/15/2019
# in collaboration with Rama Vasudevan, Liam Collins, and Kody Law

# This program reads in simulated input via csv files, then runs Bayesian inference
# on said input to confirm that our processes are functional.

import numpy as np
from kpfm_bayesian_utils import get_default_parameters, BayesianInference, processResults

R_H = np.genfromtxt('C:/Users/Administrator/Dropbox/polynomial approximation paper/Analysis Codes/Paper Codes/InputsAndOutputs2/R_H-1.csv', delimiter=',')
wd = int(np.genfromtxt('C:/Users/Administrator/Dropbox/polynomial approximation paper/Analysis Codes/Paper Codes/InputsAndOutputs2/wd-1.csv', delimiter=','))
n0 = int(np.genfromtxt('C:/Users/Administrator/Dropbox/polynomial approximation paper/Analysis Codes/Paper Codes/InputsAndOutputs2/n0-1.csv', delimiter=','))
p = get_default_parameters()

#breakpoint() # To confirm inputs have been successfully imported

y, tt, pp1, sig, gam, AA, B, BB, CC, C0, P0, CC1, GAI, M, m0, phi, m_phi, Sig = BayesianInference(R_H, wd, n0, p);

#breakpoint() # To confirm outputs are successfully calculated

# Unfortunately, outputs are not consistent with that generated by Matlab, but I am kinda tired atm haha, so I'm moving on

Rforce = np.genfromtxt('C:/Users/Administrator/Dropbox/polynomial approximation paper/Analysis Codes/Paper Codes/InputsAndOutputs2/Rforce-1.csv', delimiter=',')

# Graphing our stuff
graphBois = processResults(p, R_H, wd, Rforce, M, Sig, B, m_phi, y, CC, graph=True, verbose=False)

# Save the images
graphBois[0].savefig("3Dplot.png")
graphBois[1].savefig("OtherPlots.png")








'''
 % Saves inputs as csv files to use in the Python code
csvwrite(sprintf('InputsAndOutputs/R_H-%d.csv', k1),R_H)
csvwrite(sprintf('InputsAndOutputs/wd-%d.csv', k1),wd)
csvwrite(sprintf('InputsAndOutputs/n0-%d.csv', k1),n0)
%csvwrite(sprintf('InputsAndOutputs/p-%d.csv', k1),p) % p is just default stuff, I think, so
%we don't need to save it...

[y tt pp1 sig gam AA B BB CC C0 P0 CC1 GAI M m0 phi m_phi Sig]=BayesInfer(R_H,wd,n0,p);

% Saves outputs as csv files to compare to output of Python code
csvwrite(sprintf('InputsAndOutputs/y-%d.csv', k1),y)
csvwrite(sprintf('InputsAndOutputs/tt-%d.csv', k1),tt)
csvwrite(sprintf('InputsAndOutputs/pp1-%d.csv', k1),pp1)
csvwrite(sprintf('InputsAndOutputs/sig-%d.csv', k1),sig)
csvwrite(sprintf('InputsAndOutputs/gam-%d.csv', k1),gam)
csvwrite(sprintf('InputsAndOutputs/AA-%d.csv', k1),AA)
csvwrite(sprintf('InputsAndOutputs/B-%d.csv', k1),B)
csvwrite(sprintf('InputsAndOutputs/BB-%d.csv', k1),BB)
csvwrite(sprintf('InputsAndOutputs/CC-%d.csv', k1),CC)
csvwrite(sprintf('InputsAndOutputs/C0-%d.csv', k1),C0)
csvwrite(sprintf('InputsAndOutputs/P0-%d.csv', k1),P0)
csvwrite(sprintf('InputsAndOutputs/CC1-%d.csv', k1),CC1)
csvwrite(sprintf('InputsAndOutputs/GAI-%d.csv', k1),GAI)
csvwrite(sprintf('InputsAndOutputs/M-%d.csv', k1),M)
csvwrite(sprintf('InputsAndOutputs/m0-%d.csv', k1),m0)
csvwrite(sprintf('InputsAndOutputs/phi-%d.csv', k1),phi)
csvwrite(sprintf('InputsAndOutputs/m_phi-%d.csv', k1),m_phi)
csvwrite(sprintf('InputsAndOutputs/Sig-%d.csv', k1),Sig)
'''