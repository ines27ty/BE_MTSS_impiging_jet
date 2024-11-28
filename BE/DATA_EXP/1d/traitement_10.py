import numpy as np
import matplotlib.pyplot as plt
import os 
from lecture import lecture_files
from lecture import lecture_simu
from interpolation import interpolate_files

u_bulk = 13 # m/s
D = 0.026 # m
Re = 23000

####################### mu : u mean #######################################
# Données expérimentales
position_mu_adim, u_mean_adim, position_mu_dim , u_mean_dim = lecture_files('ij2lr-10-sw-mu.dat', D, u_bulk)

# Impinging Jet: H/D=2, Re=23000
# Single wire data at R/D=1.0
# Expt. of Cooper et al. (1992)
#    y/D          U/UBULK


# Données numériques

position_mu_fluent_dim, u_mean_fluent_dim, position_mu_fluent_adim , u_mean_fluent_adim = lecture_simu('umean_r_1.xy', 0.208, 1/D, 0, 1/u_bulk)


plt.figure(2)
plt.plot(position_mu_adim, u_mean_adim, 'o-', label="expérimental")
plt.plot(position_mu_fluent_adim, u_mean_fluent_adim, '*', label="numérique")
plt.xlabel("Position y/D")
plt.ylabel("vitesse u/UBULK")
plt.title("Profil de vitesse adimensionnalisé en fonction de la position")
plt.savefig("10-u_mean_adim.png")
plt.legend()
plt.grid()

plt.figure(3)
plt.plot(position_mu_dim, u_mean_dim, 'o-', label="expérimental")
plt.plot(position_mu_fluent_dim, u_mean_fluent_dim, '*', label="numérique")
plt.xlabel("Position y")
plt.ylabel("vitesse u")
plt.title("Profil de vitesse dimensionalisé en fonction de la position adimensionnée")
plt.savefig("10-u_mean_dim.png")
plt.legend()
plt.grid()

####################### uu  #######################################
position_uu_adim, uu_adim, position_uu_dim , uu_dim = lecture_files('ij2lr-10-sw-uu.dat', D, u_bulk**2)


# Impinging Jet: H/D=2, Re=23000
# Single wire data at R/D=1.0
# Expt. of Cooper et al. (1992)
#    y/D         uu/(UBULK**2)

plt.figure(4)
plt.plot(position_uu_adim, uu_adim, 'o-', label="expérimental")
plt.xlabel("Position y/D")
plt.ylabel("vitesse uu/UBULK**2")
plt.title("Profil de vitesse adimensionnalisé en fonction de la position")
plt.savefig("10-u_mean_adim.png")
plt.grid()

plt.figure(5)
plt.plot(position_uu_dim, uu_dim, 'o-', label="expérimental")
plt.xlabel("Position y")
plt.ylabel("vitesse uu")
plt.title("Profil de vitesse dimensionalisé en fonction de la position adimensionnée")
plt.savefig("10-u_mean_dim.png")
plt.grid()

####################### vv  #######################################
position_vv_adim, vv_adim, position_vv_dim , vv_dim = lecture_files('ij2lr-10-cw-vv.dat', D, u_bulk**2)

# Impinging Jet: H/D=2, Re=23000
# Cross wire data at R/D=1.0
# Expt. of Cooper et al. (1992)
#    y/D      vv/(UBULK**2)

plt.figure(6)
plt.plot(position_vv_adim, vv_adim, 'o-', label="expérimental")
plt.xlabel("Position y/D")
plt.ylabel("vitesse vv/UBULK**2")
plt.title("Profil de vitesse adimensionnalisé en fonction de la position")
plt.savefig("10-vv_adim.png")
plt.grid()

plt.figure(7)
plt.plot(position_vv_dim, vv_dim, 'o-', label="expérimental")
plt.xlabel("Position y")
plt.ylabel("vitesse vv")
plt.title("Profil de vitesse dimensionalisé en fonction de la position adimensionnée")
plt.savefig("10-vv_dim.png")
plt.grid()


# Tracer l'énergie cinétique turbulente à partir de uu et vv
#   Interpolation des fichiers uu et vv

file1 = 'ij2lr-10-sw-uu.dat'
file2 = 'ij2lr-10-cw-vv.dat'
output = 'interpolated_result.csv'

position_inter_adim, uu_inter_adim, vv_inter_adim = interpolate_files(file1, file2, output, num_points=1000)
uu_inter_dim = [(uu_inter_adim[i]*u_bulk**2) for i in range(len(uu_inter_adim))]
vv_inter_dim = [(vv_inter_adim[i]*u_bulk**2) for i in range(len(vv_inter_adim))]
position_inter_dim = [(position_inter_adim[i]*D) for i in range(len(position_inter_adim))]

# Calcul d'epsilone
epsilone_dim = []
epsilone_adim = []
k_dim = []
k_adim = [] 

for i in range(len(uu_inter_dim)):
    epsilone_dim.append(0.5*(uu_inter_dim[i] + vv_inter_dim[i]))
    epsilone_adim.append(0.5*(uu_inter_adim[i] + vv_inter_adim[i]))
    k_dim.append(0.5*np.sqrt(uu_inter_dim[i]**2 + vv_inter_dim[i]**2))
    k_adim.append(0.5*np.sqrt(uu_inter_adim[i]**2 + vv_inter_adim[i]**2))

plt.figure(8)
plt.plot(position_inter_dim, epsilone_dim, 'o-', label="expérimental")
plt.xlabel("Position y")
plt.ylabel("epsilone dimensionné")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente en fonction de la position")
plt.savefig("10-epsilone_dim.png")

plt.figure(9)
plt.plot(position_inter_adim, epsilone_adim, 'o-', label="expérimental")
plt.xlabel("Position y/D")
plt.ylabel("epsilone adimensionné")
plt.grid()
plt.title("Profil d'énergie cinétique turbulente adimensionné en fonction de la position")
plt.savefig("10-epsilone_adim.png")

plt.show()


