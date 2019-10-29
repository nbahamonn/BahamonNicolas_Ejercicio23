import os
import numpy as np
import matplotlib.pyplot as plt


a = os.system("c++ walk2.cpp -o walk2.x")
a = os.system("./walk2.x > walk2.dat")

plt.figure()
data = np.loadtxt("walk2.dat")
plt.plot(data[:,0], data[:,1])
plt.axis('square')
plt.xlim([-125, 125])
plt.ylim([-125, 125])
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("walk2.png")