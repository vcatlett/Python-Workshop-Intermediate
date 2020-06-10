'''
Created by Victoria Catlett for the UTD REU Python Workshop
'''
###############################################################################
############# Import what you need from packages at the top ###################
###############################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d.axes3d import Axes3D


###############################################################################
################## Create a Bivariate Gaussian function #######################
###############################################################################

def bivarGauss (x):
    z = multivariate_normal.pdf(x, mean=[0,0], cov=[[1,0],[0,1]])
    return z


###############################################################################
########### Create an X-Y grid and evaluate bivarGauss on the grid ############
###############################################################################

mx = np.linspace(-5, 5, 100)
my = np.linspace(-5, 5, 100)
mX, mY = np.meshgrid(mx, my)
mz = bivarGauss(np.stack((mX, mY), axis =2))


###############################################################################
######## Plot the Bivariate Gaussian and project it onto the X-Y plane ########
###############################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(mX, mY, mz, rstride=3, cstride=3, linewidth=1, antialiased=False, cmap=cm.coolwarm)
ax.contourf(mX, mY, mz, zdir='z', offset=-0.1, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-5, 5)
ax.set_ylabel('Y')
ax.set_ylim(-5, 5)
ax.set_zlabel('Z')
ax.set_zlim(-0.1, 0.2)
plt.title(r'Bivariate Gaussian, $\mu = (0,0)$')

plt.show()

###############################################################################
################## Plot ONLY the projection on the X-Y plane ##################
###############################################################################

plt.figure()
plt.contourf(mx, my, mz)
plt.xlabel('X')
plt.ylabel('y')
plt.title(r'Contours of a Bivariate Gaussian, $\mu = (0,0)$')
plt.colorbar()
plt.show()