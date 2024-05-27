import numpy as np
import math

a = np.arange(1)
b = np.arange(2)
c = np.arange(3)
d = np.arange(4)

probabilities = [math.exp(-17) * 17 ** k / math.factorial(k) for k in range(30+1)]

a = probabilities[:1]
b = probabilities[:2]
c = probabilities[:0]
d = probabilities[:4]
