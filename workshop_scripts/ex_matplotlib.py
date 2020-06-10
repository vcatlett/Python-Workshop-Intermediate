'''
Created by Victoria Catlett for the UTD REU Python Workshop
'''
###############################################################################
############# Import what you need from packages at the top ###################
###############################################################################

import numpy as np
import matplotlib.pyplot as plt


###############################################################################
########## Calculate y = 3x^2 +2x + 1 on 50 points between -10 and 10 #########
###############################################################################

my_x = np.linspace(-10, 10, 50)

def quadratic(x):
    y = 3*(x**2) + 2*x + 1
    return y

my_y = quadratic(my_x)
    
# Extra info: This next line does the same thing as lines 17-23 
#my_y = [3*x**2 for x in my_x]

###############################################################################
####### Use Matplotlib to plot the x and y values with green triangles ########
###############################################################################

plt.figure()
plt.plot(my_x, my_y, color='green', marker='v', linestyle='-', label='My Data')
plt.xlabel('x')
plt.ylabel(r'$y = x^{2}$')  # This uses LaTeX in the y label
plt.title('This is a plot!')
plt.legend()
plt.show()

# What happens when you use this instead of plt.plot?
#plt.scatter(my_x, my_y, color='green', marker='v', label='My Data')


###############################################################################
############### Save the figure as a PNG to the "files" folder ################
###############################################################################

plt.savefig('../files/Sample_Plot.png')