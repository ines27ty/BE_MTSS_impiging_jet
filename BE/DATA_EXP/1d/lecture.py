import numpy as np
import os

def lecture_files(filename, coeff_1, coeff_2):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

    x = []
    y = []

    with open(filename, 'r') as fichier:
        lines = fichier.readlines()

    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        if not line:  # Skip empty lines
            continue

        # Split the line into values
        values = line.split()
        if len(values) < 2:  # Ensure at least two values are present
            raise ValueError(f"Ligne invalide : {line}")
        
        try:
            x_value = float(values[0])
            y_value = float(values[1])
        except ValueError:
            raise ValueError(f"Valeurs non numériques détectées dans la ligne : {line}")

        x.append(x_value)
        y.append(y_value)

    # Convert to numpy arrays and apply coefficients
    x = np.array(x)
    y = np.array(y)
    x_dim = x * coeff_1
    y_dim = y * coeff_2

    return x, y, x_dim, y_dim

def lecture_simu(filename, a_x, b_x, a_y, b_y) :
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas.")

    x = []
    y = []

    with open(filename, 'r') as fichier:
        lines = fichier.readlines()

    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces
        if not line:  # Skip empty lines
            continue

        # Split the line into values
        values = line.split()
        if len(values) < 2:  # Ensure at least two values are present
            raise ValueError(f"Ligne invalide : {line}")
        
        try:
            x_value = float(values[0])
            y_value = float(values[1])
        except ValueError:
            raise ValueError(f"Valeurs non numériques détectées dans la ligne : {line}")

        x.append(x_value)
        y.append(y_value)

    # Convert to numpy arrays and apply coefficients
    x = np.array(x)+a_x
    y = np.array(y)
    
    x_adim = (x)*b_x 
    y_adim = (y)*b_y

    return x, y, x_adim, y_adim

