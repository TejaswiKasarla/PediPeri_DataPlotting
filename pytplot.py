import numpy as np 
import matplotlib.pyplot as plt



# first we read the file into a numpy array, ignoring comments
data = np.genfromtxt('/home/tejaswikasarla/PediPeri_AprilTags/text.txt',
					 comments = "#",
					 delimiter = ",",
					 dtype = 'float32', 
					 filling_values = 0,
					 usecols = np.arange(0,7))

# Then we parse the data into the 7 values that are being given
distance, x, y, z, yaw, pitch, roll = np.hsplit(data, 7)

# TODO: Convert the angles to degrees

# TODO: We need to smoothen these functions. At present, discontinuities are being plotted as 0. 
# They should not be plotted or else we need to estimate a proper value from them to get a smooth function

# Then we plot all these values
# We start with a 'time' variable which is of the length of each column. Since we know it is 120fps, the delta(T) ~ 8ms.
time = (1000.0/120.0)*np.arange(0, distance.size)

plt.plot(time, distance, 'r')
plt.plot(time, x, 'g')
plt.plot(time, y, 'b')
plt.plot(time, z, 'k')
plt.plot(time, yaw, 'o')
plt.plot(time, pitch, 'r--')
plt.plot(time, roll, 'b--')

plt.show()