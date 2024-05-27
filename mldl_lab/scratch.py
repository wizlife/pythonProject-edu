import numpy as np

dims = [4096] * 7
hs = []
x = np.random.randn(16, dims[0])
for d_in, d_out in zip(dims[:-1], dims[1:]):
    W = 0.01 * np.random.randn(d_in, d_out)
    x = np.tanh(x.dot(W))
    hs.append(x)
print(hs)
