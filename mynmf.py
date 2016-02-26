import numpy as np
from dif_cost import dif_cost
from divide_nonzero import divide_nonzero

def mynmf(V, k=2, iter=50):
    m = np.shape(V)[0]
    n = np.shape(V)[1]
    W = np.random.rand(m, k)
    H = np.random.rand(k, n)
    for i in xrange(iter):
        WN = V.dot(H.T)
        WD = W.dot(H).dot(H.T)
	W = W * divide_nonzero(WN / WD)
	HN = (W.T).dot(V)
        HD = (W.T).dot(W).dot(H)
        H = H * divide_nonzeor(HN / HD)
        # Compute the loss function
        cost = dif_cost(np.dot(W, H), V)
        print cost
        if cost < 0.001:
            break
    return W, H
