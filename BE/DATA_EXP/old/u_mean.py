import numpy as np
import matplotlib.pyplot as plt
import os 
from interpolation import interpolate_files

u_bulk = 13 # m/s
D = 0.026 # m
Re = 23000
filename = "u_mean_change.xy"

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

position = []
u_mean = []
position_u = []
u_mean_u = []   

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    values = line.split('\t')  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position.append(float(values[0]))
    u_mean.append(float(values[1]))

position_u = [(position[i]+0.208)/D for i in range(len(position))]
u_mean_u = [u_mean[i]/(u_bulk) for i in range(len(u_mean))]

######################### mu ##############################
# Autre fichier mu
filename = "ij2lr-10-sw-mu.dat"

# Impinging Jet: H/D=2, Re=23000
# Single wire data at R/D=1.0
# Expt. of Cooper et al. (1992)
#    y/D          U/UBULK

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

# Initialiser des listes pour les positions et pressions
# position = R/D
# Nu_adim = Nu/(Re**0.7)
position_adim_mu = []
mu_adim= []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_mu.append(float(values[0]))
    mu_adim.append(float(values[1]))

plt.figure(1)
plt.plot(position_u, u_mean_u,'o', label="simulation")
plt.plot(position_adim_mu, mu_adim, 'o-', label="expérimental")
plt.xlabel("Position  y")
plt.ylabel("vitesse U")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("u_mean.png")
plt.legend()
plt.show()
