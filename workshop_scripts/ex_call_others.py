'''
Created by Victoria Catlett for the Intermediate Python 3 Workshop
'''
###############################################################################
##### Import the script like a package. It must be in the same directory. #####
###############################################################################

import call_this_script

###############################################################################
##### Now call the function inside of call_me, which takes a numeric input ####
###############################################################################

y = call_this_script.call_this_function(3.14)
print('y = %.2f' %y)