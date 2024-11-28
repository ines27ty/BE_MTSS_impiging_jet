import numpy as np
import matplotlib.pyplot as plt
import os 
from interpolation import interpolate_files

u_bulk = 13 # m/s
D = 0.026 # m
Re = 23000

####################### uv #######################################
#cw-uv
filename = "ij2lr-10-cw-uv.dat"

# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=1.0
# Expt. of Cooper et al. (1992)
#    y/D      -uv/(UBULK**2)

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

position_adim_uv = []
uv_adim = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_uv.append(float(values[0]))
    uv_adim.append(float(values[1]))

position_uu = [position_adim_uv[i]*D for i in range(len(position_adim_uv))]
uv = [uv_adim[i]*u_bulk**2 for i in range(len(uv_adim))]

# Tracer uv en fonction de position_adim
plt.figure(2)
plt.plot(position_uu, uv, 'o-', label="expérimental")
plt.xlabel("Position y ")
plt.ylabel("vitesse uv")
plt.title("Profil de vitesse en fonction de la position")
plt.grid()
plt.savefig("10-cw-uv_dim.png")

##################### vv ########""###############
#cw-vv
filename = "ij2lr-10-cw-vv.dat"

# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=1.0
# Expt. of Cooper et al. (1992)
#    y/D      vv/(UBULK**2)

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

position_adim_vv = []
vv_adim = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_vv.append(float(values[0]))
    vv_adim.append(float(values[1]))

position_vv = [position_adim_vv[i]*D for i in range(len(position_adim_vv))]
vv = [vv_adim[i]*u_bulk**2 for i in range(len(vv_adim))]

plt.figure(4)
plt.plot(position_vv, vv, 'o-', label="expérimental")
plt.xlabel("Position y ")
plt.ylabel("vitesse vv")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("10-cw-vv_dim.png")


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

position_mu = [position_adim_mu[i]*D for i in range(len(position_adim_mu))]
mu = [mu_adim[i]*u_bulk for i in range(len(mu_adim))]

plt.figure(3)
plt.plot(position_mu, mu, 'o-', label="expérimental")
plt.xlabel("Position  y")
plt.ylabel("vitesse U")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("10-sw-mu_dim.png")


######################### uu ##############################
filename = "ij2lr-10-sw-uu.dat"

# Impinging Jet: H/D=2, Re=23000
# Single wire data at R/D=1.0
# Expt. of Cooper et al. (1992)
#    y/D         uu/(UBULK**2)

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

# Initialiser des listes pour les positions et pressions
position_adim_uu = []
uu_adim = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_uu.append(float(values[0]))
    uu_adim.append(float(values[1]))

position_uu = [position_adim_uu[i]*D for i in range(len(position_adim_uu))]
uu = [uu_adim[i]*u_bulk**2 for i in range(len(uu_adim))]


plt.figure(5)
plt.plot(position_uu, uu, 'o-', label="expérimental")
plt.xlabel("Position y")
plt.ylabel("vitesse uu")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("10-sw-uu_dim.png")


## Calcul de l'énérgie cinétique turbulente

#   Interpolation des fichiers uu et vv

file1 = 'ij2lr-10-sw-uu.dat'
file2 = 'ij2lr-10-cw-vv.dat'
output = 'interpolated_result.csv'

x_common, uu_interp, vv_interp = interpolate_files(file1, file2, output, num_points=1000)

# Adimensionnement
u_bulk = 13 # m/s
Re = 23000  
D= 0.026    # m

# Calcul d'epsilone
epsilone = []
k = []
for i in range(len(uu_interp)):
    epsilone.append(0.5*u_bulk**2*(uu_interp[i] + vv_interp[i]))
    k.append(0.5*np.sqrt((uu_interp[i]*(u_bulk**2))**2 + (vv_interp[i]*(u_bulk**2))**2))
    position_eps = x_common*D

plt.figure(6)
plt.plot(position_eps, epsilone, 'o-', label="expérimental")
plt.xlabel("Position ")
plt.ylabel("epsilone")
plt.grid()
plt.savefig("10-epsilone_ubulk.png")

plt.figure(7)
plt.plot(position_eps, k, 'o-', label="expérimental")
plt.xlabel("Position y")
plt.ylabel("k")
plt.grid()
plt.savefig("10-k_ubulk.png")



