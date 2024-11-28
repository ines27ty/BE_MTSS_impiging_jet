import numpy as np
import matplotlib.pyplot as plt
import os 


# Autre fichier : cv-uv
filename = "ij2lr-30-cw-uv.dat"

# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=3.0
# Expt. of Cooper et al. (1992)
#    y/D      -UV/(UBULK**2)

if os.path.exists(filename):
    with open(filename, 'r') as fichier:
        lines = fichier.readlines()
else:
    raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

# Initialiser des listes pour les positions et pressions
# position = R/D
# Nu_adim = Nu/(Re**0.7)
position_adim_uv = []
uv_admin = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_uv.append(float(values[0]))
    uv_admin.append(float(values[1]))

# Tracer Nu_adim en fonction de position_adim
plt.figure(1)
plt.plot(position_adim_uv, uv_admin, 'o-', label="expérimental")
plt.xlabel("Position adimensionnée")
plt.ylabel("vitesse uv adimensionné")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("30-cw-uv.png")

# Autre fichier
filename = "ij2lr-30-cw-vv.dat"

# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=3.0
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
vv_admin = []

# Parcourir chaque ligne du fichier
for line in lines:
    line = line.strip()  # Supprimer les espaces en début et fin de ligne
    line = line.replace('\t', ',')  # Remplacer les tabulations par des virgules
    values = line.split()  # Diviser la ligne en une liste de valeurs
    
    # Ajouter les valeurs à leurs listes respectives
    position_adim_vv.append(float(values[0]))
    vv_admin.append(float(values[1]))

plt.figure(2)
plt.plot(position_adim_vv, vv_admin, 'o-', label="expérimental")
plt.xlabel("Position adimensionnée")
plt.ylabel("vitesse vv adimensionné")
plt.title("Profil de vitesse adimensionné en fonction de la position adimensionnée")
plt.grid()
plt.savefig("30-cw-vv.png")


