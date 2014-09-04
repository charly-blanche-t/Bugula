
import networkx  as nx
import numpy as np
import scipy as sp




def list_directed_cc (H):
    adj_matrix = nx.to_scipy_sparse_matrix(H) # Return the graph adjacency matrix as a SciPy sparse matrix
 
    list_cc = sp.sparse.csgraph.connected_components(adj_matrix, directed=True, connection='weak', return_labels=True)

    print(" All cc: ", list_cc)

    return list_cc
