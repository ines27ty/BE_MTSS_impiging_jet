import numpy as np
import matplotlib.pyplot as plt
import os 
from interpolation import interpolate_files

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

# Initialiser des listes pour les positions et pressions
# position = R/D
# Nu_adim = Nu/(Re**0.7)
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


# Autre fichier
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

# Initialiser des listes pour les positions et pressions
# position = R/D
# Nu_adim = Nu/(Re**0.7)
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
u_ubulk_adim = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_mu.append(float(values[0]))
    u_ubulk_adim.append(float(values[1]))

# Autre fichier uu
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
# position = R/D
# Nu_adim = Nu/(Re**0.7)
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



# Tracer uv en fonction de position_adim
plt.figure(2)
plt.plot(position_adim_uv, uv_adim, 'o-', label="expérimental")
plt.xlabel("Position y/D ")
plt.ylabel("vitesse uv -uv/(UBULK**2)")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("10-cw-uv.png")


plt.figure(3)
plt.plot(position_adim_mu, u_ubulk_adim, 'o-', label="expérimental")
plt.xlabel("Position  y/D")
plt.ylabel("vitesse U/UBULK")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("10-sw-mu.png")


plt.figure(4)
plt.plot(position_adim_vv, vv_adim, 'o-', label="expérimental")
plt.xlabel("Position y/D ")
plt.ylabel("vitesse vv/(UBULK**2)")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("10-cw-vv.png")

plt.figure(5)
plt.plot(position_adim_uu, uu_adim, 'o-', label="expérimental")
plt.xlabel("Position y/D")
plt.ylabel("vitesse uu/(UBULK**2)")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("10-sw-uu.png")

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
for i in range(len(uu_interp)):
    epsilone.append(0.5*u_bulk**2*(uu_interp[i] + vv_interp[i]))

position_eps = [x_common[i] for i in range(len(x_common))]
plt.figure(6)
plt.plot(position_eps, epsilone, 'o-', label="expérimental")
plt.xlabel("Position y/D")
plt.ylabel("epsilone")
plt.grid()
plt.savefig("10-epsilone.png")
plt.show()
