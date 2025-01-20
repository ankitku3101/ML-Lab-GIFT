import numpy as np
noise = (np.random.random([15]) * 4) - 2
print(noise)
label = np.zeros(15)
label = label + noise
print(label)     