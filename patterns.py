"""

patterns

Fluvio L. Lobo Fenoglietto
05/03/2019

"""

# ============================================ #
# Libraries and Modules
# ============================================ #
import numpy as np
import matplotlib.pyplot as plt


# ============================================ #
# Functions
# ============================================ #


def random( x_dim, y_dim ):
    '''
    random pattern

        This function generates a binary, random pattern or texture

        Fluvio L. Lobo Fenoglietto
        05/03/2019
    '''

    pattern = np.random.randint(2, size=(y_dim,x_dim))
    plt.imshow(pattern, cmap=plt.cm.gray)
    plt.show()

    return pattern

# -------------------------------------------- #

def walk( x_dim, y_dim ):
    '''
    random pattern

        This function generates a binary, random pattern or texture

        Fluvio L. Lobo Fenoglietto
        05/03/2019
    '''

    #pattern = np.random.randint(2, size=(y_dim,x_dim))
    pattern = np.zeros(size=(y_dim,x_dim))
    plt.imshow(pattern, cmap=plt.cm.gray)
    plt.show()

    return pattern
