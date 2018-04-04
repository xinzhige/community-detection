# -*- coding: utf-8 -*-
#
# Author:   Zhige Xin <xinzhige8@gmail.com>

# Implement a density function that is used to measure how good a
# community structure is in one social network
"""
Parition density.
"""
import numpy as np


def density(adj, ind):
    """Returns a partition density that is used to measure how good a 
    community structure is for one social network.

    Parameters
    ----------
    adj : adjacency matrix
    ind : indicator matrix

    Returns
    ----------
    Partition density

    Examples
    --------
    >>> from density import density
    >>> W = np.array([[0, 1, 1, 0, 0, 0],
                      [1, 0, 1, 0, 0, 0],
                      [1, 1, 0, 1, 0, 0],
                      [0, 0, 1, 0, 1, 1],
                      [0, 0, 0, 1, 0, 1],
                      [0, 0, 0, 1, 1, 0]])
    >>> U = np.array([[1, 0],
                      [1, 0],
                      [1, 1],
                      [1, 1],
                      [0, 1],
                      [0, 1]])
    >>> print(density(W, U))
    >>> 0.38095238095238093

    References
    ----------
    .. [1] Ahn, Yong-Yeol, James P. Bagrow, and Sune Lehmann. "Link
           communities reveal multiscale complexity in networks." nature
           466, no. 7307 (2010): 761.
    """
    num_communities = ind.shape[1]
    num_edges_all = np.count_nonzero(adj) / 2
    result = 0
    for k in range(num_communities):
        nodes = ind[:, k].nonzero()[0]
        nodes_connected = np.sort(list(set([i for i in nodes for j in nodes
                                            if i != j and adj[i, j] != 0])))
        num_nodes = len(nodes_connected)
        if num_nodes != 1 and num_nodes != 2:
            num_edges = len([i for i in nodes_connected
                             for j in nodes_connected
                             if i != j and adj[i, j] != 0]) / 2
            denominator = (num_nodes - 1) * (num_nodes - 2)
            numerator = num_edges * (num_edges - num_nodes + 1)
            result += numerator / denominator
    result = 2 * result / num_edges_all
    return result
