import numpy as np
samples = [[0.47,1],[0.24,1],[0.75,1],[0.00,1],[-0.80,1],[-0.59,1],[1.09,1],[1.34,1],
           [1.01,1],[-1.02,1],[0.50,1],[0.64,1],[-1.15,1],[-1.68,1],[-2.21,1],[-0.52,1],
           [3.93,1],[4.21,1],[5.18,1],[4.20,1],[4.57,1],[2.63,1],[4.52,1],[3.31,1],
           [6.75,1],[3.47,1],[4.32,1],[3.08,1],[4.10,1],[4.00,1],[2.99,1],[3.83,1]]
n = len(samples)
labels = [0]*(n//2) + [1]*(n-n//2)

A = np.matrix(samples)
b = np.matrix(labels).transpose()

print(np.linalg.inv(A.transpose()*A)*A.transpose()*b)
