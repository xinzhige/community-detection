# Implement a density function that is used to measure how good a
# community structure is in one social network

import numpy as np


def density(similarity, indicator):
    m = indicator.shape[0]
    n = indicator.shape[1]
    result = 0 
    for j in range(n):
        num_nodes = np.count_nonzero(indicator[:, j]) 
	nodes = indicator[:, j].nonzero()[0].tolist()
	num_edges = 0
        for i in nodes:
            for k in nodes:
                if i < k and similarity[i, k].all():
                    num_edges += 1
	denominator = ((num_nodes * (num_nodes - 1)) / 2 - (num_nodes - 1))
	if denominator != 0:
	    tmp = (num_edges - (num_nodes - 1)) / denominator
	else:
            tmp = 0
        result += (tmp * num_edges) / n
    return result
