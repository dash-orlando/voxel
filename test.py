import numpy as np
import matplotlib.pyplot as plt

x_dim = 240
y_dim = 120

fig=plt.figure()

# make up some data for demo purposes
raw = np.random.randint(2, size=(y_dim,x_dim))
# apply some logic operatioin to the data
#O = (raw >= 5) * 1   # get either 0 or 1 in the array
I = np.random.randint(10, size=(y_dim,x_dim))  # get 0-9 in the array

# plot each image ...
# ... side by side
#fig.add_subplot(1, 2, 1)   # subplot one
#plt.imshow(I, cmap=plt.cm.gray)

#fig.add_subplot(1, 2, 2)   # subplot two
# my data is OK to use gray colormap (0:black, 1:white)
plt.imshow(raw, cmap=plt.cm.gray)  # use appropriate colormap here
plt.show()
