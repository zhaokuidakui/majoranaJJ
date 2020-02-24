import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import matplotlib.lines as mlines
from scipy import interpolate

import majoranas.modules.constants as const
import majoranas.modules.lattice as lat
import majoranas.modules.operators as op

ax = 2      #unit cell size along x-direction in [A]
ay = 2      #unit cell size along y-direction in [A]
Ny = 25     #number of lattice sites in y direction
Nx = 25     #number of lattice sites in x direction
N = Ny*Nx   #Total number of lattice sites
print(N)

x1 = 10
x2 = 10
y1 = 10
y2 = 10

coor = lat.cross(x1, x2, y1, y2)
NN = lat.NN_Arr(coor)

H = op.H0(coor, ax, ay)
energy, states = LA.eigh(H)

#Ibeam Eigenvalues
print(energy.shape)
print(energy[0:10]/energy[0])

op.state_cplot(coor, states[:, 3])